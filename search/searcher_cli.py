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

from indexer import get_schema
from indexer import get_index



if __name__ == '__main__':
    schema = get_schema()
    ix = get_index()

    import questionary
    
    q = questionary.select(
    "Search for:",
    choices=["Title", "Ingredients", "Tags"]).ask()

    if q == "Title":
        parser = QueryParser("title", ix.schema)
    elif q == "Ingredients":
        parser = QueryParser("ingredients", ix.schema)
    elif q == "tags":
        parser = QueryParser("tags", ix.schema)
    else:
        print("Sorry, this search option has not been implemented yet - stay tuned!")

    
    # authors = questionary.checkbox("Select specific authors?", choices=[
    #    "All Authors",
    #    "Smitten Kitchen",
    #    "Joy The Baker"]).ask()
    
    query = questionary.text("Search: ").ask()
    myquery = parser.parse(query)
    
    print("searching for:")
    print(myquery)
    # print("for authors:")
    # print(authors)
    # print("\n")

    #NEEDS TO BE EXACT
    # allow_q = Term("url", "https://smittenkitchen.com/2021/12/short-rib-onion-soup/")
    # # Don't show any documents where the "tag" field contains "todo"
    # restrict_q = query.Term("tag", "todo")

    with ix.searcher() as s:
        results = s.search(myquery, terms = True, limit = 20)  #filter=allow_q, mask=restrict_q
        print("Found " + str(len(results)) + "results")
        print(results.scored_length())
        for i, r in enumerate(results):
            print("result found: " + str(i))
            print(r["title"])
            print(r["url"])
            print("\n")






# # qp = QueryParser("content", schema=myindex.schema)
# # q = qp.parse(u"hello world")

# # with myindex.searcher() as s:
# #     results = s.search(q)