from flat import Flatmate, Bill
from pdf import PdfReport

#Input a values of object bill such as total or period
bill = Bill(float(input('Please, input amount of the bill: ')), str(input('Whats is the period?(for ex. December): ')))
print (bill.amount,bill.period)

#Get a values such as a days in house or yours name
Guille = Flatmate(int(input("How many days Guille on the flat: ")), 'Guille')
Manu  = Flatmate(int(input("How many days Manu on the flat: ")), 'Manu')


print('{} should be pay {:.2f}$' .format(Manu.name, Manu.pays(bill,Guille)))
print('{} should be pay {:.2f}$' .format(Guille.name, Guille.pays(bill,Manu)))

pdf = PdfReport('Report1.pdf')
pdf.generate(Guille,Manu,bill)