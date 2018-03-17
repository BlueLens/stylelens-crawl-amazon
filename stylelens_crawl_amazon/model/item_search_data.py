# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model
import traceback


class ItemSearchData(Model):
  def __init__(self,
               keywords=None,
               search_index=None,
               response_groups=None,
               browse_node=None,
               sort=None):
    self.bl_types = {
      'keywords': str,
      'search_index': str,
      'response_groups': str,
      'browse_node': str,
      'sort': str
    }

    self.attribute_map = {
      'keywords': 'keywords',
      'search_index': 'search_index',
      'response_groups': 'response_groups',
      'browse_node': 'browse_node',
      'sort': 'sort'
    }

    self._keywords = keywords
    self._search_index = search_index
    self._response_groups = response_groups
    self._browse_node = browse_node
    self._sort = sort

  @classmethod
  def from_dict(cls, dikt):
    return deserialize_model(dikt, cls)
  # from_dict.__annotations__ = {'return': 'ItemSearchData'}

  @property
  def keywords(self):
    return self._keywords
  # keywords.__annotations__ = {'return': str}

  @keywords.setter
  def keywords(self, keywords):
    self._keywords = keywords
  # keywords.__annotations__ = {'keywords': str}

  @property
  def search_index(self):
    return self._search_index
  # search_index.__annotations__ = {'return': str}

  @search_index.setter
  def search_index(self, search_index):
    self._search_index = search_index
  # search_index.__annotations__ = {'search_index': str}

  @property
  def response_groups(self):
    return self._response_groups
  # response_groups.__annotations__ = {'return': str}

  @response_groups.setter
  def response_groups(self, response_groups):
    self._response_groups = response_groups
  # response_groups.__annotations__ = {'response_groups': str}

  @property
  def browse_node(self):
    return self._browse_node
  # browse_node.__annotations__ = {'return': str}

  @browse_node.setter
  def browse_node(self, browse_node):
    self._browse_node = browse_node
  # browse_node.__annotations__ = {'browse_node': str}

  @property
  def sort(self):
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
  # sort.__annotations__ = {'return': str}

  @sort.setter
  def sort(self, sort):
    self._sort = sort
  # sort.__annotations__ = {'sort': str}

