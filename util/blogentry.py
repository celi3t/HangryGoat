import sys
import json
from dateutil.parser import parse
from datetime import datetime
import pandas as pd

from text_util import TextUtil

class BlogEntry(object):
    """Data class modeling a raw blog entry"""
    def __init__(self, title, date, url, raw_text, source, crawl_url):
        super(BlogEntry, self).__init__()

        self.__title = title
        if isinstance(date, datetime):
            self.__date = date
        else:
            self.__date = parse(date)
        self.__url = url
        self.__raw_text = raw_text
        self.__source = source
        self.__crawl_url = crawl_url

    def title(self):
        return self.__title

    def date(self):
        return self.__date

    def url(self):
        return self.__url

    def text(self):
        return self.__raw_text

    def source(self):
        return self.__source

    def crawl_url(self):
        return self.__crawl_url

    @staticmethod
    def from_json_object(json_object):
        title = TextUtil.unpack_list(json_object['title'])
        date_string = TextUtil.unpack_list(json_object['timestamp'])
        raw_text = TextUtil.unpack_list(json_object['raw_content'])
        url = TextUtil.unpack_list(json_object['url'])
        source = TextUtil.to_utf8(json_object['source'])
        crawl_url = TextUtil.to_utf8(json_object['crawl_url'])

        return BlogEntry(title, date_string, url, raw_text, source, crawl_url)

class BlogEntryCollection(object):
    """Data class modeling a collection of BlogEntry elements"""
    def __init__(self, entries):
        super(BlogEntryCollection, self).__init__()
        self.__entries = entries

    @staticmethod
    def from_json_file(file_path):
        json_object = json.load(open(file_path))
        return BlogEntryCollection.from_json_object(json_object)

    @staticmethod
    def from_json_object(json_collection):
        entries = []
        for json_entry in json_collection:
            try:
                entry = BlogEntry.from_json_object(json_entry)
                entries.append(entry)
            except IndexError:
                print "Failed to create an entry from JSON"

        blog_entry_collection = BlogEntryCollection(entries)
        errors = len(json_collection) - blog_entry_collection.size()

        print "Parsed " + str(blog_entry_collection.size()) + " with " + str(errors) + " errors"
        return blog_entry_collection

    def size(self):
        return len(self.__entries)
        
    def to_dataframe(self):
        data = {}
        data['title'] = list()
        data['timestamp'] = list()
        data['url'] = list()
        data['raw_content'] = list()
        for entry in self:
            data['title'].append(entry.title())
            data['timestamp'].append(entry.date())
            data['url'].append(entry.url())
            data['raw_content'].append(entry.text())

        data = pd.DataFrame.from_dict(data)
        data['year'] = data['timestamp'].dt.year
        data['month'] = data['timestamp'].dt.month 
        data['week'] = data['timestamp'].dt.week
        return data

    def __iter__(self):
        for entry in self.__entries:
            yield entry

if __name__ == "__main__":
    collection = BlogEntryCollection.from_json_file(sys.argv[1])
    print collection.size()
    for entry in collection:
        print entry.title()
    print collection.to_dataframe()
