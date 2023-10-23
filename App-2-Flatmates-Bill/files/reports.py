from fpdf import FPDF
import webbrowser
import os
class PdfReport:
    """
    create pdf report with data about: flatmates, amount, period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2),2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1),2))

        #generare pdf
        pdf = FPDF(orientation="P", unit='pt', format='A4')
        # create a page
        pdf.add_page()

        # Add icon
        pdf.image("house.png", w=30,h=30)

        # Populate the pdf
        # set font
        pdf.set_font(family='Times', size=24, style='B')
        # create top cell with a title
        pdf.cell(w=0, h=80, txt="Flatmates bill", border=1, align="C", ln=1)

        # create period with value
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0,ln=1)

        # create cells with flatmates
        pdf.set_font(family='Times', size=14)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0,ln=1)

        # create cells with flatmates
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0)        # create cells with flatmates

        # generate pdf doc
        pdf.output(self.filename)

        # display the pdf automatically
        webbrowser.open('file://' + os.path.realpath(self.filename))
