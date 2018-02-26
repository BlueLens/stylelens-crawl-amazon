from stylelens_crawl_amazon.stylelens_crawl import StylensCrawler

sc = StylensCrawler()
item_searches = sc.get_item_searches()


items = sc.get_items()
for item in items:
  print(item.asin)
