
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv


class SmittenKitchen():
    def __init__(self):
        self.domain = "smittenkitchen.com"
        self.results = {}

    def parse_page(self, url):
        res = {}
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            ingredients = []
            ingredient_block = soup.find_all('div', class_='jetpack-recipe-ingredients')
            tags_block = soup.find_all('span', class_='cat-links')
            if len(ingredient_block) > 0:
                for i in ingredient_block[0].find_all('li'):
                    ingredients.append(i.text)
            
                if len(ingredients) > 0:
                    res['ingredients'] = ingredients
                    res['title'] = soup.find('title').text.replace(" – smitten kitchen", "")
                    res['url'] = url
                    res['author'] = "smitten kitchen"

                    if len(tags_block) > 0:
                        print(tags_block[0].text)
                        res['tags'] = tags_block[0].text
        except:
            print("failed to connect to: " + url)

        self.results = res



if __name__ == '__main__':
    sk = SmittenKitchen()
    with open('../data/urls/smitten_kitchen.csv', 'r') as csvlinks:
        links = csv.reader(csvlinks)
        results = []
        for l in links:
            # print(l)
            sk.parse_page(l[0])
            if len(sk.results) > 0:
                results.append(sk.results)
        
    df = pd.DataFrame(results)
    df.to_csv('../data/parsed/smitten_kitchen.csv', index = False)



## 1. drop everything that is not a letter or a number
## 2. measurement words
## 3. extra_words
## 4. processing words

