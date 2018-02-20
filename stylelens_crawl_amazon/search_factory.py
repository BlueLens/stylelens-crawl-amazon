from __future__ import absolute_import

from stylelens_crawl_amazon.item_search import ItemSearch
from stylelens_crawl_amazon.item_lookup import ItemLookup
from .browse_nodes import BrowseNodes

CATEGORIES     = 'stylelens_crawl_amazon/data/categories.txt'
SEARCH_INDICES = 'stylelens_crawl_amazon/data/search_indices.txt'
SORTS          = 'stylelens_crawl_amazon/data/sorts.txt'
ITEM_SEARCH_RESPONSE_GROUPS= 'stylelens_crawl_amazon/data/item_search_response_groups.txt'
ITEM_LOOKUP_RESPONSE_GROUPS= 'stylelens_crawl_amazon/data/item_lookup_response_groups.txt'
ATTRIB_TEXTURE = 'stylelens_crawl_amazon/data/attribute_texture.txt'
ATTRIB_FABRIC  = 'stylelens_crawl_amazon/data/attribute_fabric.txt'
ATTRIB_SHAPE   = 'stylelens_crawl_amazon/data/attribute_shape.txt'
ATTRIB_PART    = 'stylelens_crawl_amazon/data/attribute_part.txt'
ATTRIB_STYLE   = 'stylelens_crawl_amazon/data/attribute_style.txt'

class SearchFactory(object):
  def __init__(self, amazon):
    self._amazon = amazon
    self._keywords = []
    self._browse_nodes = {}
    self._search_indices = []
    self._categories = []
    self._attrib_list = []
    self._item_searches = []
    self._sorts = []
    self._response_groups = []

    self._init()
    self._item_ids = []

  def search(self):
    for i in self._item_searches:
      items, similar_item_ids = i.search()
      _item_lookups = self._lookup_similar_items(similar_item_ids)
      for l in _item_lookups:
        similar_items = l.lookup()
        print(len(similar_items))
      print(len(items))
      print(len(similar_item_ids))

  def _init(self):
    self._browse_nodes = self._get_browse_nodes()
    if self._browse_nodes is None:
      print('Can not get BrowseNodes from AWS')
      return
    self._init_attributes()
    self._init_categories()
    self._init_search_indices()
    self._init_item_search_response_groups()
    self._init_item_lookup_response_groups()
    self._init_sorts()
    self._generate_keywords_small() # or self._generate_keywords_large()
    self._item_searches = self._generate_item_searchs()

  def _init_categories(self):
    self._categories.extend(self._get_items(CATEGORIES))

  def _init_item_search_response_groups(self):
    self._response_groups.extend(self._get_items(ITEM_SEARCH_RESPONSE_GROUPS))

  def _init_item_lookup_response_groups(self):
    self._response_groups.extend(self._get_items(ITEM_LOOKUP_RESPONSE_GROUPS))

  def _init_sorts(self):
    self._sorts.extend(self._get_items(SORTS))

  def _init_search_indices(self):
    self._search_indices.extend(self._get_items(SEARCH_INDICES))

  def _init_attributes(self):
    self._attrib_list.append(self._get_items(ATTRIB_TEXTURE))
    self._attrib_list.append(self._get_items(ATTRIB_FABRIC))
    self._attrib_list.append(self._get_items(ATTRIB_SHAPE))
    self._attrib_list.append(self._get_items(ATTRIB_PART))
    self._attrib_list.append(self._get_items(ATTRIB_STYLE))

  def _get_browse_nodes(self):
    try:
      bn = BrowseNodes()
    except Exception as e:
      print(e)
      return None

    return bn.get_browse_nodes()

  def _generate_keywords_small(self):
    for c in self._categories:
      self._keywords.append(c)

    for attributes in self._attrib_list:
      for a in attributes:
        self._keywords.append(a)

  def _generate_keywords_large(self):
    for c in self._categories:
      self._keywords.append(c)
      for attributes in self._attrib_list:
        for a in attributes:
          self._keywords.append(a + ' ' + c)

  def _generate_item_searchs(self):
    for search_index in self._search_indices:
      for sort in self._sorts:
        for keyword in self._keywords:
          response_groups = ','.join(self._response_groups)
          if search_index == 'Apparel':
            for browse_node in self._browse_nodes.values():
              yield self._generate_item_search(search_index=search_index,
                                               sort=sort,
                                               keyword=keyword,
                                               response_groups=response_groups,
                                               browse_node=browse_node)
          else:
            yield self._generate_item_search(search_index=search_index,
                                             sort=sort,
                                             keyword=keyword,
                                             response_groups=response_groups)

  def _generate_item_search(self,
                            search_index,
                            sort,
                            keyword,
                            response_groups,
                            browse_node=None):
    i = ItemSearch(amazon=self._amazon)
    i.search_index = search_index
    i.browse_node = browse_node
    i.sort = sort
    i.response_groups = response_groups
    i.keywords = keyword
    return i


  def _get_items(self, file=None):
    items_ = open(file, 'r', encoding='UTF-8')
    items = []
    for i in items_.readlines():
      items.append(i.strip())

    return items

  def _chunks(self, l, n):
    for i in range(0, len(l), n):
      yield l[i:i + n]

  def _lookup_similar_items(self, item_ids):
    response_groups = ','.join(self._response_groups)
    for ids in self._chunks(item_ids, 10):
      yield self._generate_item_lookup(item_ids=ids,
                                       response_groups=response_groups)


  def _generate_item_lookup(self,
                            item_ids,
                            search_index=None,
                            response_groups=None):
    i = ItemLookup(amazon=self._amazon, item_ids=item_ids)
    i.response_groups = response_groups

    return i


