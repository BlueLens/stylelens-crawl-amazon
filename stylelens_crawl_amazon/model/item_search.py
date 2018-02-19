# coding: utf-8

from __future__ import absolute_import
from bs4 import BeautifulSoup


class ItemSearch(object):
  def __init__(self,
               amazon,
               keywords=None,
               search_index=None,
               response_groups=None,
               browse_node=None,
               sort=None,
               item_page=None):

    self._amazon = amazon
    self._keywords = keywords
    self._search_index = search_index
    self._response_groups = response_groups
    self._browse_node = browse_node
    self._sort = sort
    self._item_page = item_page
    self._item_ids = []

  def search(self):
    page = 1
    total_pages = 0
    max_page = 10
    while True:
      res = self._amazon.ItemSearch(Keywords=self._keywords,
                              SearchIndex=self._search_index,
                              BrowseNode=self._browse_node,
                              Availability='Available',
                              ItemPage=page,
                              Sort=self._sort,
                              ResponseGroup=self._response_groups)
      soup = BeautifulSoup(res, "xml")

      # print(soup)
      items = soup.find('Items')

      request = items.find('Request')
      isValid = request.IsValid.string
      if isValid == 'True':
        print('valid')

      total_pages_tag = items.find('TotalPages')
      if total_pages_tag != None:
        total_pages = int(total_pages_tag.text)
        # print('total pages : ' + total_pages_tag.text)
      else:
        print('')

      item_list = items.find_all('Item')
      for item in item_list:
        self._item_ids.append(item.ASIN.text)
        # print(item.ASIN.text)
        # print(item.DetailPageURL.text)
        # if item.Binding:
        #   binding = item.Binding.text
        #   print(binding)
        # if item.Brand:
        #   print(item.Brand.text)
        # if item.Department:
        #   print(item.Department.text)
        # features = item.find_all('Feature')
        # for feature in features:
        #   print('Feature:' + feature.text)
        #
        # if item.Label:
        #   print('Label:' + item.Label.text)
        # if item.Manufacturer:
        #   print('Manufacturer:' + item.Manufacturer.text)
        # if item.Model:
        #   print('Model:' + item.Model.text)
        # print('ProductGroup:' + item.ProductGroup.text)
        # print('ProductTypeName:' + item.ProductTypeName.text)
        # if item.Publisher:
        #   print('Publisher:' + item.Publisher.text)
        # if item.Studio:
        #   print('studio:' + item.Studio.text)
        # if item.Title:
        #   print(item.Title.text)

        if item.SimilarProducts:
          similar_products = item.SimilarProducts.find_all('SimilarProduct')
          for product in similar_products:
            if product.ASIN:
              self._item_ids.append(product.ASIN.text)

      page = page + 1

      if page > max_page or page > total_pages:
        break

    return set(self._item_ids)

  @property
  def keywords(self) -> str:
    return self._keywords

  @keywords.setter
  def keywords(self, keywords: str):
    self._keywords = keywords

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
