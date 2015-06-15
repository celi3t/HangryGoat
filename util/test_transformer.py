import unittest
from transformer import *
from datetime import datetime

from blogentry import BlogEntry, BlogEntryCollection
from text_util import TextUtil

class TestTransformer(unittest.TestCase):
    
    def test_transform(self):
        date = datetime.now()
        b = BlogEntry("title", date, "url", "raw_text", "source", "crawl_url")
        collection = BlogEntryCollection([b])
        collection1 = DiscardBody.transform(collection)
        collection1 = ToLowerCase.transform(collection1)
        collection1 = StripPunctuation.transform(collection1)
        transformed_entry = collection1[0]
        expected_entry = BlogEntry("title", date, "url",  "", "source", "crawl_url")
        self.assertEquals(expected_entry.title() , transformed_entry.title())
        self.assertEquals(expected_entry.date() , transformed_entry.date())
        self.assertEquals(expected_entry.url() , transformed_entry.url())


