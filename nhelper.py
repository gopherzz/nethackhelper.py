import os
import requests
from bs4 import BeautifulSoup

class nhelper:
    def __init__(self):
        while(True):
            try:
                search = self.get_inp('Search: ')
                os.system('cls||clear')
                if search == 'Quit' or search == 'Q':
                    exit()
                else:
                    URL = 'https://nethackwiki.com/wiki/%s' % (search)
                    site = self.get_html(URL)

                    status = self.get_status(site)
                    short_status = self.get_short_status(status)
        
                    self.out_stat(short_status)

            except AttributeError:
                print("Oops, silly, you materialize ERROR... Try Again!!")
                continue


    def get_inp(self, text):
        search = input(text)
        search = search.capitalize()
        search = search.replace(' ', '_')
        
        return search

    def get_html(self, URL):
        return requests.get(URL).text

    def get_status(self, site):
        soup = BeautifulSoup(site, features="lxml")
        status = soup.find('div', {'class': 'monsterfull'})
        
        return status
    
    def get_short_status(self, status):
        status_trs = status.find_all('tr')
        short_status = status_trs[-3]
        
        return short_status
    
    def out_stat(self, short_status):
        print(short_status.text.replace('\n', '').replace(': ', '\n').replace('. ', '\n'))    

if __name__ == '__main__':
    nhelper()
