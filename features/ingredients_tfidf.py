import pandas as pd
import re
import string
import itertools
import nltk
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

from gensim.test.utils import common_texts
from gensim.models import Phrases
from gensim.models import Word2Vec
### Uses "Phrases" from gensim.
### Phrases implements collocation statistics to find which words go together as n grams
### Useful for identifying ingredients in a list of ingredients, e.g.
### Salt, Kosher salt, Himalayan salt
### Then use Word2Vec on n-gram-transformed dataset

##### Read data
raw_ingredients = pd.read_csv("/Users/celeste/code/HangryGoat/data/parsed/ingredients_1.csv")

print(raw_ingredients.head())


