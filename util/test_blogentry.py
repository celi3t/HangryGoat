import unittest
import json
from datetime import datetime
from blogentry import BlogEntry, BlogEntryCollection

class TestBlogEntry(unittest.TestCase):

    def test_construct_with_nones(self):
        date = datetime.now()
        b = BlogEntry(None, date, None, None, None, None)
        self.assertEqual(b.title(), None)
        self.assertEqual(b.date(), date)
        self.assertEqual(b.url(), None)
        self.assertEqual(b.text(), None)
        self.assertEqual(b.source(), None)
        self.assertEqual(b.crawl_url(), None)

    def test_construct_with_invalid_date(self):
        error = False
        not_a_valid_date = "not a valid date"
        try:
            b = BlogEntry(None, not_a_valid_date, None, None, None, None)
        except ValueError:
            error = True
        self.assertTrue(error)

    def test_construct_with_date(self):
        date = datetime.now()
        b = BlogEntry("title", date, "url", "raw_text", "source", "crawl_url")
        self.assertEqual(b.title(), "title")
        self.assertEqual(b.date(), date)
        self.assertEqual(b.url(), "url")
        self.assertEqual(b.text(), "raw_text")
        self.assertEqual(b.source(), "source")
        self.assertEqual(b.crawl_url(), "crawl_url")

    def test_construct_with_datestring(self):
        date = datetime.now()
        date_string = str(date)
        b = BlogEntry("title", date_string, "url", "raw_text", "source", "crawl_url")
        self.assertEqual(b.title(), "title")
        self.assertEqual(b.date(), date)
        self.assertEqual(b.url(), "url")
        self.assertEqual(b.text(), "raw_text")
        self.assertEqual(b.source(), "source")
        self.assertEqual(b.crawl_url(), "crawl_url")

    def test_load_from_json(self):
        date = datetime.now()
        date_string = str(date)
        json_string = '\
            { \
                "title": ["title"], \
                "url": ["url"], \
                "timestamp": ["' + date_string + '"], \
                "raw_content": ["raw", "text"], \
                "source": "source", \
                "crawl_url": "crawl_url"\
            }'
        json_object = json.loads(json_string)
        b = BlogEntry.from_json_object(json_object)
        self.assertEqual(b.title(), "title,")
        self.assertEqual(b.date(), date)
        self.assertEqual(b.url(), "url,")
        self.assertEqual(b.text(), "raw,text,")
        self.assertEqual(b.source(), "source")
        self.assertEqual(b.crawl_url(), "crawl_url")

class TestBlogEntryCollection(unittest.TestCase):
    blog_entry_1 = BlogEntry("title", datetime.now(), "url", "raw_text", "source", "crawl_url")
    blog_entry_2 = BlogEntry("title", datetime.now(), "url", "raw_text", "source", "crawl_url")

    def test_invalid_entries(self):
        error = False
        try:
            BlogEntryCollection(TestBlogEntryCollection.blog_entry_1)
        except ValueError:
            error = True
        self.assertTrue(error)

    def test_construct(self):
        entries = [TestBlogEntryCollection.blog_entry_1, TestBlogEntryCollection.blog_entry_2]
        bc = BlogEntryCollection(entries)
        self.assertEquals(2, bc.size())
        for entry in bc:
            self.assertIn(entry, entries)
        for entry in entries:
            self.assertIn(entry, bc)

    def test_load_from_json(self):
        date = datetime.now()
        date_string = str(date)
        json_entry_string = '\
            { \
                "title": ["title"], \
                "url": ["url"], \
                "timestamp": ["' + date_string + '"], \
                "raw_content": ["raw", "text"], \
                "source": "source", \
                "crawl_url": "crawl_url"\
            }'
        json_collection_string = '[' + json_entry_string + ', ' + json_entry_string + ']'
        json_object = json.loads(json_collection_string)
        bc = BlogEntryCollection.from_json_object(json_object)
        self.assertEquals(2, bc.size())
