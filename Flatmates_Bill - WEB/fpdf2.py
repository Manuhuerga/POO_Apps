from fpdf import FPDF

pdf = FPDF(orientation = 'P', unit='pt', format='A4')
pdf.add_page()
pdf.set_font(family= 'Times', size=24, style='B')
pdf.cell(w=0, h=80, txt= "Flatmates Bill", border =1, align='C',ln=1)
pdf.cell(w=100, h=40, txt='Period: ',border=0)
pdf.cell(w=100, h=40, txt='December',border=0)

pdf.output('Bill.pdf')