import numpy as np
import pandas as pd

from string_utils import check_contains, check_contains_howmany


class Featurizer(object):
    def __init__(self, data):
        self.data = data
        keys = list()
        for k, v in data:
            keys.append(k)
        self.feature_matrix = pd.DataFrame(index = keys)
        self.nrows = len(keys)
        
    def word_count(self, keyword, column = 'title', exact_match = False):
        feat_vector = np.zeros(self.nrows)
        for i, (key, values) in enumerate(self.data):
            v = pd.Series(values[column])
            # print v
            # print v.apply(check_contains_howmany, args=[keyword, exact_match]).sum()
            # print v.apply(check_contains_howmany, args=[keyword, exact_match]).sum()
            # lsg
            # ndf = v[v.apply(check_contains_howmany, args=[keyword, exact_match])].count()  
            feat_vector[i] = v.apply(check_contains_howmany, args=[keyword, exact_match]).sum()
        self.feature_matrix[keyword + '_wordcount'] = feat_vector 
        
        
    def word_appears(self, keyword, column = 'title', exact_match = False):
        feat_vector = np.zeros(self.nrows)
        for i, (key, values) in enumerate(self.data):
            v = pd.Series(values[column])
            ndf = v[v.apply(check_contains, args=[keyword, exact_match])].count()  
            feat_vector[i] = ndf
        self.feature_matrix[keyword + '_wordcount'] = feat_vector
