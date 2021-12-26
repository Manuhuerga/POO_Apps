from selectorlib import Extractor
import requests

class Temperature:

    headers = {
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            }
    
    url = 'https://www.timeanddate.com/weather/'
    
    def __init__(self,country,city):
        self.country = country.replace(' ', '-')
        self.city = city.replace(' ','-')

    def scrap(self):
        extractor = Extractor.from_yaml_file('temperature.yaml')
        r = requests.get(self.url_build() ,headers=self.headers)
        c = r.text
        extract = extractor.extract(c)
        return extract

    def get(self):
        scrap_content = self.scrap()
        return (float(scrap_content[temp]).replace('C', '').strip())

    def url_build(self):
        return self.url + self.country + '/' + self.city

if __name__ == '__main__':
    t = Temperature('argentina','buenos aires')
