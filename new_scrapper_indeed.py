import requests
import re
import time
try:
    from bs4 import BeautifulSoup
except :
    from BeautifulSoup import BeautifulSoup 

import math



def links_scrapper(title, location = "United Kingdom"):

    #Add job title to search. Any space will be reeplaced with a + symbol 

    title = title
    title = title.replace(" ", "+")

    #Add location to search. Any space will be reeplaced with a + symbol. No case sensitive
    location =location
    location = location.replace(" ", "+")

    base_url = "https://www.indeed.co.uk/jobs?q="+title+"&l="+location

    #First url to check for number of ads stracting
    first_url = base_url+"&start=0"

    #conducting a request of the stated URL above:
    first_page = requests.get(first_url)

    #sleep for 5 secs to avoid the site recognising the script as a bot and blocking our IP 
    time.sleep(5)

    #specifying a desired format of “page” using the html parser - this allows python to read the various components of the page, rather than treating it as one long string.
    soup = BeautifulSoup(first_page.text, "html.parser")
    #Extract all the posts of the page
    posts = soup.find_all("a", class_=re.compile("tapItem fs-unmask result job_"))

    #Get number of ads:

    n_ads = int(str(soup.text).partition("Page 1 of")[2].partition("jobs")[0].replace(",", ""))

    #Calculate number of pages, as 15 ads are shown by page. As the last page can have less ads, we will use math.ceil

    n_pages = math.ceil(n_ads /15)

    #Generate a list with all the possible links for the different pages


    def links_pages(pages_url, n_pages = 0):
        #Starting an empty list
        links_pages = []

        #For each page in the range between 0 and the number of pages, add a new link with the page number
        for i in range(int(n_pages)):
            links_pages.append(pages_url + str(i))
        return links_pages

    link_pages = (links_pages(first_url[:-1], n_pages))

    # Def a function to  all the links to ads from a page

    def links_ads(page_url):
        #conducting a request of the stated URL above:
        page = requests.get(page_url)
        #sleep for 5 secs to avoid the site recognising the script as a bot and blocking our IP 
        time.sleep(5)


        #specifying a desired format of “page” using the html parser - this allows python to read the various components of the page, rather than treating it as one long string.
        soup = BeautifulSoup(page.text, "html.parser")

        #Extract all the posts of the page
        posts = soup.find_all("a", class_=re.compile("tapItem fs-unmask result job_"))

        if len(posts) == 0:
            print("No posts found in page " + str(page_url))

        
        
        #Starting an empty list
        links_ads =[]
        #For each page in the range between 0 and the number of ads, add the new link, formatted according the page style

        for i in range(len(posts)):
            print("ad " + str(i+1) + " of " + str(len(posts)) + " in page " + str(page_url))
            link = "https://uk.indeed.com" + str(posts[i]).partition('href="')[2].partition(" ")[0]
            link = link.partition("amp;")[0] + link.partition("amp;")[2]
            link = link.partition("rc/clk")[0] + "viewjob" + link.partition("rc/clk")[2]
            links_ads.append(link)
      

        return links_ads

    # Create an empty list and add all the links

    all_ads_links = []

    for page in range(len(link_pages)):
        print("Page " + str(page + 1) + " of " + str(len(link_pages)))
        all_ads_links = all_ads_links + links_ads(link_pages[page])

    return all_ads_links

all_links = links_scrapper("Data Analyst", location = "United Kingdom")