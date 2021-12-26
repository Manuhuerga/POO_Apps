#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Api Key is bb94cbc9f44544079ac6787fc4413211
import requests
from pprint import pprint

class ExcelFile:
    
    def __init__(self, filename):
        #TODO no implemented yet
        self.filename = filename
    
    def get_data(self):
        pass

class Email:

    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body

    def send(self):
        pass

class NewsFeed:
    
    def __init__(self,interest: str ,from_data :str, to_data:str) -> str:
        self.interest = interest
        self.from_data = from_data
        self.to_data = to_data

    def get(self):
        url = self.build_url()
        r = requests.get(url)
        content = r.json()
        articles = content['articles']
        
        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"
        
        return email_body 

    def build_url(self):
        interest = 'qinTitle=' + self.interest + '&'
        from_data = 'from=' + self.from_data +'&'
        to_data = 'to=' + self.to_data +'&'
        url = 'https://newsapi.org/v2/everything?' + interest + from_data + to_data + \
                        'sortBy=publishedAt&'\
                        'apiKey=bb94cbc9f44544079ac6787fc4413211'
                        
        return url  


if __name__ == '__main__':
    feed = NewsFeed('Tesla', '2021-12-12', '2021-12-19')
    pprint(feed.get())


#pprint(content)