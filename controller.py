from flask import jsonify
from model.table import ScrapingTableInformation


def show():
    # this is the url of the page we want to scrape
    url = 'https://colombia.as.com/resultados/futbol/mundial/2022/clasificacion/'

    # tell the object to get the url
    data = ScrapingTableInformation().pages(url)

    return jsonify({"records": data, 'result': len(data)})