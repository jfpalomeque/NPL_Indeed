from links_scrapper_indeed import links_scrapper
from ads_scrapper_indeed import ads_scrapper_indeed

keyword = "Data Analyst"
all_links = links_scrapper(keyword, location="United Kingdom", num_pages=1)
ads_db = []
ads_db.append(ads_scrapper_indeed(all_links[0], keyword))