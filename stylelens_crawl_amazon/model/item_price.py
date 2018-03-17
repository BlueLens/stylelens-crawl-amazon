# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class ItemPrice(Model):
  def __init__(self,
               amount=None,
               currency_code=None,
               formatted_price=None):
    self.bl_types = {
      'amount': str,
      'currency_code': str,
      'formatted_price': str
    }

    self.attribute_map = {
      'amount': 'amount',
      'currency_code': 'currency_code',
      'formatted_price': 'formatted_price'
    }

    self._amount = amount
    self._currency_code = currency_code
    self._formatted_price = formatted_price

  @classmethod
  def from_dict(cls, dikt):
    return deserialize_model(dikt, cls)
  # from_dict.__annotations__ = {'return': 'ItemPrice'}

  @property
  def amount(self):
    return self._amount
  # amount.__annotations__ = {'return': str}

  @amount.setter
  def amount(self, amount):
    self._amount = amount
  # amount.__annotations__ = {'amount': str}

  @property
  def currency_code(self):
    return self._currency_code
  # currency_code.__annotations__ = {'return': str}

  @currency_code.setter
  def currency_code(self, currency_code):
    self._currency_code = currency_code
  # currency_code.__annotations__ = {'currency_code': str}

  @property
  def formatted_price(self):
    return self._formatted_price
  # formatted_price.__annotations__ = {'return': str}

  @formatted_price.setter
  def formatted_price(self, formatted_price):
    self._formatted_price = formatted_price
  # formatted_price.__annotations__ = {'formatted_price': str}
