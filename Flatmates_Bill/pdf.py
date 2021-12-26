from fpdf import FPDF

class PdfReport:
    """
    Create a pdf report about the bill
    """
    def __init__(self,filename):
        self.filename = filename
    
    def generate(self, flatmate1, flatmate2, bill):

        M_pay= round(flatmate1.pays(bill,flatmate2),2)
        G_pay = round(flatmate2.pays(bill,flatmate1),2)
        
        pdf = FPDF(orientation = 'P', unit='pt', format='A5')
        pdf.add_page()
        pdf.image('epec.png',x=340,y=0, w=74, h=28)
        #Title
        pdf.set_font(family= 'Times', size=20, style='B')
        pdf.cell(w=0, h=60, txt= "Flatmates Bill", border =1, align='C',ln=1)
        #Period
        pdf.set_font(family= 'Times', size=18, style='B')
        pdf.cell(w=80, h=35, txt='Period: ',border=0)
        pdf.cell(w=80, h=35, txt=bill.period ,border=0,ln=1)
        #Flatmate1
        pdf.set_font(family= 'Times', size=14, style='IB')
        pdf.cell(w=80, h=30, txt=flatmate2.name + ':',border=0)
        pdf.cell(w=120, h=30, txt = str(G_pay)+'$' ,border=0, ln=1)
        #Flatmate2
        pdf.cell(w=80, h=30, txt=flatmate1.name+ ':',border=0)
        pdf.cell(w=120, h=30, txt = str(M_pay)+'$' ,border=0, ln=1)
        #PDF Output
        pdf.output(self.filename)
