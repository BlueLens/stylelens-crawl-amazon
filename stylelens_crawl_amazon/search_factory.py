from __future__ import absolute_import

import os
from stylelens_crawl_amazon.item_search import ItemSearch
from stylelens_crawl_amazon.model.item_search_data import ItemSearchData
from stylelens_crawl_amazon.item_lookup import ItemLookup
from .browse_nodes import BrowseNodes

CATEGORIES     = 'data/categories.txt'
SEARCH_INDICES = 'data/search_indices.txt'
SORTS_APPAREL  = 'data/sorts_Apparel.txt'
SORTS_FASHION  = 'data/sorts_Fashion.txt'
ITEM_SEARCH_RESPONSE_GROUPS= 'data/item_search_response_groups.txt'
ITEM_LOOKUP_RESPONSE_GROUPS= 'data/item_lookup_response_groups.txt'
ATTRIB_TEXTURE = 'data/attribute_texture.txt'
ATTRIB_FABRIC  = 'data/attribute_fabric.txt'
ATTRIB_SHAPE   = 'data/attribute_shape.txt'
ATTRIB_PART    = 'data/attribute_part.txt'
ATTRIB_STYLE   = 'data/attribute_style.txt'

class SearchFactory(object):
  def __init__(self, amazon, generate_item_searches=False):
    self._amazon = amazon
    self._keywords = []
    self._browse_nodes = {}
    self._search_indices = []
    self._categories = []
    self._attrib_list = []
    self._item_searches = []
    self._sorts_apparel = []
    self._sorts_fashion = []
    self._search_response_groups = []
    self._lookup_response_groups = []
    self._item_ids = {}
    self._similar_item_ids = []

    if generate_item_searches == True:
      self._init()

  def search(self, item_searches):
    for i in item_searches:
      items, similar_item_ids = i.search(self._amazon)
      self._save_similar_item_ids(similar_item_ids)
      yield items

  def lookup_similar_items(self):
    _item_lookups = self._lookup_similar_items()
    for l in _item_lookups:
      items = l.lookup()
      print(len(items))
      yield items

  def get_item_searches(self):
    return self._item_searches

  def get_similar_items(self):
    return self._similar_item_ids

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
    self._init_sorts_apparel()
    self._init_sorts_fashion()
    self._generate_keywords_small() # or self._generate_keywords_large()
    self._item_searches = self._generate_item_searches()

  def _init_categories(self):
    self._categories.extend(self._get_items(CATEGORIES))

  def _init_item_search_response_groups(self):
    self._search_response_groups.extend(self._get_items(ITEM_SEARCH_RESPONSE_GROUPS))

  def _init_item_lookup_response_groups(self):
    self._lookup_response_groups.extend(self._get_items(ITEM_LOOKUP_RESPONSE_GROUPS))

  def _init_sorts_apparel(self):
    self._sorts_apparel.extend(self._get_items(SORTS_APPAREL))

  def _init_sorts_fashion(self):
    self._sorts_fashion.extend(self._get_items(SORTS_FASHION))

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

  def _generate_item_searches(self):
    response_groups = ','.join(self._search_response_groups)

    for search_index in self._search_indices:
      if search_index == 'Apparel':
        for sort in self._sorts_apparel:
          for browse_node in self._browse_nodes.values():
            for keyword in self._keywords:
              yield self._generate_item_search(search_index=search_index,
                                               sort=sort,
                                               keyword=keyword,
                                               response_groups=response_groups,
                                               browse_node=browse_node)
      else:
        for sort in self._sorts_fashion:
          for keyword in self._keywords:
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
    i = ItemSearch()
    data = ItemSearchData()
    data.keywords = keyword
    data.search_index = search_index
    data.browse_node = browse_node
    data.sort = sort
    data.response_groups = response_groups
    i.search_data = data
    return i


  def _get_items(self, file=None):
    this_dir, this_filename = os.path.split(__file__)
    file = os.path.join(this_dir, file)
    items_ = open(file, 'r', encoding='UTF-8')
    items = []
    for i in items_.readlines():
      items.append(i.strip())

    return items

  def _chunks(self, l, n):
    for i in range(0, len(l), n):
      yield l[i:i + n]

  def _lookup_similar_items(self ):
    response_groups = ','.join(self._response_groups)
    for ids in self._chunks(self._similar_item_ids, 10):
      yield self._generate_item_lookup(item_ids=ids,
                                       response_groups=response_groups)


  def _generate_item_lookup(self,
                            item_ids,
                            response_groups=None):
    i = ItemLookup(amazon=self._amazon, item_ids=item_ids)
    i.response_groups = response_groups

    return i

  def _save_similar_item_ids(self, ids):
    self._similar_item_ids.extend(ids)
    self._similar_item_ids = list(set(self._similar_item_ids))

