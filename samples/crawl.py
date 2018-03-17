from stylelens_crawl_amazon.stylelens_crawl import StylensCrawler

sc = StylensCrawler(generate_item_searches=True)
item_searches = sc.get_item_searches()
i = 0
for s in item_searches:
  data = s.search_data
  print('_: ' + str(i))
  print(data.search_index)
  print(data.keywords)
  print(data.browse_node)
  print(data.response_groups)
  print(data.sort)
  # its = []
  # its.append(s)
  # items = sc.get_items(its)
  # for item in items:
  #   print(item.asin)

  i = i + 1


