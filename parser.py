
import requests
from bs4 import BeautifulSoup

### Store ingredients and text in a database
### Search by ingredient(s)
### Store tags too

### terminal visualization template

### ADD button from slack



page = requests.get("https://smittenkitchen.com/2021/12/short-rib-onion-soup/")
# print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())

# print(list(soup.children))

# for link in soup.find_all('a'):
#     print(link.get('href'))

# for link in soup.find_all('div', class_='jetpack-recipe-ingredients'):
#     print(link.find_all('li', "jetpack-recipe-ingredient p-ingredient ingredient"))


# print(soup.title.text)
ingredients = []
for i in soup.find_all('div', class_='jetpack-recipe-ingredients')[0].find_all('li'):
    ingredients.append(i.text)

print(ingredients)

# for step in soup.find_all('div', class_='jetpack-recipe-directions e-instructions'):
#         print(step.prettify())
for c in soup.find_all('span', class_='cat-links'):
    print(c.text)