import string
import numpy as np
import pandas as pd

from blogentry import BlogEntry, BlogEntryCollection
from text_util import TextUtil


class ToLowerCase():

    @staticmethod
    def transform(collection):
        output_collection = list()
        for entry in collection:
            output_collection.append(BlogEntry(TextUtil.to_lower_case(entry.title()), \
            entry.date(), entry.url(), TextUtil.to_lower_case(entry.text()), 
            entry.source, entry.crawl_url))

        return BlogEntryCollection(output_collection)
        
class StripPunctuation():
    
    @staticmethod
    def eliminate_punctuation(in_string):
        return TextUtil.eliminate_punctuation(in_string)
    
    @staticmethod
    def transform(collection):
        output_collection = list()
        for entry in collection:
            output_collection.append(BlogEntry(StripPunctuation.eliminate_punctuation(entry.title()), \
            entry.date(), entry.url(), StripPunctuation.eliminate_punctuation(entry.text()),
            entry.source, entry.crawl_url))
        return BlogEntryCollection(output_collection)
        
        
class DiscardBody():

    @staticmethod
    def transform(collection):
        output_collection = list()
        for entry in collection:
            output_collection.append(BlogEntry(entry.title(), entry.date(), entry.url(), '', entry.source(), entry.crawl_url()))
        return BlogEntryCollection(output_collection)


class RawContentVectorizer():
    
    @staticmethod
    def transform(collection, foodwords_list, neighboring_words = 2):
        collection = ToLowerCase.transform(collection)
        collection = StripPunctuation.transform(collection)
        output_collection = list()
        for entry in collection:
            raw_words =  TextUtil.make_lowercase_word_vector(entry.text()) #, unique = False, stemming = True
            tot_words = len(raw_words)
            index = neighboring_words
            raw_content_words_list = list()
            while index <= (tot_words - neighboring_words):
                if TextUtil.list_contains(raw_words[index], foodwords_list):
                    sub_sentence = raw_words[(index-neighboring_words):(index+neighboring_words+1)]
                    
                    for word in sub_sentence:
                        raw_content_words_list.append(word)
                    
                    index += neighboring_words
                else:
                    index += 1
            
            output_collection.append(BlogEntry(entry.title(), entry.date(), entry.url(), set(raw_content_words_list)))
        return output_collection
        
         
        
# if __name__ == '__main__':
#     collection = BlogEntryCollection.from_json_file(sys.argv[1])
#     print collection.size()
    
