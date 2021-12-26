class Bill:
    """
    Objetos that contains data about a bill, such as
    total amount and peoriod of the bill
    """
    def __init__(self,amount, period):
        self.amount = amount
        self.period = period

class Flatmate:
    """
    Data of flatmates, such as names, pay ,etc
    """
    def __init__(self,day_in_house, name):
        self.day_in_house = day_in_house
        self.name = name

    def pays(self,bill, Flatmate):
        return (bill.amount/(self.day_in_house + Flatmate.day_in_house)) *self.day_in_house