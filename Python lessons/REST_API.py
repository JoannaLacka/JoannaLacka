# pobieranie danych
# pip install requests

import requests
# import json

def get_json_data():
    parameters = "per_page=3"
    response = requests.get("https://www.pikademia.pl/wp-json/wp/v2/posts", parameters)
    # response = requests.get("https://www.pikademia.pl/wp-json/wp/v2/posts?per_page=3")
    #  print(response.status_code)
    # content = response.content
    # articles = json.loads(content)
    articles = response.json()
    # print(type(articles))
    for article in articles:
        print(article["title"]["rendered"])

get_json_data()
