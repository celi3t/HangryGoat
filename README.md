After 6 years, I am resurrecting this unfinished project like it's 2022 and my idea app for organizing recipes does not exist yet!

#### What is this project - current features

HangryGoat is a CLI tool to search for recipes only among my favorite foodblogs.
You can search by:
- title
- ingredients
- tags


#### How to run it
`python3 search/searcher_cli.py`

#### MVP status report
- Set up project in Docker --OK
- Daily Airflow report (mock to start) to slack 
- Crawler for links --OK, kinda
- Parser for recipe text, ingredients, tags (raw)  --OK, should add more parsers
- Clean text, ingredients
- Simple SQLite storage - First iteration of schemas
- Search ranking first iteration  --OK, can use some refactoring
- Webapp / Notebook ok to start

#### Future work

NLP fun: 
- Improve the search by ingredients 
- Create derived tags

Webapp with GUI for search
- Collect telemetry for personalization
- Move to Streamlit

Deploy on `The Dusty` with Heroku
- Set up actual monitoring

