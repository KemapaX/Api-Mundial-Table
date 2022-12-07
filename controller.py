from flask import jsonify
from model.table import ScrapingTableInformation


def show(password):
    if password == 'ae@1234':
        # this is the url of the page we want to scrape
        url_as = 'https://colombia.as.com/resultados/futbol/mundial/2022/clasificacion/'

        # tell the object to get the url
        data = ScrapingTableInformation().pages(url_as)

        return jsonify({"records": data, 'result': len(data)})
    else:
        return jsonify({'messege': 'Password incorrect'})