from .aws_product_api import AwsProductApi

class StylensCrawler(object):
  def __init__(self):
    self._aws = AwsProductApi()

  def get_items(self):
    item_list = self._aws.item_search()
    for items in item_list:
      for item in items:
        yield item

  def get_similar_items(self):
    item_list = self._aws.item_lookups()
    for items in item_list:
      for item in items:
        yield item


