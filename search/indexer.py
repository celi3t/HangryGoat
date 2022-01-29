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
                    tags=TEXT(stored=True), 
                    url=ID(stored=True), 
                    author=ID(stored=True), 
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
        writer.add_document(title=element["title"], url=element["url"],  ingredients=element["ingredients"],
        author=element["author"],  tags=element["tags"])
    writer.commit()


def reset_index():
    schema = get_schema()
    create_index(schema)


def index_dict(dictionary):    
    storage = FileStorage("index")
    ix = storage.open_index()
    add_to_index(ix, [dictionary])




if __name__ == '__main__':
    # reset_index()
    to_index = "../data/parsed/iamafoodblog.csv"
    #"../data/parsed/smitten_kitchen.csv"
    
    schema = get_schema()
    storage = FileStorage("index")
    ix = storage.open_index()

    data = pd.read_csv(to_index)
    dd = data.to_dict(orient = 'index')
    add_to_index(ix, dd.values())
