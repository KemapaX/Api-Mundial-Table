import requests
from bs4 import BeautifulSoup

class ScrapingTableInformation:
    def __init__(self):
        self.list_teams_name = list()
        self.list_teams_logo = list()
        self.list_teams_pts = list()

        self.tabla = []
        
    
    def pages(self, url):
        # this is the html from the given url
        page = requests.request("GET", url)

        # this do the convert to Beautiful format. it allow identify the different element from HTML    
        soup = BeautifulSoup(page.content, 'html.parser')

        # find_all('element', attribute_=' ') -> find everything, using the indicated parameters
        teams_name = soup.find_all('span', class_='nombre-equipo')
        teams_pts = soup.find_all('td', class_='destacado')

        # add information to list
        data_name=self.add_information(teams_name)
        data_pts=self.add_information(teams_pts)

        # add information to table
        tabla=self.add_table(data_name, data_pts)

        return tabla


    # this need a parameter fot it can add information to list
    def add_information(self, data):
        list_teams = list()
        for teams_x in data:
            if teams_x.text != list_teams:
                list_teams.append(teams_x.text)
        return list_teams
    
    # this need two parameters for it can add information to table of teams and resulted
    def add_table(self, data_a, data_b):
        list_teams = list()
        n = 0
        for i in data_a:
            n+=1
            list_teams.append(
                {'id': n, 'name': i, 'pts': data_b[data_a.index(i)]})
        return list_teams


