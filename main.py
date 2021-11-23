from links_scrapper_indeed import links_scrapper
from ads_scrapper_indeed import ads_scrapper_indeed

keyword = "Data Analyst"
all_links = links_scrapper(keyword, location="United Kingdom", num_pages=1)
ads_db = []
for index, link in enumerate(all_links):
    print(str(index + 1) + " of " + str(len(all_links)))
    ads_db.append(ads_scrapper_indeed(all_links[index], keyword))
