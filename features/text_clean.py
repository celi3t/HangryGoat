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

df = pd.read_csv("/Users/celeste/code/HangryGoat/data/parsed/smitten_kitchen.csv")

measure_words = pd.read_csv("/Users/celeste/code/HangryGoat/data/nlp_stuff/measurements.csv", header = None).values
measure_words = list(itertools.chain(*measure_words))


#### Everything to lower case
#### Only keep letters and spaces

raw = df['ingredients'].apply(lambda x: x.replace("[", "").replace("}", "").split(",")).explode("ingredients").head().values
# take out punctuation and numbers
raw = [re.sub("[0-9]+", "", x).lower() for x in raw]

table = str.maketrans('', '', "!#$%&'()*+,./:;<=>?@[\]^_`{|}~")
raw = [w.translate(table) for w in raw]
# print(raw)

#### Now tokenize
tokens = [word_tokenize(x) for x in raw]
tokens = list(itertools.chain(*tokens))
# print(tokens)

#### Take out stop words
#nltk.download('stopwords')
stopwords.fileids() 
stopw = stopwords.words('english')
stopw += measure_words
toks = []
for tok in tokens:
    if tok not in stopw:
        toks.append(tok)
#toks = [toks.append(tok) for tok in tokens if tok not in stopw]
# print(toks)

### Do (TF IDF) a histogram to eliminate other words that are used to describe ingredients and are not ingredients
## print(Counter(toks))

#### Word Stemming
porter = PorterStemmer()
stemmed = [porter.stem(word) for word in toks]
print(stemmed)


print(len(toks))
print(len(stemmed))


#### Count Vecotrizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(raw)
print(vectorizer.get_feature_names_out())
X = X.toarray()

ingr_dict = {}
for i in range(0, X.shape[1]):
    for j, ingredient in enumerate(vectorizer.get_feature_names_out()):
        if ingredient not in ingr_dict:
            ingr_dict[ingredient] = 1
            
        print(ingredient)


# for i, ingredient in enumerate(vectorizer.get_feature_names_out()):
#     print(ingredient)
#     print(len(X.toarray()[i]))

# beef AND Bone:
# Tot beef
# tot beef and bone

# print([re.sub("[0-9]+", "", x) for x in raw])


# nltk.download('punkt')





