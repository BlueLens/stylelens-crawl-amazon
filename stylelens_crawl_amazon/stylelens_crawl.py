from .aws_product_api import AwsProductApi
import traceback

class StylensCrawler(object):
  def __init__(self):
    self._aws = AwsProductApi()

  def get_items(self):
    item_list = self._aws.item_search()
    try:
      for items in item_list:
        for item in items:
          yield item
    except Exception as e:
      print(e)
      traceback.print_exc(limit=None)
      yield None

  def get_similar_items(self):
    item_list = self._aws.item_lookups()
    try:
      for items in item_list:
        for item in items:
          yield item
    except Exception as e:
      print(e)
      traceback.print_exc(limit=None)
      yield None


