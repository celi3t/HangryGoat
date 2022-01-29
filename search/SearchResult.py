class SearchResult():
    def __init__(self, res, search_type):
        # self.author = res["author"]
        self.url = res["url"]
        self.title = res["title"]
        self.title_score = 0
        self.ingredient_score = 0
    
    def set_ingredient_score(self, score):
        self.ingredient_score = score

    def set_title_score(self, score):
        self.title_score = score

    def get_score(self):
        return self.title_score * 0.7 + self.ingredient_score * 0.3

    #### TODO:
    ## Implement SearchResult equality
    





# # qp = QueryParser("content", schema=myindex.schema)
# # q = qp.parse(u"hello world")

# # with myindex.searcher() as s:
# #     results = s.search(q)