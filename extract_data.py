import json
from urllib import request
from bs4 import BeautifulSoup


def buildJData(js, filename):
    """
    build json file from the data & filer unnecessary data
    :param js: dict represent data about the demanded categories (pizza, drinks, dessert)
    :param filename: new json file name
    :return: ""
    """
    with open(filename, 'w') as f:
        data = js['dishList']
        for item in data:
            del item['categoryID']
            del item['choices']
            del item['dishImageUrl']
            del item['isPopularDish']
            del item['dishPopularityScore']
            del item['enableComment']
        json.dump(data, f, indent=4)


def extractData():
    """
    extract data from the url and build js files
    :return:
    """
    url = 'https://www.10bis.co.il/NextApi/GetRestaurantMenu?' \
          'culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup'
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    site_json = json.loads(soup.text)
    for x in site_json["Data"]["categoriesList"]:
        if x['categoryName'] == 'Pizzas':
            buildJData(x, 'pizzas_data.json')
        if x['categoryName'] == 'Drinks':
            buildJData(x, 'drinks_data.json')
        if x['categoryName'] == 'Desserts':
            buildJData(x, 'desserts_data.json')
