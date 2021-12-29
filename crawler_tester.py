
import requests
import csv
from bs4 import BeautifulSoup




def show_links(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.find_all('a'))
    for l in soup.find_all('a'):
        link = l.get('href')
        if link is not None:
            if link.startswith(url):
                if iamafoodblog_rules(link):
                    print(link)



def smitten_kitchen_rules(link):
    return (len(link.split("/")) == 7 and "?" not in link and "#" not in link)

def iamafoodblog_rules(link):
    return (len(link.split("/")) == 5 and "?" not in link and "#" not in link)


if __name__ == '__main__':
    show_links('https://iamafoodblog.com/')