import numpy as np
import pandas as pd

#from datetime import datetime
import matplotlib.pyplot as plt
import json
from dateutil.parser import parse
from datetime import date
import re

import sys
sys.path.append('/Users/celi/Desktop/FoodMath/hangry-goat.git/util/')
from blogentry import BlogEntry, BlogEntryCollection

def collection_to_dataframe(collection):
    data = {}
    data['title'] = list()
    data['timestamp'] = list()
    data['url'] = list()
    data['raw_content'] = list()
    
    for entry in collection:
        data['title'].append(entry.title())
        data['timestamp'].append(entry.date())
        data['url'].append(entry.url())
        data['raw_content'].append(entry.text())
        
    data = pd.DataFrame.from_dict(data)
    data['year'] = data['timestamp'].dt.year
    data['month'] = data['timestamp'].dt.month 
    data['week'] = data['timestamp'].dt.week
    #print data
    return data




# def raw_to_dataframe(filepath):
#     data = {}
#     data['title'] = list()
#     data['timestamp'] = list()
#     data['url'] = list()
#     other_fields = list()
#     for element in json.load(open(filepath)):
#         if not len(element['title']) == 0 and not len(element['timestamp']) == 0:  
#             for field in element.keys():
#                 if field not in data:
#                     data[field] = list()
#                     other_fields.append(field)
#                     
#             
#             title = str(element['title'][0].encode('utf-8', 'replace').lower()).split()
#             datestring =  parse(element['timestamp'][0])
#             url = element['url'][0].split('/')[2]
#             
#             data['title'].append(title)
#             data['timestamp'].append(datestring)
#             data['url'].append(url)
#             for field in other_fields:
#                 print field
#                 print element[field]
#                 if len(element[field]) > 0:
#                     data[field].append(element[field][0].encode('utf-8', 'replace').lower().split())
#                 else:
#                     data[field].append(None)
#             
#             
#     data = pd.DataFrame.from_dict(data)
#     data['year'] = data['timestamp'].dt.year
#     data['month'] = data['timestamp'].dt.month 
#     data['week'] = data['timestamp'].dt.week
#     return data
# 



if __name__ == '__main__':
    collection = BlogEntryCollection.from_json_file(sys.argv[1])
    print collection.size()
    collection_to_dataframe(collection)
    
    # jtb_path = '/Users/celi/Desktop/FoodMath/hangry-goat.git/scrapy/hangrygoat/analysis/items.json'
    # example_df = raw_to_dataframe(jtb_path)
    # print example_df['week']