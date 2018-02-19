import bottlenose
from .search_factory import SearchFactory


class AwsProductApi(object):
  def __init__(self):
    print('init')
    self._amazon = bottlenose.Amazon()
    self._search_factory = SearchFactory(self._amazon)

  def item_search(self):
    print('item_search')
    self._search_factory.search()