# ### https://whoosh.readthedocs.io/en/latest/quickstart.html

from whoosh.qparser import QueryParser
from whoosh.fields import Schema, TEXT, ID

import os.path
from whoosh.index import create_in
from whoosh.index import open_dir

from whoosh.query import *
from whoosh.qparser import QueryParser
from whoosh.filedb.filestore import FileStorage

from whoosh.index import create_in

import pandas as pd


def get_schema():
    return Schema(title=TEXT(stored=True), 
                    url=ID(stored=True), 
                    ingredients=TEXT(stored=True))

def get_index():
    storage = FileStorage("index")
    return storage.open_index()

def create_index(schema):
    if not os.path.exists("index"):
        os.mkdir("index")
    create_in("index", schema)

def add_to_index(index, elements):
    writer = ix.writer()
    for element in elements:
        writer.add_document(title=element["title"], url=element["url"],  ingredients=element["ingredients"])
    writer.commit()



if __name__ == '__main__':

    schema = get_schema()
    # # create_index(schema)
    
    storage = FileStorage("index")
    # # # Using the Storage object
    # # ix = storage.create_index(schema, indexname="usages")
    ix = storage.open_index()

    data = pd.read_csv("../results.csv")
    dd = data.to_dict(orient = 'index')
    # print(dd.values())
    add_to_index(ix, dd.values())
    # for key, item in dd.items():
    #     print(item)
    #     print("\n")
    #     add_to_index(index, item)
