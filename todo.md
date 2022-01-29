
## To Do List

### Done:
- parse list of urls into a pandas dataframe
- index recipes with title, ingredients, tags, author, url
- cli search tool
- crawler class and rules class to apply different rules when crawling for recipe urls
- Search with filters (e.g. search "chicken" in ingredients where author = XYZ)
- improve search by ingredients

### Data stuff
- more parsers
- data cleaning everywhere
- finalize db schema

### Search stuff
- "postprocessing" of search results, recalculating a final search score based on whether a recipe popped up as result by title search, ingredient search, or tag search
- implement search by tag (don't have tags finalized at the moment)

### Integrations
- ADD button for new recipe from slack
- automate crawlers (maybe?)

### WebApp stuff 
- Create a GUI for search
- Display search results with hero image

### NLP stuff
- if recipe block is not available, get recipe from raw text
- implement tags
