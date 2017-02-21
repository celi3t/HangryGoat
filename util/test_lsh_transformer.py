import unittest
from lsh_transformer import *
from datetime import datetime

from blogentry import BlogEntry, BlogEntryCollection
from text_util import TextUtil

class TestLSHTransformer(unittest.TestCase):
    
    def test_transform(self):
        #collection = BlogEntryCollection.from_json_file(sys.argv[1])
        #print collection.size()

        #words_matrix, entry_titles = RawContentVectorizer.transform_to_word_matrix(collection) #np.zeros((6,3))#

        words_matrix = np.zeros((6,3))
        words_matrix[:, 0] = np.array([1,1,1,0,0,0])
        words_matrix[:, 1] = np.array([1,1,1,1,0,0])
        words_matrix[:, 2] = np.array([1,0,0,0,1,1])
        
        entry_titles = ['a', 'b', 'c']

        a_hash = [1]#[randrange(sys.maxint) for _ in xrange(0, num_hashes)]#np.arange(1,13)#
        b_hash = [1]#[randrange(sys.maxint) for _ in xrange(0, num_hashes)]#np.ones(12)#

        #print zip(a_hash, b_hash)

        lsh_df = pd.DataFrame(columns = ['band', 'doc_id', 'hash_value', 'entry_titles'])
        index = 0
        titles = list()
        for doc_id, signature in enumerate(words_matrix): #take away the transpose after testing
            num_per_band = len(words_matrix[0, :])
            min_hash_row = RawContentVectorizer.get_min_hash_row(signature, num_per_band)
            #print min_hash_row

            #
            #banded = RawContentVectorizer.get_band(min_hash_row, num_per_band)
            # 
            for band_id, band in enumerate(min_hash_row):
                #print band
                lsh_df.loc[index, :] = band_id, doc_id, hash(band[0]), entry_titles[doc_id] #hash(band)
                index += 1

        print lsh_df

        #from sklearn.cluster import MeanShift

        for band_id, band_values in lsh_df.groupby(['band']):
        #     band_results = {}
        #     for doc_id, doc_values in band_values.groupby(['doc_id']):
        #     
        #         value = float(doc_values['hash_value'])
        #         if value not in band_results:
        #             band_results[value] = list()
        #             band_results[value].append(doc_id)
        #         else:
        #             band_results[value].append(doc_id)
        #             
        #     print "Results for band: ", band_id
        #     print "tot clusters: ", len(band_results)
        #     print band_results
        #     print "\n"


            # model = MeanShift()
            # clusters = model.fit_predict(np.array(band_values['hash_value']))
            # n_clusters = np.max(clusters)
            # print n_clusters      
            # plt.figure()
            # plt.scatter(band_values['doc_id'], band_values['hash_value'], alpha = 0.2)
            # plt.show()
            # 
            # print "SORTED DATAFRAME"
            # bv = band_values.sort(columns = 'hash_value', inplace = False)
            # print bv
        
