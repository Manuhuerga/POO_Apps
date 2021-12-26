from flat import Flatmate, Bill
#from pdf import PdfReport

#Input a values of object bill such as total or period
bill = Bill(float(input('Please, input amount of the bill: ')), str(input('Whats is the period?(for ex. December): ')))
print (bill.amount,bill.period)

#Get a values such as a days in house or yours name
flatmate1 = str(input('Name of flatmate 1: '))
flatmate2 = str(input('Name of flatmate 2: '))

flatmate_1 = Flatmate(int(input(f"How many days {flatmate1} on the flat: ")), flatmate1)
flatmate_2 = Flatmate(int(input(f"How many days {flatmate2} on the flat: ")), flatmate2)


print('{} should be pay {:.2f}$' .format(flatmate_1.name, flatmate_1.pays(bill,flatmate_2)))
print('{} should be pay {:.2f}$' .format(flatmate_2.name, flatmate_2.pays(bill,flatmate_1)))

#pdf = PdfReport('Report1.pdf')
#pdf.generate(Guille,Manu,bill)