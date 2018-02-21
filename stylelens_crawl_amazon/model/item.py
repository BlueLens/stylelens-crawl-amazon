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
    self._features = features
    self._label = label
    self._manufacturer = manufacturer
    self._product_group = product_group
    self._product_type_name = product_type_name

  @classmethod
  def from_dict(cls, dikt) -> 'Item':
    return deserialize_model(dikt, cls)

  @property
  def asin(self) -> str:
    return self._asin

  @asin.setter
  def asin(self, asin: str):
    self._asin = asin

  @property
  def parent_asin(self) -> str:
    return self._parent_asin

  @parent_asin.setter
  def parent_asin(self, parent_asin: str):
    self._parent_asin = parent_asin

  @property
  def detail_page_link(self) -> str:
    return self._detail_page_link

  @detail_page_link.setter
  def detail_page_link(self, detail_page_link: str):
    self._detail_page_link = detail_page_link

  @property
  def add_to_wishlist_link(self) -> str:
    return self._add_to_wishlist_link

  @add_to_wishlist_link.setter
  def add_to_wishlist_link(self, add_to_wishlist_link: str):
    self._add_to_wishlist_link = add_to_wishlist_link

  @property
  def title(self) -> str:
    return self._title

  @title.setter
  def title(self, title: str):
    self._title = title

  @property
  def s_image(self) -> ItemImage:
    return self._s_image

  @s_image.setter
  def s_image(self, s_image: ItemImage):
    self._s_image = s_image

  @property
  def m_image(self) -> ItemImage:
    return self._m_image

  @m_image.setter
  def m_image(self, m_image: ItemImage):
    self._m_image = m_image

  @property
  def l_image(self) -> ItemImage:
    return self._l_image

  @l_image.setter
  def l_image(self, l_image: ItemImage):
    self._l_image = l_image

  @property
  def binding(self) -> str:
    return self._binding

  @binding.setter
  def binding(self, binding: str):
    self._binding = binding

  @property
  def brand(self) -> str:
    return self._brand

  @brand.setter
  def brand(self, brand: str):
    self._brand = brand

  @property
  def department(self) -> str:
    return self._department

  @department.setter
  def department(self,  department: str):
    self._department= department

  @property
  def color(self) -> str:
    return self._color

  @color.setter
  def color(self,  color: str):
    self._color = color

  @property
  def clothing_size(self) -> str:
    return self._clothing_size

  @clothing_size.setter
  def clothing_size(self, clothing_size: str):
    self._clothing_size = clothing_size

  @property
  def size(self) -> str:
    return self._size

  @size.setter
  def size(self, size: str):
    self._size = size

  @property
  def price(self) -> ItemPrice:
    return self._price

  @price.setter
  def price(self, price: ItemPrice):
    self._price = price

  @property
  def features(self) -> List[str]:
    return self._features

  @features.setter
  def features(self, features: List[str]):
    self._features = features

  @property
  def label(self) -> str:
    return self._label

  @label.setter
  def label(self, label: str):
    self._label = label

  @property
  def manufacturer(self) -> str:
    return self._manufacturer

  @manufacturer.setter
  def manufacturer(self, manufacturer: str):
    self._manufacturer = manufacturer

  @property
  def product_group(self) -> str:
    return self._product_group

  @product_group.setter
  def product_group(self, product_group: str):
    self._product_group = product_group

  @property
  def product_type_name(self) -> str:
    return self._product_type_name

  @product_type_name.setter
  def product_type_name(self, product_type_name: str):
    self._product_type_name= product_type_name
