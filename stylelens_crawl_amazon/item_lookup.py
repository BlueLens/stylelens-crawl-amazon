# coding: utf-8

from __future__ import absolute_import
from bs4 import BeautifulSoup
from typing import List, Dict
from stylelens_crawl_amazon.model import Item
from stylelens_crawl_amazon.model import ItemImage
from stylelens_crawl_amazon.model import ItemPrice


class ItemLookup(object):
  def __init__(self,
               amazon,
               item_ids,
               include_reviews_summary=False,
               response_groups=None):

    self._amazon = amazon
    self._item_ids = item_ids
    self._response_groups = response_groups
    self._include_reviews_summary = include_reviews_summary
    self._items = []

  def lookup(self):
    res = self._amazon.ItemLookup(ItemId=','.join(self._item_ids),
                            IncludeReviewsSummary=self._include_reviews_summary,
                            ResponseGroup=self._response_groups)
    soup = BeautifulSoup(res, "xml")
    # print(soup.prettify())
    # self._log(soup.prettify())

    items = soup.find('Items')
    request = items.find('Request')
    isValid = request.IsValid.text
    if isValid != 'True':
      print("isValid is not True")
      return None

    if items.Item:
      item = items.Item

    while True:
      self._extract_item(item)

      item = item.next_sibling
      if not item:
        break
    return self._items

  def _extract_item(self, data, parent_detail_page=None, parent_add_to_wishlist_link=None):
    item = Item()
    item.asin = data.ASIN.text
    if data.ParentASIN:
      item.parent_asin = data.ParentASIN.text

    if data.DetailPageURL:
      item.detail_page_link = data.DetailPageURL.text
    elif parent_detail_page != None:
      item.detail_page_link = parent_detail_page.replace(item.parent_asin, item.asin)

    if data.ItemLinks:
      item_link = data.ItemLinks.ItemLink
      while True:
        if item_link.Description:
          if 'Add To Wishlist' == item_link.Description.text:
            item.add_to_wishlist_link = item_link.URL.text
        item_link = item_link.next_sibling
        if not item_link:
          break
    elif parent_add_to_wishlist_link != None:
      item.add_to_wishlist_link = parent_add_to_wishlist_link.replace(item.parent_asin, item.asin)

    self._extract_images(item, data)

    if data.ItemAttributes:
      self._extract_item_attributes(item, data.ItemAttributes)

    if item.m_image is not None:
      self._items.append(item)

    if data.Variations:
      self._extract_variations(data.Variations, item.detail_page_link, item.add_to_wishlist_link)

    # if data.SimilarProducts:
    #   similar_products = data.SimilarProducts.find_all('SimilarProduct')
    #   for product in similar_products:
    #     if product.ASIN:
    #       self._similar_item_ids.append(product.ASIN.text)

  def _extract_variations(self, variations, parent_detail_page, parent_add_to_wishlist_link):

    if variations.Item:
      item = variations.Item
    else:
      return

    while True:
      self._extract_item(item, parent_detail_page=parent_detail_page, parent_add_to_wishlist_link=parent_add_to_wishlist_link)
      item = item.next_sibling
      if not item:
        break

  def _extract_images(self, item_attributes, data):
    if data.SmallImage:
      ii = ItemImage()
      ii.url = data.SmallImage.URL.text
      ii.height = data.SmallImage.Height.text
      ii.width = data.SmallImage.Width.text
      ii.unit = data.SmallImage.Width['Units']
      item_attributes.s_image = ii

    if data.MediumImage:
      ii = ItemImage()
      ii.url = data.MediumImage.URL.text
      ii.height = data.MediumImage.Height.text
      ii.width = data.MediumImage.Width.text
      ii.unit = data.MediumImage.Width['Units']
      item_attributes.m_image = ii

    if data.LargeImage:
      ii = ItemImage()
      ii.url = data.LargeImage.URL.text
      ii.height = data.LargeImage.Height.text
      ii.width = data.LargeImage.Width.text
      ii.unit = data.LargeImage.Width['Units']
      item_attributes.l_image = ii

  def _extract_item_attributes(self, item, data):
    if data.Binding:
      item.binding = data.Binding.text
    if data.Brand:
      item.brand = data.Brand.text
    if data.Department:
      item.department = data.Department.text
    if data.Color:
      item.color = data.Color.text
    if data.ClothingSize:
      item.clothing_size = data.ClothingSize.text
    if data.ListPrice:
      p = ItemPrice()
      p.amount = data.ListPrice.Amount.text
      p.currency_code = data.ListPrice.CurrencyCode.text
      p.formatted_price = data.ListPrice.FormattedPrice.text

    if data.Feature:
      item.features = []
      feature = data.Feature
      while True:
        item.features.append(feature.text)
        feature = feature.next_sibling
        if feature.name != 'Feature':
          break

    if data.ProductGroup:
      item.product_group = data.ProductGroup.text
    if data.ProductTypeName:
      item.product_type_name = data.ProductTypeName.text
    if data.Title:
      item.title = data.Title.text

  @property
  def item_ids(self) -> List[str]:
    return self._item_ids

  @item_ids.setter
  def item_ids(self, item_ids: List[str]):
    self._item_ids = item_ids

  @property
  def search_index(self) -> str:
    return self._search_index

  @search_index.setter
  def search_index(self, search_index: str):
    self._search_index = search_index

  @property
  def response_groups(self) -> str:
    return self._response_groups

  @response_groups.setter
  def response_groups(self, response_groups: str):
    self._response_groups = response_groups

  @property
  def browse_node(self) -> str:
    return self._browse_node

  @browse_node.setter
  def browse_node(self, browse_node: str):
    self._browse_node = browse_node

  @property
  def sort(self) -> str:
    """
    Sort values
     - ref. : https://docs.aws.amazon.com/ko_kr/AWSECommerceService/latest/DG/LocaleUS.html
    relevancerank
    popularity-rank
    price
    -price
    reviewrank
    launch-date
    """
    return self._sort

  @sort.setter
  def sort(self, sort: str):
    self._sort = sort

  @property
  def item_page(self) -> str:
    return self._item_page

  @item_page.setter
  def item_page(self, item_page: str):
    self._item_page = item_page

  def _log(self, data):
    f = open('lookup_log.txt', 'a', encoding='UTF-8')
    f.write(str(data))
    f.close()
