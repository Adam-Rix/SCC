# SCC
Swagger Contract Checker - created to verify contracts between back-end and front-end developers using Swagger.

# SCC.py
The main script, needable for executing all your swagger requests.

# conftest.py 
File for operate web_driver: \
1. **main_framework** = Pytest; \
1.1 **default_scope_for_entire_tests** = Session; \
1.2 **default_scope_for_reading_envs** = Function.
2. **sub_fraimwork** = Selenium; \
2.1 **default_browser** = Chrome; \
2.2 **default_argument** = Incognito.

# request_searcher.py
Script for searching any requests on swagger page and building a list with requests and their content body.

# builder.py
The main fabric of all functions

# resources dir
Use that if u have your own .env

# example of output
ASSED [100%]

Total API requests found: 7

POST - /some/api/path
POST - /some/api/path
GET - /some/api/path/{smth}
PUT - /some/api/path/{smth}
DELETE - /some/api/path/{smth}
PUT - /some/api/path
POST - some/api/path

Always is fine

