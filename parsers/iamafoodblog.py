
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv



class IAmAFoodBlog():
    def __init__(self):
        self.domain = "iamafoodblog.com"
        self.results = {}

    def parse_page(self, url):
        res = {}
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            ingredients = []

            ingredient_block = soup.find_all('div', class_='wprm-recipe-ingredients-container')
            if len(ingredient_block) > 0:  
                for i in ingredient_block[0].find_all('li'):
                    ingredients.append(i.text)

            tags = []
            tags_block = soup.find_all('span', class_='topcat')
            if len(tags_block) > 0:
                for t in tags_block:
                    tags.append(t.text)

            title = soup.find('title').text.replace(" · i am a food blog", "").replace("i am a food blog", "")
            
            if len(ingredients) > 0:
                res['ingredients'] = ingredients
                res['title'] = title
                res['url'] = url
                res['author'] = "iamafoodblog"
                res['tags'] = str(tags)      
                print("added new recipe: " + title)
        except:
            print("failed to connect to: " + url)

        self.results = res



if __name__ == '__main__':
    with open('../data/urls/iamafoodblog.csv', 'r') as csvlinks:
        links = csv.reader(csvlinks)
        results = []
        for l in links:
            parser = IAmAFoodBlog()
            parser.parse_page(l[0])
            if len(parser.results) > 0:
                results.append(parser.results)
        
    df = pd.DataFrame(results)
    df.to_csv('../data/parsed/iamafoodblog.csv', index = False)



## 1. drop everything that is not a letter or a number
## 2. measurement words
## 3. extra_words
## 4. processing words

