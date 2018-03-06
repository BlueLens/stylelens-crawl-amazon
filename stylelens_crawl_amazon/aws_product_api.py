import bottlenose
import time
import random
from urllib.error import HTTPError
from .search_factory import SearchFactory


class AwsProductApi(object):
  def __init__(self, generate_item_searches=False):
    self._amazon = bottlenose.Amazon(ErrorHandler=self._error_handler)
    self._search_factory = SearchFactory(self._amazon, generate_item_searches)

  def _error_handler(self, err):
    ex = err['exception']
    if isinstance(ex, HTTPError) and ex.code == 503:
      time.sleep(random.expovariate(0.5))
      return True


  def get_item_searches(self):
    return self._search_factory.get_item_searches()

  def get_similar_items(self):
    return self._search_factory.get_similar_items()

  def item_search(self, item_searches):
    return self._search_factory.search(item_searches)

  def item_lookups(self):
    return self._search_factory.lookup_similar_items()
