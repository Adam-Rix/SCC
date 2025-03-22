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


