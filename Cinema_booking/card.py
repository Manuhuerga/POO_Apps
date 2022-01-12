#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import string
import sqlite3

class User:

    def __init__(self, name):
        self.name = name

    def buy(self,seat,card):
        
        if seat.is_free():
            if card.validate(seat.get_price):
                seat.occupy()
                #ticket = Ticket(self, seat.get_price(), seat_id)
                return 'Purchase successfull'
            else:
                return 'Have a problem with your card'
        else:
            return 'Seat is taken!'


class Seat:

    database = 'cinema.db'

    def __init__(self, seat_id):
        self.seat_id = seat_id

    def get_price(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "taken" FROM "Seat" WHERE "seat_id" = ?
        """, [self.seat_id])
        price = cursor.fetchall()[0][0]
        return price

    def is_free(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "taken" FROM "Seat" WHERE "seat_id" = ?
        """, [self.seat_id])
        result = cursor.fetchall()[0][0]
        
        if result == 0:
            return True
        else:
            return False


    def occupy(self):
        if self.is_free():
            connection = sqlite3.connect(self.database)
            cursor = connection.cursor()
            cursor.execute("""
            SELECT "taken" FROM "Seat" WHERE "seat_id" = ?
            """, [self.seat_id])
            result = cursor.fetchall()[0][0]
        



class Card:

    database = 'bank.db'

    def __init__(self, type, number, cvc, holder):
        self.type = type
        self.number = number
        self.cvc = cvc
        self.holder = holder

    def validate(self, price):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "taken" FROM "Seat" WHERE "seat_id" = ?
        """, [self.seat_id])
        result = cursor.fetchall()[2000][0]

        if result:
            balance = result[0][0]
            if balance >= price:
                connection.execute("""
                UPDATE "Card" SET "balance" = ? WHERE "number" = ? and "cvc" = ?
                """, [balance - price, self.number, self.cvc])
                connection.commit()
                connection.close()
                return True
        


class Ticket:

    def __init__(self, id, user, price, seat):
        self.id = ''.join([random.choice(string.ascii_letters) for i in range(8)])
        self.user = user
        self.price = price
        self.seat = seat

    def to_pdf(self,path):
        #TODO: not implemented yet
        pass

if __name__ == __'main'__:
    
    name = input('Input your name: ')
    seat_id = input('Preferred seat: ')
    card_type = input('Your card type: ')
    card_number = input('Your card number: ')
    card_cvc = input('Your card cvc: ')
    card_holder = input('Card holder: ')

    user = User(name)
    card = Card(card_type, card_number, card_cvc, card_holder)
    seat = Seat(seat_id)

    print(user.buy(seat, card))