# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class ItemImage(Model):
  def __init__(self,
               url=None,
               height=None,
               width=None,
               unit=None):
    self.bl_types = {
      'url': str,
      'height': str,
      'width': str,
      'unit': str
    }

    self.attribute_map = {
      'url': 'url',
      'height': 'height',
      'width': 'width',
      'unit': 'unit'
    }

    self._url = url
    self._height = height
    self._width = width
    self._unit = unit

  @classmethod
  def from_dict(cls, dikt) -> 'ItemImage':
    return deserialize_model(dikt, cls)

  @property
  def url(self) -> str:
    return self._url

  @url.setter
  def url(self, url: str):
    self._url = url

  @property
  def height(self) -> str:
    return self._height

  @height.setter
  def height(self, height: str):
    self._height = height

  @property
  def width(self) -> str:
    return self._width

  @width.setter
  def width(self, width: str):
    self._width= width

  @property
  def unit(self) -> str:
    return self._unit

  @unit.setter
  def unit(self, unit: str):
    self._unit = unit
