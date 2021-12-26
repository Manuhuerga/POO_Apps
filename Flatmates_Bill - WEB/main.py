from flask.globals import request
from flask.views import MethodView
from wtforms import Form, StringField , SubmitField
from flask import Flask, render_template
from flat import Flatmate,Bill

app = Flask(__name__)

class HomePage(MethodView):
    def get (self):
        return render_template('index.html')

class BillFormPage(MethodView):
    def get (self):
        data_bill = BillForm()
        return render_template('bill_form_page.html', data=data_bill)

class ResultsPage(MethodView):
    def post(self):
        databill = BillForm(request.form)
        amount = float(databill.amount.data)
        period = databill.period.data

        the_bill = Bill(amount,period)
        flatmate1 = Flatmate(float(databill.days_in_house1.data), databill.name1.data)
        flatmate2 = Flatmate(float(databill.days_in_house2.data), databill.name2.data )
        
        return render_template('results.html',name1=flatmate1.name, amount1= round(flatmate1.pays(the_bill,flatmate2),2),
        name2=flatmate2.name, amount2= round(flatmate2.pays(the_bill,flatmate1),2))
        # return '{} should be pay {:.2f} {} should be pay {:.2f}$'.format(flatmate1.name, 
        #        flatmate1.pays(the_bill, flatmate2), flatmate2.name, flatmate2.pays(the_bill,flatmate1))

class BillForm(Form):
    amount = StringField('Bill amount: ')
    period = StringField('Bill period: ')

    name1= StringField('Name: ')
    days_in_house1 = StringField('Day in the house: ')

    name2 = StringField('Name: ')
    days_in_house2 = StringField('Day in the house: ')

    button = SubmitField('Calculate')
    



app.add_url_rule('/', view_func=HomePage.as_view('Home_page'))
app.add_url_rule('/bill_form', view_func=BillFormPage.as_view('Bill_form_page'))
app.add_url_rule('/result', view_func=ResultsPage.as_view('Result_page'))

app.run(debug=True)