from fpdf import FPDF

class PDF():
    def __init__(self,name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica","B",50)
        self._pdf.cell(0,50,'CS50 Shirtificate', new_x='LMARGIN', new_y="NEXT",align = 'C')
        self._pdf.image("shirtificate.png")
        self._pdf.set_font_size(25)
        self._pdf.set_text_color(255,255,255)
        self._pdf.text(x=60,y=140, text=f"{name} took CS50")
    def save(self,name):
        self._pdf.output(name)

name= input('Name: ')
pdf = PDF(name)
pdf.save('shirtificate.pdf')
