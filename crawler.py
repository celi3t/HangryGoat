
import requests
import csv
from bs4 import BeautifulSoup

from crawler_tester import smitten_kitchen_rules, iamafoodblog_rules



class LinkRule():
    def __init__(self, rulefun):
        self.rulefun = rulefun
    
    def apply(self, link):
        return self.rulefun(link)



class LinkCrawler():
    def __init__(self, allowed_domain, rules, max_allowed, name, write = False):
        self.max_allowed = max_allowed
        self.allowed_domain = allowed_domain
        self.rules = rules
        self.linklist = []
        if write:
            self.writerpath = f"./data/urls/{name}.csv"
            open(self.writerpath, 'w', newline='')
        else:
            self.writerpath = None 

    def get_new_writer(self, path):
        with open(path, 'w', newline='') as csvfile:
            return csv.writer(csvfile)

    def run_recursive(self, url):
        if len(self.linklist) < self.max_allowed:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            for l in soup.find_all('a'):
                link = l.get('href')
                if link is not None:
                    if link.startswith(self.allowed_domain):
                        if self.rules.apply(link):
                            if link not in self.linklist:
                                print(link)
                                self.linklist.append(link)
                                if self.writerpath:
                                    with open(self.writerpath, 'a', newline='') as csvfile:
                                        w = csv.writer(csvfile)
                                        w.writerow([link])
                                self.run_recursive(link)


# def smitten_kitchen_rules(link):
#     return (len(link.split("/")) == 7 and "?" not in link and "#" not in link)


if __name__ == '__main__':

    domain = 'https://iamafoodblog.com/'
    max_it = 1000
    author = "iamafoodblog"
    skr = LinkRule(iamafoodblog_rules)

    skcrawler = LinkCrawler(domain, skr, max_it, author, write=True)
    print(skcrawler.linklist)
    skcrawler.run_recursive(domain)
    print(len(skcrawler.linklist))
    print(len(set(skcrawler.linklist)))

    # skr = LinkRule(smitten_kitchen_rules)

    # skcrawler = LinkCrawler('https://smittenkitchen.com', skr, 1000, "smitten_kitchen", write=True)
    # print(skcrawler.linklist)
    # skcrawler.run_recursive('https://smittenkitchen.com')
    # # print(skcrawler.linklist)
    # print(len(skcrawler.linklist))
    # print(len(set(skcrawler.linklist)))


#### FOR TESTING LATER
        # print(skr.apply('https://smittenkitchen.com/2021/08/baked-farro-with-summer-vegetables/'))
    # print(skr.apply('https://smittenkiten.com/2021/08/baked-farro-with-summer-vegetables/'))
    # print(skr.apply('https://smittenkiten.com/2021/08/baked-farro-with-summer-vegetables/??jojofds'))


