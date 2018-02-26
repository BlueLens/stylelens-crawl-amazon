import bottlenose
from .search_factory import SearchFactory


class AwsProductApi(object):
  def __init__(self, generate_item_searches=False):
    self._amazon = bottlenose.Amazon()
    self._search_factory = SearchFactory(self._amazon, generate_item_searches)

  def get_item_searches(self):
    return self._search_factory.get_item_searches()

  def get_similar_items(self):
    return self._search_factory.get_similar_items()

  def item_search(self, item_searches):
    return self._search_factory.search(item_searches)

  def item_lookups(self):
    return self._search_factory.lookup_similar_items()
