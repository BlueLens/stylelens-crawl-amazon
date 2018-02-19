# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class ItemAttributes(Model):
  def __init__(self, title=None, binding=None, brand=None,
               department=None, features=None, label=None, manufacturer=None,
               product_group=None, product_type_name=None,
               publisher=None, studio=None):
    self.swagger_types = {
      'title': str,
      'binding': str,
      'brand': str,
      'department': str,
      'features': List[str],
      'label': str,
      'manufacturer': str,
      'product_group': str,
      'product_type_name': str,
      'publisher': str,
      'studio': str
    }

    self.attribute_map = {
      'title': 'title',
      'binding': 'binding',
      'brand': 'brand',
      'department': 'department',
      'features': 'features',
      'label': 'label',
      'manufacturer': 'manufacturer',
      'product_group': 'product_group',
      'product_type_name': 'product_type_name',
      'publisher': 'publisher',
      'studio': 'studio'
    }

    self._title = title
    self._binding = binding
    self._brand = brand
    self._department = department
    self._features = features
    self._label = label
    self._manufacturer = manufacturer
    self._product_group = product_group
    self._product_type_name = product_type_name
    self._publisher = publisher
    self._studio = studio

  @classmethod
  def from_dict(cls, dikt) -> 'ItemAttributes':
    return deserialize_model(dikt, cls)

  @property
  def title(self) -> str:
    return self._title

  @title.setter
  def title(self, title: str):
    self._title = title

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

  @property
  def publisher(self) -> str:
    return self._publisher

  @publisher.setter
  def publisher(self, publisher: str):
    self._publisher= publisher

  @property
  def studio(self) -> str:
    return self._studio

  @studio.setter
  def studio(self, studio: str):
    self._studio= studio
