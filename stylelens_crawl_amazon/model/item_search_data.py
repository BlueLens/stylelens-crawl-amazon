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
  def from_dict(cls, dikt) -> 'ItemSearchData':
    return deserialize_model(dikt, cls)

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

