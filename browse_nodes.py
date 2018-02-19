import bottlenose
from bs4 import BeautifulSoup


amazon = bottlenose.Amazon()

# version: 2018.2.13
# Departments/Women/Clothing:1040660
# Departments/Women/Shops/Contemporary & Designer/Clothing:11300395011
# Departments/Women/Shops/Juniors:7581674011
# Departments/Women/Shops/Maternity:7581675011
# Departments/Women/Shops/Petite:7581676011
# Departments/Women/Shops/Plus-Size:7581677011
# Departments/Women/Shops/Uniforms, Work & Safety/Clothing:7606660011
# Departments/Men/Clothing:1040658
# Departments/Men/Shops/Contemporary & Designer/Clothing:11307731011
# Departments/Men/Shops/Big & Tall:7581681011
# Departments/Men/Shops/Uniforms, Work & Safety/Clothing:7606661011
# Departments/Men/Shops/Surf, Skate & Street/Clothing:9564526011
# Departments/Girls/Clothing:1040664
# Departments/Girls/Shops/School Uniforms/Clothing:2492634011
# Departments/Boys/Clothing:1040666
# Departments/Boys/Shops/School Uniforms/Clothing:2492627011
# Departments/Baby/Baby Girls/Clothing:1044512
# Departments/Baby/Baby Boys/Clothing:1044510
# Departments/Novelty & More/Clothing/Novelty/Women:9056921011
# Departments/Novelty & More/Clothing/Novelty/Men:9056985011
# Departments/Novelty & More/Clothing/Novelty/Girls:9057038011
# Departments/Novelty & More/Clothing/Novelty/Boys:9057092011
# Departments/Novelty & More/Clothing/Novelty/Baby:9057141011
# Departments/Novelty & More/Clothing/Exotic Apparel/Women:2491298011
# Departments/Novelty & More/Clothing/Exotic Apparel/Men:1261192011
# Departments/Uniforms, Work & Safety/Clothing:1265851011
# Departments/Traditional & Cultural Wear:7586166011


node_list = [
  'Departments/Women/Clothing',
  'Departments/Women/Shops/Contemporary & Designer/Clothing',
  'Departments/Women/Shops/Juniors',
  'Departments/Women/Shops/Maternity',
  'Departments/Women/Shops/Petite',
  'Departments/Women/Shops/Plus-Size',
  'Departments/Women/Shops/Uniforms, Work & Safety/Clothing',
  'Departments/Men/Clothing',
  'Departments/Men/Shops/Contemporary & Designer/Clothing',
  'Departments/Men/Shops/Big & Tall',
  'Departments/Men/Shops/Uniforms, Work & Safety/Clothing',
  'Departments/Men/Shops/Surf, Skate & Street/Clothing',
  'Departments/Girls/Clothing',
  'Departments/Girls/Shops/School Uniforms/Clothing',
  'Departments/Boys/Clothing',
  'Departments/Boys/Shops/School Uniforms/Clothing',
  'Departments/Baby/Baby Girls/Clothing',
  'Departments/Baby/Baby Boys/Clothing',
  'Departments/Novelty & More/Clothing/Novelty/Women',
  'Departments/Novelty & More/Clothing/Novelty/Men',
  'Departments/Novelty & More/Clothing/Novelty/Girls',
  'Departments/Novelty & More/Clothing/Novelty/Boys',
  'Departments/Novelty & More/Clothing/Novelty/Baby',
  'Departments/Novelty & More/Clothing/Exotic Apparel/Women',
  'Departments/Novelty & More/Clothing/Exotic Apparel/Men',
  'Departments/Uniforms, Work & Safety/Clothing',
  'Departments/Traditional & Cultural Wear'
]

black_list = [
  'Shoes',
  'Jewelry',
  'Handbags',
  'Wallets',
  'Accessories'
]


def get_browse_nodes(name=None, browse_node_id=None):
  for n in name:
    for b in black_list:
      if b in n:
        return None
  if len(name) > 0:
    flattened_name = "/".join(str(x) for x in name)
    for node in node_list:
      if node in flattened_name:
        return None

  response = amazon.BrowseNodeLookup(BrowseNodeId=browse_node_id)
  soup = BeautifulSoup(response, "xml")
  isValid = soup.BrowseNodes.Request.IsValid.string

  if isValid == 'True':
    children = soup.BrowseNodes.BrowseNode.Children
    if children is not None:
      browseNodes = soup.BrowseNodes.BrowseNode.Children.find_all('BrowseNode')
      for browseNode in browseNodes:
        name.append(browseNode.Name.string)
        flattened_name = "/".join(str(x) for x in name)
        if flattened_name in node_list:
          print(flattened_name + ':' + browseNode.BrowseNodeId.string)
        ret = get_browse_nodes(name, browseNode.BrowseNodeId.string)
        if ret is None:
          name.pop()

    else:
      return None

# All
get_browse_nodes([], '7141123011')

# One by One
# get_browse_nodes(['Departments','Men'], '7147441011')
# get_browse_nodes(['Departments','Girls'], '7147442011')
# get_browse_nodes(['Departments','Boys'], '7147443011')
# get_browse_nodes(['Departments','Baby'], '7147444011')
# get_browse_nodes(['Departments','Novelty & More'], '7147445011')
# get_browse_nodes(['Departments','Luggage & Travel Gear'], '9479199011')
# get_browse_nodes(['Departments','Uniforms, Work & Safety'], '7586144011')
# get_browse_nodes(['Departments','Costumes & Accessories'], '7586165011')
# get_browse_nodes(['Departments','Shoe, Jewelry & Watch Accessories'], '7586146011')
# get_browse_nodes(['Departments','Traditional & Cultural Wear'], '7586166011')

# response = amazon.ItemLookup(ItemId="B01DFKC2SO")
# response = amazon.ItemSearch(Keywords="pants", SearchIndex="All")
# response = amazon.ItemLookup(ItemId="163357", ResponseGroup="SalesRank")
# response = amazon.ItemLookup(ItemId="B0769BGRYM", ResponseGroup="BrowseNodes") #pants
# response = amazon.ItemLookup(ItemId="B073P7GFG3", ResponseGroup="BrowseNodes")
# response = amazon.BrowseNodeLookup(BrowseNodeId='7141123011') #Clothing, Shoes & Jewelry
# response = amazon.BrowseNodeLookup(BrowseNodeId='7141124011') #Departments
# response = amazon.BrowseNodeLookup(BrowseNodeId='7147440011') #Departments/Women
# response = amazon.ItemSearch(Keywords="pants", SearchIndex="Fashion", BrowseNode='7141124011')
# response = amazon.ItemLookup(ItemId="B0744PTT8F", ResponseGroup="ItemAttributes,Images,Variations,Offers")
# response = amazon.ItemSearch(Keywords="pants", SearchIndex="Fashion", BrowseNode='7141124011', ResponseGroup='PromotionSummary,Offers')
# response = amazon.ItemSearch(Keywords="zig", SearchIndex="Apparel", ResponseGroup="ItemAttributes,BrowseNodes")
# response = amazon.SimilarityLookup(ItemId='B01GRP0KFQ', SearchIndex="Apparel", ResponseGroup="Small,ItemAttributes")
# response = amazon.ItemSearch(Keywords="shirts", SearchIndex="Apparel", ResponseGroup='BrowseNodes')
# response = amazon.ItemSearch(Keywords="skirt", SearchIndex="Apparel", ResponseGroup='BrowseNodes')

