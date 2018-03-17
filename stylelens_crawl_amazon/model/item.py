# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model
from .item_image import ItemImage
from .item_price import ItemPrice


class Item(Model):
  def __init__(self,
               asin=None,
               parent_asin=None,
               detail_page_link=None,
               add_to_wishlist_link=None,
               title=None,
               s_image=None,
               m_image=None,
               l_image=None,
               binding=None,
               brand=None,
               department=None,
               color=None,
               clothing_size=None,
               size=None,
               price=None,
               lowest_price=None,
               highest_price=None,
               features=None,
               label=None,
               manufacturer=None,
               product_group=None,
               product_type_name=None):
    self.bl_types = {
      'asin': str,
      'parent_asin': str,
      'detail_page_link': str,
      'add_to_wishlist_link': str,
      'title': str,
      's_image': ItemImage,
      'm_image': ItemImage,
      'l_image': ItemImage,
      'binding': str,
      'brand': str,
      'department': str,
      'color': str,
      'clothing_size': str,
      'size': str,
      'price': ItemPrice,
      'lowest_price': ItemPrice,
      'highest_price': ItemPrice,
      'features': List[str],
      'label': str,
      'manufacturer': str,
      'product_group': str,
      'product_type_name': str
    }

    self.attribute_map = {
      'asin': 'asin',
      'parent_asin': 'parent_asin',
      'detail_page_link': 'detail_page_link',
      'add_to_wishlist_link': 'add_to_wishlist_link',
      'title': 'title',
      's_image': 's_image',
      'm_image': 'm_image',
      'l_image': 'l_image',
      'binding': 'binding',
      'brand': 'brand',
      'department': 'department',
      'color': 'color',
      'clothing_size': 'clothing_size',
      'size': 'size',
      'price': 'price',
      'lowest_price': 'lowest_price',
      'highest_price': 'highest_price',
      'features': 'features',
      'label': 'label',
      'manufacturer': 'manufacturer',
      'product_group': 'product_group',
      'product_type_name': 'product_type_name'
    }

    self._asin = asin
    self._parent_asin = parent_asin
    self._detail_page_link = detail_page_link
    self._add_to_wishlist_link = add_to_wishlist_link
    self._title = title
    self._s_image = s_image
    self._m_image = m_image
    self._l_image = l_image
    self._binding = binding
    self._brand = brand
    self._department = department
    self._color = color
    self._clothing_size = clothing_size
    self._size = size
    self._price = price
    self._lowest_price = lowest_price
    self._highest_price = highest_price
    self._features = features
    self._label = label
    self._manufacturer = manufacturer
    self._product_group = product_group
    self._product_type_name = product_type_name

  @classmethod
  def from_dict(cls, dikt):
    return deserialize_model(dikt, cls)
  # from_dict.__annotations__ = {'return': 'Item'}

  @property
  def asin(self):
    return self._asin
  # asin.__annotations__ = {'return': str}

  @asin.setter
  def asin(self, asin):
    self._asin = asin
  # asin.__annotations__ = {'asin':str}

  @property
  def parent_asin(self):
    return self._parent_asin
  # parent_asin.__annotations__ = {'return': str}

  @parent_asin.setter
  def parent_asin(self, parent_asin):
    self._parent_asin = parent_asin
  # parent_asin.__annotations__ = {'parent_asin': str}

  @property
  def detail_page_link(self):
    return self._detail_page_link
  # detail_page_link.__annotations__ = {'return': str}

  @detail_page_link.setter
  def detail_page_link(self, detail_page_link):
    self._detail_page_link = detail_page_link
  # detail_page_link.__annotations__ = {'detail_page_link': str}

  @property
  def add_to_wishlist_link(self):
    return self._add_to_wishlist_link
  # add_to_wishlist_link.__annotations__ = {'return': str}

  @add_to_wishlist_link.setter
  def add_to_wishlist_link(self, add_to_wishlist_link):
    self._add_to_wishlist_link = add_to_wishlist_link
  # add_to_wishlist_link.__annotations__ = {'add_to_wishlist_link': str}

  @property
  def title(self):
    return self._title
  # title.__annotations__ = {'return': str}

  @title.setter
  def title(self, title):
    self._title = title
  # title.__annotations__ = {'title': str}

  @property
  def s_image(self):
    return self._s_image
  # s_image.__annotations__ = {'return': ItemImage}

  @s_image.setter
  def s_image(self, s_image):
    self._s_image = s_image
  # s_image.__annotations__ = {'s_image': ItemImage}

  @property
  def m_image(self):
    return self._m_image
  # m_image.__annotations__ = {'return': ItemImage}

  @m_image.setter
  def m_image(self, m_image):
    self._m_image = m_image
  # m_image.__annotations__ = {'m_image': ItemImage}

  @property
  def l_image(self):
    return self._l_image
  # l_image.__annotations__ = {'l_image': ItemImage}

  @l_image.setter
  def l_image(self, l_image):
    self._l_image = l_image
  # l_image.__annotations__ = {'l_image': ItemImage}

  @property
  def binding(self):
    return self._binding
  # binding.__annotations__ = {'return': str}

  @binding.setter
  def binding(self, binding):
    self._binding = binding
  # binding.__annotations__ = {'binding': str}

  @property
  def brand(self):
    return self._brand
  # brand.__annotations__ = {'return': str}

  @brand.setter
  def brand(self, brand):
    self._brand = brand
  # brand.__annotations__ = {'brtand': str}

  @property
  def department(self):
    return self._department
  # department.__annotations__ = {'return': str}

  @department.setter
  def department(self,  department):
    self._department= department
  # department.__annotations__ = {'department': str}

  @property
  def color(self):
    return self._color
  # color.__annotations__ = {'return': str}

  @color.setter
  def color(self,  color):
    self._color = color
  # color.__annotations__ = {'color': str}

  @property
  def clothing_size(self):
    return self._clothing_size
  # clothing_size.__annotations__ = {'return': str}

  @clothing_size.setter
  def clothing_size(self, clothing_size):
    self._clothing_size = clothing_size
  # clothing_size.__annotations__ = {'clothing_size': str}

  @property
  def size(self):
    return self._size
  # size.__annotations__ = {'return': str}

  @size.setter
  def size(self, size):
    self._size = size
  # size.__annotations__ = {'size': str}

  @property
  def price(self):
    return self._price
  # price.__annotations__ = {'return': ItemPrice}

  @price.setter
  def price(self, price):
    self._price = price
  # price.__annotations__ = {'price': ItemPrice}

  @property
  def lowest_price(self):
    return self._lowest_price
  # lowest_price.__annotations__ = {'return': ItemPrice}

  @lowest_price.setter
  def lowest_price(self, lowest_price):
    self._lowest_price = lowest_price
  # lowest_price.__annotations__ = {'lowest_price': ItemPrice}

  @property
  def highest_price(self):
    return self._highest_price
  # highest_price.__annotations__ = {'return': ItemPrice}

  @highest_price.setter
  def highest_price(self, highest_price):
    self._highest_price = highest_price
  # highest_price.__annotations__ = {'highest_price': ItemPrice}

  @property
  def features(self):
    return self._features
  # features.__annotations__ = {'return': List[str]}

  @features.setter
  def features(self, features):
    self._features = features
  # features.__annotations__ = {'features': List[str]}

  @property
  def label(self):
    return self._label
  # label.__annotations__ = {'return': str}

  @label.setter
  def label(self, label):
    self._label = label
  # label.__annotations__ = {'label': str}

  @property
  def manufacturer(self):
    return self._manufacturer
  # manufacturer.__annotations__ = {'return': str}

  @manufacturer.setter
  def manufacturer(self, manufacturer):
    self._manufacturer = manufacturer
  # manufacturer.__annotations__ = {'manufacturer': str}

  @property
  def product_group(self):
    return self._product_group
  # product_group.__annotations__ = {'return': str}

  @product_group.setter
  def product_group(self, product_group):
    self._product_group = product_group
  # product_group.__annotations__ = {'product_group': str}

  @property
  def product_type_name(self):
    return self._product_type_name
  # product_type_name.__annotations__ = {'return': str}

  @product_type_name.setter
  def product_type_name(self, product_type_name):
    self._product_type_name= product_type_name
  # product_type_name.__annotations__ = {'product_type_name': str}
