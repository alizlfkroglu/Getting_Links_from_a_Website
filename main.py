import requests
from bs4 import BeautifulSoup

target_url = "https://news.ycombinator.com/"
foundLinks = []
y= 30
def make_request(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

def crawl(url):
    links= make_request(url)
    for link in links.find_all("a"):
        found_link = link.get("href")
        if found_link not in foundLinks:
            foundLinks.append(found_link)
        if "https" in found_link:
            found_link= found_link.split()
            print(found_link)

crawl(target_url)








