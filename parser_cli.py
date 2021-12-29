
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

import fire

from search.indexer import index_dict

from parsers.smittenkitchen import SmittenKitchen
from parsers.iamafoodblog import IAmAFoodBlog


def parse(url):
    parsers = {}
    parsers["smittenkitchen.com"] = SmittenKitchen()
    parsers["iamafoodblog.com"] = IAmAFoodBlog()
    for key, par in parsers.items():
        if key in url:
            par.parse_page(url)
            if len(par.results) > 0:
                print(par.results)
                index_dict(par.results)




#### USAGE:
#### python3 parser_cli.py parse https://iamafoodblog.com/tiktok-ramen/
if __name__ == '__main__':
    fire.Fire()

