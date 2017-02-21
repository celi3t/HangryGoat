import nltk

data = "This dd gg chapter dd gg is dividedd into dd gg sections that dd gg skip between two dd gg quite dd gg ddifferent styles. ddIn the \"computing dd gg with ladddnguage\" sections we will take on some linguistically ddmotivated programming taddsks without dd gg necessarily explaining how they work. In the \"closer look at Python\" sections we will systematically review key programming concepts. We'll flag the two styles in the section titles, but later chapters will mix both styles without being so up-front about it. We hope this style of introduction gives you an authentic taste of what will come later, while covering a range of elementary concepts in linguistics and computer science. If you have basic familiarity with both areas, you can skip to 5; we will repeat any important points in later chapters, and if you miss anything you can easily consult the online reference material at http://nltk.org/. If the material is completely new to you, this chapter will raise more questions than it answers, questions that are addressed in the rest of this book.".lower()




from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans

import json
from dateutil.parser import parse

jtb_path = '/Users/celi/Desktop/FoodMath/hangry-goat.git/scrapy/hangrygoat/analysis/items.json'

corpus = []
for element in json.load(open(jtb_path)):
    if len(element['title']) > 0:
        corpus.append(element['title'][0])



print corpus.concordance('butter')

ksdn
vectorizer = CountVectorizer(min_df=1)
X = vectorizer.fit_transform(corpus).toarray()

analyze = vectorizer.build_analyzer()

print vectorizer

fd = nltk.FreqDist(corpus)
fd.plot()
fd.plot(50, cumulative=True)
fd.most_common(5)


model1 = KMeans(n_clusters = 10)

y = model1.fit_predict(X)

print model1.score(X)

# bigram_measures = nltk.collocations.BigramAssocMeasures()
# trigram_measures = nltk.collocations.TrigramAssocMeasures()
# finder = nltk.collocations.BigramCollocationFinder.from_words(data)
# 
# 
# print bigram_measures.pmi
# print finder
# print finder.nbest(bigram_measures.pmi, 5)