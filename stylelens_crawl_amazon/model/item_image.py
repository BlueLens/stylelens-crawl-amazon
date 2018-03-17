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
  def from_dict(cls, dikt):
    return deserialize_model(dikt, cls)
  # from_dict.__annotations__ = {'return': 'ItemImage'}

  @property
  def url(self):
    return self._url
  # url.__annotations__ = {'return': str}

  @url.setter
  def url(self, url):
    self._url = url
  # url.__annotations__ = {'url': str}

  @property
  def height(self):
    return self._height
  # height.__annotations__ = {'return': str}

  @height.setter
  def height(self, height):
    self._height = height
  # height.__annotations__ = {'height': str}

  @property
  def width(self):
    return self._width
  # width.__annotations__ = {'return': str}

  @width.setter
  def width(self, width):
    self._width= width
  # width.__annotations__ = {'width': str}

  @property
  def unit(self):
    return self._unit
  # unit.__annotations__ = {'return': str}

  @unit.setter
  def unit(self, unit):
    self._unit = unit
  # unit.__annotations__ = {'unit': str}
