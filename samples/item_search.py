import bottlenose
from bs4 import BeautifulSoup


amazon = bottlenose.Amazon()

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


page = 1
max_page = 10
while True:
  response = amazon.ItemSearch(Keywords="open-back",
                               SearchIndex="FashionWomen",
                               ItemPage=page,
                               BrowseNode=None,
                               Availability='Available',
                               Sort='launch-date',
                               ResponseGroup='ItemAttributes,Images,Similarities,Variations')
  soup = BeautifulSoup(response, "xml")

  # print(soup)
  items = soup.find('Items')

  request = items.find('Request')
  isValid = request.IsValid.string
  if isValid == 'True':
    print('valid')

  totalPages = items.find('TotalPages')
  print(totalPages)

  item_list = items.find_all('Item')
  for item in item_list:
    print(item.ASIN.text)
    print(item.DetailPageURL.text)
    itemAttributes = item.ItemAttributes
    if item.Binding:
      binding = item.Binding.text
      print(item.Brand.text)
    if item.Department:
      print(item.Department.text)
    features = item.find_all('Feature')
    for feature in features:
      print('Feature:' + feature.text)

    if item.Label:
      print('Label:' + item.Label.text)
    if item.Manufacturer:
      print('Manufacturer:' + item.Manufacturer.text)
    if item.Model:
      print('Model:' + item.Model.text)
    print('ProductGroup:' + item.ProductGroup.text)
    print('ProductTypeName:' + item.ProductTypeName.text)
    if item.Publisher:
      print('Publisher:' + item.Publisher.text)
    if item.Studio:
      print('studio:' + item.Studio.text)
    print(item.Title.text)
    print('__________')

  # if int(totalPages) > page:
  print('page ======== : ' + str(page))
  page = page + 1

  if page > max_page:
    break


