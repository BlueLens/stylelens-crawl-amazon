from .aws_product_api import AwsProductApi

class StylensCrawler(object):
  def __init__(self):
    print('init')
    self._aws = AwsProductApi()

  def start(self):
    print('start')
    self._aws.item_search()

