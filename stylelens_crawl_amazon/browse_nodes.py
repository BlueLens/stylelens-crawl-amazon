from __future__ import absolute_import
import os
import bottlenose
from bs4 import BeautifulSoup


BROWSE_NODE_WHITE_LIST_FILE = 'data/browse_nodes_white.txt'
BROWSE_NODE_BLACK_LIST_FILE = 'data/browse_nodes_black.txt'
BROWSE_NODE_CACHE = 'browse_node_cache.txt'

class BrowseNodes(object):
  def __init__(self, name=[], id='7141123011'):
    print('init')
    self._browse_nodes = {}
    self._amazon = bottlenose.Amazon()
    self._white_list = self._get_white_list()
    self._black_list = self._get_black_list()
    self._init_browse_nodes(name, id)

  def get_browse_nodes(self):
    return self._browse_nodes

  def _get_browse_nodes_from_cache(self):
    nodes_ = open(BROWSE_NODE_CACHE, 'r', encoding='UTF-8')
    for n in nodes_.readlines():
      map = n.strip().split(':')
      key = map[0].strip()
      value = map[1].strip()
      self._browse_nodes[key] = value

  def _init_browse_nodes(self, name=None, id=None):
    if os.path.exists(BROWSE_NODE_CACHE):
      self._get_browse_nodes_from_cache()
    else:
      self._get_browse_nodes(name, id)
      self._save_to_cache()

  def _get_browse_nodes(self, name=None, id=None):
    for n in name:
      for b in self._black_list:
        if b in n:
          return None
    if len(name) > 0:
      flattened_name = "/".join(str(x) for x in name)
      for node in self._white_list:
        if node in flattened_name:
          return None

    response = self._amazon.BrowseNodeLookup(BrowseNodeId=id)
    soup = BeautifulSoup(response, "xml")
    isValid = soup.BrowseNodes.Request.IsValid.string

    if isValid == 'True':
      children = soup.BrowseNodes.BrowseNode.Children
      if children is not None:
        browseNodes = soup.BrowseNodes.BrowseNode.Children.find_all('BrowseNode')
        for browseNode in browseNodes:
          name.append(browseNode.Name.string)
          flattened_name = "/".join(str(x) for x in name)
          if flattened_name in self._white_list:
            print(flattened_name + ':' + browseNode.BrowseNodeId.string)
            self._browse_nodes[flattened_name] = browseNode.BrowseNodeId.string
          # print(flattened_name)
          ret = self._get_browse_nodes(name, browseNode.BrowseNodeId.string)
          if ret is None:
            name.pop()
      else:
        return None

  def _get_white_list(self):
    this_dir, this_filename = os.path.split(__file__)
    file = os.path.join(this_dir, BROWSE_NODE_WHITE_LIST_FILE)
    node_list = open(file, 'r', encoding='UTF-8')
    nodes = []
    for node in node_list.readlines():
      nodes.append(node.strip())

    return nodes

  def _get_black_list(self):
    this_dir, this_filename = os.path.split(__file__)
    file = os.path.join(this_dir, BROWSE_NODE_BLACK_LIST_FILE)
    node_list = open(file, 'r', encoding='UTF-8')
    nodes = []
    for node in node_list.readlines():
      nodes.append(node.strip())

    return nodes

  def _save_to_cache(self):
    f = open(BROWSE_NODE_CACHE, 'w', encoding='UTF-8')
    for key in self._browse_nodes.keys():
      data = '{}:{}\n'.format(key, self._browse_nodes[key])
      f.write(data)
    f.close()
