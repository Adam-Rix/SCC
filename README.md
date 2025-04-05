# SCC
Swagger Contract Checker - created to verify contracts between back-end and front-end developers using Swagger.

# SCC.py
The main script, needable for executing all your swagger requests.

# conftest.py 
File for operate web_driver: 

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
PASSED [100%]

~Requests found: 

~Total API requests found: 7

POST - /some/api/path \
POST - /some/api/path \
GET - /some/api/path/{smth} \
PUT - /some/api/path/{smth} \
DELETE - /some/api/path/{smth} \
PUT - /some/api/path \
POST - /some/api/path 

Always is fine

~~Total examples of body requests found: 5

{ \
  &emsp; "somId": "123", \
  &emsp; "smthelse": "123" \
},

~~Total examples of body responses found: 3

{ \
  "someCats": { \
    "111": "23213", \
    "444": "3213" \
},

# plans
1. Improve request_searcher.py for: \
1.1 Collecting bodies of each request; ✅\
1.2 Collecting examples of each response; ✅\
1.3 Replacing non-json responses by response-codes (200, 300, etc.) from examples of responses;
2. Create a script for work with collections of requests from swagger; \
2.1 Write a script for sending requests with api paths from 2 arrays; \
2.2 Improve the script for correlating the response from server with expected; 
3. Update outputs for better understanding;
4. Finalize the epic.