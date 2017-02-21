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

from data_importer import collection_to_dataframe
from group_by import group_by
from featurizer import Featurizer

import sys
sys.path.append('/Users/celi/Desktop/FoodMath/hangry-goat.git/util/')
from blogentry import BlogEntry, BlogEntryCollection


if __name__ == '__main__':
    collection = BlogEntryCollection.from_json_file(sys.argv[1])
    print collection.size()
    data = collection_to_dataframe(collection)
    grouped_data = group_by(data, 'year', 'month')
    featurizer = Featurizer(grouped_data)

    featurizer.word_count('orange', column = 'raw_content', exact_match = False)
    print featurizer.feature_matrix
