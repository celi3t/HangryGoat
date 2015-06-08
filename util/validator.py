#!/usr/bin/env python

import sys
import re
import blogentry as be
from sets import Set

class Validator(object):
    """Validates JSON data"""
    def __init__(self, input_json_paths=[], entry_predicates=[], collection_predicates=[]):
        super(Validator, self).__init__()
        self._input_json_paths = input_json_paths
        self._collections = dict()
        for path in self._input_json_paths:
            collection = be.BlogEntryCollection.from_json_file(path)
            self._collections[path] = collection

        for entry_predicate in entry_predicates:
            self.evaluate_blog_entry_predicate(entry_predicate)

        for collection_predicate in collection_predicates:
            self.evaluate_collection_predicate(collection_predicate)

    def evaluate_blog_entry_predicate(self, predicate):
        errors = dict()
        error_items = dict()
        for path, collection in self._collections.iteritems():
            file_errors = 0
            file_error_items = []
            for entry in collection:
                if(not predicate.evaluate(entry)):
                    file_errors += 1
                    file_error_items.append(entry)
            errors[path] = file_errors
            error_items[path] = file_error_items

        print "*** Entry predicate " + predicate.describe() + " failures:"
        total_errors = 0;
        for path, collection in self._collections.iteritems():
            print path + " => " + str(errors[path]) + "/" + str(collection.size())
            total_errors += errors[path]
        print "Total: " + str(total_errors)
        print "\n"

    def evaluate_collection_predicate(self, predicate):
        print "*** Collection predicate " + predicate.describe() + ":"
        for path, collection in self._collections.iteritems():
            if(predicate.evaluate(collection)):
                print "PASS: " + path
            else:
                print "FAIL: " + path

class FieldNotEmptyPredicate(object):
    def __init__(self, field_name):
        super(FieldNotEmptyPredicate, self).__init__()
        self._field_name = field_name

    def describe(self):
        return "FieldNotEmptyPredicate(" + self._field_name + ")"

    def evaluate(self, entry):
        field_value = getattr(entry, self._field_name)()
        if field_value:
            return True
        else:
            return False

class MatchesRegexPredicate(object):
    def __init__(self, regex, field_name):
        super(MatchesRegexPredicate, self).__init__()
        self._regex = regex
        self._field_name = field_name

    def describe(self):
        return "MatchesRegexPredicate(\"" + str(self._regex.pattern) + "\", " + self._field_name + ")"

    def evaluate(self, entry):
        field_value = getattr(entry, self._field_name)()
        if re.search(htmlTagRegex, field_value) != None:
            return False
        return True

class DuplicateFreePredicate(object):
    def __init__(self, field_name):
        super(DuplicateFreePredicate, self).__init__()
        self._field_name = field_name

    def describe(self):
        return "DuplicateFreePredicate(" + self._field_name + ")"

    def evaluate(self, collection):
        set = Set();
        for entry in collection:
            field_value = getattr(entry, self._field_name)()
            set.add(field_value)
        return collection.size() == len(set)

if __name__ == "__main__":

    input_files = sys.argv[1:]
    entry_predicates = []
    collection_predicates = []

    entry_predicates.append(FieldNotEmptyPredicate("title"))
    entry_predicates.append(FieldNotEmptyPredicate("text"))
    htmlTagRegex = re.compile("<[a-zA-Z]+>", re.IGNORECASE | re.MULTILINE)
    entry_predicates.append(MatchesRegexPredicate(htmlTagRegex, "title"))
    entry_predicates.append(MatchesRegexPredicate(htmlTagRegex, "text"))

    collection_predicates.append(DuplicateFreePredicate("crawl_url"))

    v = Validator(input_files, entry_predicates, collection_predicates)
