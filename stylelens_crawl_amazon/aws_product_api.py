import bottlenose
from .search_factory import SearchFactory


class AwsProductApi(object):
  def __init__(self):
    self._amazon = bottlenose.Amazon()
    self._search_factory = SearchFactory(self._amazon)

  def item_search(self):
    return self._search_factory.search()

  def item_lookups(self):
    return self._search_factory.lookup_similar_items()
