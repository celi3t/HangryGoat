
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv


def parse_page(url):
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
                else:
                    res['tags'] = ""
            else:
                print("ingredients not found")
                print(ingredient_block)
        else:
            print("ingredient block not found")
            print(url)
            print(ingredient_block)
    return res



if __name__ == '__main__':
    with open('../data/urls/smitten_kitchen.csv', 'r') as csvlinks:
        links = csv.reader(csvlinks)
        results = []
        for l in links:
            # print(l)
            parsed = parse_page(l[0])
            if len(parsed) > 0:
                results.append(parsed)
        
    df = pd.DataFrame(results)
    df.to_csv('../data/parsed/smitten_kitchen.csv', index = False)



## 1. drop everything that is not a letter or a number
## 2. measurement words
## 3. extra_words
## 4. processing words

