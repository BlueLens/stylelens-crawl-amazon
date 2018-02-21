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
  def from_dict(cls, dikt) -> 'ItemPrice':
    return deserialize_model(dikt, cls)

  @property
  def amount(self) -> str:
    return self._amount

  @amount.setter
  def amount(self, amount: str):
    self._amount = amount

  @property
  def currency_code(self) -> str:
    return self._currency_code

  @currency_code.setter
  def currency_code(self, currency_code: str):
    self._currency_code = currency_code

  @property
  def formatted_price(self) -> str:
    return self._formatted_price

  @formatted_price.setter
  def formatted_price(self, formatted_price : str):
    self._formatted_price = formatted_price
