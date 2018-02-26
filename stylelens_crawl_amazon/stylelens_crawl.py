from .aws_product_api import AwsProductApi
import traceback

class StylensCrawler(object):
  def __init__(self, generate_item_searches=False):
    self._aws = AwsProductApi(generate_item_searches=generate_item_searches)

  def get_item_searches(self):
    return self._aws.get_item_searches()

  def get_items(self, item_searches):
    item_list = self._aws.item_search(item_searches)
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


