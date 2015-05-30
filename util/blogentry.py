import sys
import json
import dateutil.parser

class BlogEntry(object):
    """Data class modeling a raw blog entry"""
    def __init__(self, title, date_string, url, raw_text):
        super(BlogEntry, self).__init__()

        self.__title = title
        self.__date = dateutil.parser.parse(date_string)
        self.__url = url
        self.__raw_text = raw_text

    def title(self):
        return self.__title

    def date(self):
        return self.__date

    def url(self):
        return self.__url

    def text(self):
        return self.__text

    @staticmethod
    def from_json_object(json_object):
        title = json_object['title'][0].encode('utf-8', 'replace')
        date_string = json_object['timestamp'][0].encode('utf-8', 'replace')
        raw_text = json_object['raw_content'][0].encode('utf-8', 'replace')
        url = json_object['url'][0].encode('utf-8', 'replace')

        return BlogEntry(title, date_string, "", raw_text)

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

    def __iter__(self):
        for entry in self.__entries:
            yield entry

if __name__ == "__main__":
    collection = BlogEntryCollection.from_json_file(sys.argv[1])
    print collection.size()
    for entry in collection:
        print entry.title()