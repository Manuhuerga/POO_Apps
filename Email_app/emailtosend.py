import yagmail
import pandas
from emailgetter import NewsFeed
from datetime import date, datetime
from time import sleep

def send_email(date_from_today, date_from_last_month, row):
    news_feed = NewsFeed(interest=row['interest'],from_data = date_from_last_month, to_data= date_from_today)

    email = yagmail.SMTP('pythontestemails2021@gmail.com','PythonTesting123')
    email.send(row['email'], 
                subject = 'Your {} news for today!'.format(row['interest'].capitalize()),
                contents = 'Hi {}\n See about {}:\n{}'.format(row['name'],row['interest'].capitalize(),news_feed.get()),
                attachments = 'design.txt')

while True:
    if datetime.now().hour == 13 and datetime.now().minute == 15:
        today = date.today()
        date_from_today = str(today.year) + '-' + str(today.month) + '-' + str(today.day)
        date_from_last_month = str(today.year) + '-' + str(today.month-1) + '-' + str(today.day)

        df = pandas.read_excel('people.xlsx')

        for index,row in df.iterrows():
            send_email(date_from_today, date_from_last_month, row)
    
    #sleep(60)