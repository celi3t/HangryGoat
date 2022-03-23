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
paths = ["/Users/celeste/code/HangryGoat/data/parsed/iamafoodblog.csv", \
"/Users/celeste/code/HangryGoat/data/parsed/smitten_kitchen.csv"]

data = []
for path in paths:
    data.append(pd.read_csv(path))

df = pd.concat(data, axis = 0)

measure_words = pd.read_csv("/Users/celeste/code/HangryGoat/data/nlp_stuff/measurements.csv", header = None).values
measure_words = list(itertools.chain(*measure_words))

#### Everything to lower case
#### Only keep letters and spaces

raw = df['ingredients'].apply(lambda x: x.replace("[", "").replace("}", "").split("', '")).explode("ingredients").values
# take out punctuation and numbers
raw = [re.sub("[0-9]+", "", x).lower() for x in raw]

table = str.maketrans('', '', "!#$%&'()*+,./:;<=>?@[\]^_`{|}~")
raw = [w.translate(table) for w in raw]

tokenized = [word_tokenize(x) for x in raw]
# If I wanted to flatten all sentences in one big document:
# tokenized = list(itertools.chain(*tokenized))
#print(tokenized)

#### Take out stop words
#nltk.download('stopwords')
stopwords.fileids() 
stopw = stopwords.words('english')
stopw += measure_words

doc = []
for sentence in tokenized:
    sent = []
    for word in sentence:
        ### TODO: eliminate the s at the end, or some for of word stemming
        ### Also add numbers to stopwords
        if word not in stopw:
            sent.append(word)
    if len(sent) > 0:
        doc.append(sent)



#doc =  [['unsalted', 'butter', 'melted'], ['light', 'dark', 'brown', 'sugar'], ['granulated', 'sugar'], ['ground', 'cinnamon'], ['kosher', 'salt'], ['all-purpose', 'flour'], ['unsalted', 'butter', 'softened'], ['granulated', 'sugar'], ['large', 'egg'], ['sour', 'cream'], ['vanilla', 'extract'], ['all-purpose', 'flour'], ['baking', 'powder'], ['kosher', 'salt']]
# toks = [toks.append(tok) for tok in tokens if tok not in stopw]
# print(doc)
###Word to vec example

### Preprocess with phrases
phrases = Phrases(doc, min_count=1, threshold=1)

trained = []
for p in doc:
    print(phrases[p])
    trained.append(phrases[p])

phrases.save("/tmp/ingredients.pkl")
print(trained[0:5])
tt = [str(x).replace("[", "").replace("]", "") for x in trained]
print(tt[0:5])

ing = pd.DataFrame({"ingredient": tt})

ing.to_csv("/Users/celeste/code/HangryGoat/data/parsed/ingredients_1.csv", index = False)





#phrase_model.add_vocab([["hello", "world"], ["meow"]])
#frozen_model = phrase_model.freeze()





######## OLD CODE THAT WILL NEED TO BE DELETED


# new_sentence = ['kosher', 'salt', 'lemon']
# print(phrases[new_sentence])
# phrases[doc]
# print(phrases[['salt']])

# model = Word2Vec(sentences=trained, vector_size=100, window=2, min_count=1, workers=4)
# # # #model.save("word2vec.model")

# # # model.train([doc], total_examples=len(doc), epochs = 10)

# # vector = model.wv['kosher']  # get numpy vector of a word
# # print(vector)
# similars = model.wv.most_similar('kosher_salt', topn=5)  
# print(similars)



# # Train a bigram detector.
# from gensim.models.word2vec import Text8Corpus
# sentences = Text8Corpus(datapath('testcorpus.txt'))

# bigram_transformer = 
# # Apply the trained MWE detector to a corpus, using the result to train a Word2vec model.
# # model = Word2Vec(bigram_transformer[common_texts], min_count=1)
# for phrase, score in bigram_transformer.find_phrases(sentences).items():
#     print(phrase, score)
