import sys
from random import randrange
import string
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from blogentry import BlogEntry, BlogEntryCollection
from text_util import TextUtil
from mapreduce_framework import SimpleMapReduce

from sklearn.cluster import KMeans


class RawContentLSHVectorizer():
        
    @staticmethod
    def transform_to_word_matrix(collection):
        words_dict = {}
        words_matrix = {}
        word_counter = 0
        empty_array = [0] * collection.size()
        entry_titles = list()
        for entry_id, entry in enumerate(collection):
            raw_words =  TextUtil.make_lowercase_word_vector(entry.text())
            entry_titles.append(entry.title())
            for w_id, word in enumerate(raw_words):
                if word not in words_dict:
                    words_dict[word] = word_counter
                    words_matrix[word_counter] = list()
                    #print 'before:', words_matrix[word_counter].shape, entry_id, words_matrix[word_counter]
                    words_matrix[word_counter].append(entry_id)
                    #print words_matrix[word_counter].shape, entry_id, words_matrix[word_counter]
                    word_counter += 1
                else:
                    words_matrix[words_dict[word]].append(entry_id)
        
        tot_words = len(words_dict.keys()) 
        wd = {}
        wwd = {}
        for word in words_dict:
            if len(words_matrix[words_dict[word]]) > 8:
                wd[words_dict[word]] = words_matrix[words_dict[word]]   
                wwd[word] = words_dict[word]
        
        words_matrix = wd 
        words_dict = wwd   
        matrix = np.zeros((collection.size(), tot_words))
        for col_index in words_matrix.keys():
            for row_index in words_matrix[col_index]:
                #print row_index, col_index
                matrix[row_index, col_index] = 1
        
        print words_dict.keys()

        return matrix, entry_titles
 
        
    @staticmethod
    def min_hash_fn(a, b, sig): 
        hashes = ((a*np.arange(1, len(sig)+1) + b) % 1274)*sig #[((a * x) + (b % len(sig))) for x in np.arange(len(sig))]
        if len(hashes[hashes != 0]) > 0:
            return min(hashes[hashes != 0])
        else:
            return 0

    @staticmethod
    def get_min_hash_row(sig, band_size, hash_parameters):
        hashes = list()
        for band in RawContentLSHVectorizer.get_band(sig, band_size):
            hash_values = [RawContentLSHVectorizer.min_hash_fn(a, b, sig) for a, b in hash_parameters]
            hashes.append(hash_values)
        return hashes
        
    @staticmethod
    def get_band(l, n):
        for i in xrange(0, len(l), n):
            yield frozenset(l[i:i+n])
            
            
    @staticmethod
    def LSH_cluster_entries(collection):
        words_matrix, entry_titles = RawContentLSHVectorizer.transform_to_word_matrix(collection)
        a_hash = [1,2]#[randrange(sys.maxint) for _ in xrange(0, num_hashes)]#np.arange(1,13)#
        b_hash = [1,3]#[randrange(sys.maxint) for _ in xrange(0, num_hashes)]#np.ones(12)#

        #this dataframe will contain the hash for each band and each hash function
        lsh_df = pd.DataFrame(columns = ['band_id', 'doc_id', 'hash_value', 'entry_titles', 'hash_id'])

        index = 0
        for doc_id, signature in enumerate(words_matrix): #take away the transpose after testing
            num_per_band = len(words_matrix[0, :])
            min_hash_row = RawContentLSHVectorizer.get_min_hash_row(signature, num_per_band, zip(a_hash, b_hash))

            for band_id, band in enumerate(min_hash_row):
                for hashindex, hashvalue in enumerate(band):
                    lsh_df.loc[index, :] = band_id, doc_id, hash(hashvalue), entry_titles[doc_id], hashindex 
                    index += 1

        print 'done computing hash values, now with clustering'

        for band_id, band_values in lsh_df.groupby(['band_id', 'hash_id']):
            band_results = {}
            for doc_id, doc_values in band_values.groupby(['doc_id']):

                value = float(doc_values['hash_value'])#

                if value not in band_results:
                    band_results[value] = list()
                    band_results[value].append(doc_id)
                else:
                    band_results[value].append(doc_id)

            print "Results for band: ", band_id
            print "tot clusters: ", len(band_results), 'tot data:', len(lsh_df) 
            print "\n"

            print "SORTED DATAFRAME"
            bv = band_values.sort(columns = 'hash_value', inplace = False)
            print bv

        
        for band_id, band_values in lsh_df.groupby(['band_id', 'hash_id']):
            model = KMeans(50)

            print np.array(band_values['hash_value']).reshape(len(band_values), 1)
            clusters = model.fit_predict(np.array(band_values['hash_value']).reshape(len(band_values), 1))
        # n_clusters = np.max(clusters)
        # print n_clusters      
            plt.figure()
            plt.scatter(clusters, band_values['hash_value'], alpha = 0.2)
            plt.show()




if __name__ == '__main__':
    collection = BlogEntryCollection.from_json_file(sys.argv[1])
    print collection.size()
    RawContentLSHVectorizer.LSH_cluster_entries(collection)


