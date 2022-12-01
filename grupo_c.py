from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import json

list_teams_name = list()
list_teams_logo = list()
list_teams_pts = list()

tabla = []

# this is the url of the page we want to scrape 
url = 'https://colombia.as.com/resultados/futbol/mundial/2022/clasificacion/'

# this is the html from the given url
page = requests.get(url)

#this do the convert to Beautiful format. it allow identify the different element from HTML 
soup = BeautifulSoup(page.content, 'html.parser')

#teams from table C
#find_all('element', attribute_=' ') -> find everything, using the indicated parameters
teams_name = soup.find_all('span', class_='nombre-equipo')
teams_pts = soup.find_all('td', class_='destacado')

for teams_x in teams_name:
    if teams_x.text != list_teams_name:
        list_teams_name.append(teams_x.text)

for teams_pts in teams_pts:
    if teams_pts.text != list_teams_name:
        list_teams_pts.append(teams_pts.text)


dt = pd.DataFrame({'name': list_teams_name, 'pts': list_teams_pts})


dt = dt.to_dict('records')
str(dt).encode('utf-8')
data = json.dumps(dt, indent=4, ensure_ascii=False)


print(data) 