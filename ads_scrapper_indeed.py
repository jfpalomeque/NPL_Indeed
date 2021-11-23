import requests
import re
from bs4 import BeautifulSoup
import bs4


def ads_scrapper_indeed(link, keyword=None):

    # Request page from link

    ad_page = requests.get(link)

    # Parser of the page
    page_soup = BeautifulSoup(ad_page.text, "html.parser")

    # Extraction of ad title
    title = page_soup.find_all("div", class_=re.compile
                               ("""title-container """))
    title = page_soup.find("h1").contents[0]

    if title is None:
        title = "Nan"

    # Extraction of ad company
    company = page_soup.find_all("div", class_=re.compile
                                 ("""jobsearch-InlineCompanyRating """))[0]
    company = company.contents[0].contents[0]                             

    if company is None:
        company = "Nan"
    elif not isinstance(company, bs4.element.NavigableString):
        company = company.contents[0]

    # Extraction of ad company
    description = page_soup.find("div", {"id": "jobDescriptionText"}).text

    if description is None:
        description = "Nan"

    location = page_soup.find_all("div", class_=re.compile("JobInfoHeader"))
    location = location[-1]
    location = location.contents[-1].contents[0]

    if location is None:
        location = "Nan"

    rating = page_soup.find_all("div", class_=re.compile("JobInfoHeader"))
    rating = str(rating).partition('aria-label="')[2]
    rating = rating.partition("out of 5 stars")[0]

    if rating == "":
        rating = "Nan"
    else:
        rating = rating.split()[0]

    ad_info = [title, company, rating, location, description, keyword, link]
    return ad_info
 



