# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('--json', help='json data filepath')
# parser.add_argument('--keyword', help='keyword for word count', nargs = '*')
# parser.add_argument('--granularity', help='fields to group data by', nargs = '*')
# args = parser.parse_args()
# 
# filepath = args.json
# keywords = args.keyword
# groupbykey = args.granularity
# 
# print filepath
# print keywords
# print groupbykey

#from data_importer import collection_to_dataframe
from group_by import group_by
#from featurizer import Featurizer

import sys
sys.path.append('/Users/celi/Desktop/FoodMath/hangry-goat.git/util/')
from blogentry import BlogEntry, BlogEntryCollection
from transformer import DiscardBody, ToLowerCase, StripPunctuation

sample_text = 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin \
literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, \
looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in \
classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum \
et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular\
during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.The \
standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from \
"de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from \
the 1914 translation by H. Rackham.'


if __name__ == '__main__':
    #collection = BlogEntryCollection.from_json_file(sys.argv[1])
    filepath = '/Users/celi/Desktop/FoodMath/hangry-goat.git/scrapy/hangrygoat/analysis/data/full_text_jtb.json'#'full_text_jtb.json'
    collection = BlogEntryCollection.from_json_file(filepath)
    print collection.size()
    data = collection.to_dataframe()
    data_as_string = list()
    for datum in data['raw_content']:
        data_as_string.append(str(datum))
    
    from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
    from sklearn.decomposition import NMF
    
    vect = CountVectorizer(input='content', lowercase=True, stop_words='english')
    v = vect.fit_transform(data_as_string[:])#
    #print data_as_string[11]

    transformer = TfidfTransformer()
    vocabulary = vect.get_feature_names()
    X = transformer.fit_transform(v)
    print v.shape, X.shape
    
    nmf = NMF(n_components=20, random_state=1).fit(X)
    n_top_words = 5
    #print("done in %0.3fs." % (time() - t0))

    feature_names = vocabulary

    for topic_idx, topic in enumerate(nmf.components_):
        print "Topic #%d:" % topic_idx
        print " ".join([feature_names[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]])
        print "\n"

    # better_voc = list()
    # for w, weight in enumerate(X): 
    #     print weight
    #     if weight > 0.05:
    #         better_voc.append(vocabulary[w])
    
    # from sklearn.cluster import KMeans
    # from sklearn import metrics
    # true_k = 2
    # km = KMeans(2)
    # y = km.fit(X)
    # 
    # print y
    
    # print "Homogeneity: %0.3f" % metrics.homogeneity_score(labels, km.labels_)
    # print "Completeness: %0.3f" % metrics.completeness_score(labels, km.labels_)
    # print "V-measure: %0.3f" % metrics.v_measure_score(labels, km.labels_)
    # print "Adjusted Rand-Index: %.3f" % metrics.adjusted_rand_score(labels, km.labels_)
    # print "Silhouette Coefficient: %0.3f" % metrics.silhouette_score(X, km.labels_, sample_size=1000)

    # print "\n"
    # 
    # print "Top terms per cluster:" 
    # order_centroids = km.cluster_centers_.argsort()[:, ::-1]
    # terms = vect.get_feature_names()
    # for i in range(true_k):
    #     print "Cluster %d:" % i#, end= ' ' 
    #     for ind in order_centroids[i, :10]:
    #         print ' %s' % terms[ind]#, end=''
    
    
    # import matplotlib.pyplot as plt
    # 
    # plt.figure()
    # plt.scatter(y, y)
    # plt.show()
    #print transformer.get_feature_names()    
    
    #grouped_data = group_by(data, 'year', 'month')
    #print grouped_data
    #featurizer = Featurizer(grouped_data)

    #featurizer.word_count('orange', column = 'raw_content', exact_match = False)
    #print featurizer.feature_matrix
