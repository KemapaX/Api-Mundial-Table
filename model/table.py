import requests
from bs4 import BeautifulSoup

class ScrapingTableInformation:
    def __init__(self):
        self.tabla = []
        
    
    def pages(self, *args):
        # this is the html from the given url
        page_as = requests.request("GET", args[0])
        
        # this do the convert to Beautiful format. it allow identify the different element from HTML    
        soup_as = BeautifulSoup(page_as.content, 'html.parser')

        # find_all('element', attribute_=' ') -> find everything, using the indicated parameters
        teams_name = soup_as.find_all('span', class_='nombre-equipo')
        teams_pts = soup_as.find_all('td', class_='destacado')
        teams_pj = soup_as.find_all('td', class_='')
        teams_logo = soup_as.find_all('th', class_='cont-nombre-equipo')
        
        """ for the table of teams lack | GF GC DG | 
        
        For the next update, improve the logic of all the functions
        
        """
        

        # add information to list
        data_name=self.add_information(teams_name)
        data_pts=self.add_information(teams_pts)
        data_pj=self.add_information(teams_pj)
        data_logo=self.add_information_img(teams_logo, 'image')
        
        # add information to table
        tabla=self.add_table(data_name, data_pts, data_pj, data_logo)
        
        return tabla


    # this need a parameter fot it can add information to list
    def add_information(self, data):
        list_teams = list()
        for teams_x in data:
            if teams_x.text != list_teams:
                list_teams.append(teams_x.text)
        return list_teams
    
    
    # this function give img of the teams
    def add_information_img(self, data, attribute):
        list_teams = list()
        for teams_x in data:
            logo = teams_x.find('img', itemprop=attribute).get('data-src')
            
            list_teams.append(logo)
        return list_teams
    
    
    # this need two parameters for it can add information to table of teams and resulted
    def add_table(self, *args):
        list_teams = list()
        n = 0; p = 0
        
        for i in args[0]:
            n+=1
            list_teams.append(
                {'id': n, 'name': i, 'PTJ': args[1][args[0].index(i)], 'PJ': args[2][p],
                'PG': args[2][p+1], 'PE': args[2][p+2], 'PP': args[2][p+3], 'img_logo': args[3][n-1]})
            p+=4
        
        return list_teams


