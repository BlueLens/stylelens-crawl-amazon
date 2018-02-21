from stylelens_crawl_amazon.stylelens_crawl import StylensCrawler

sc = StylensCrawler()
items = sc.get_items()
for item in items:
  print(item.asin)
