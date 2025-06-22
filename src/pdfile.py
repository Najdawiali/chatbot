from fpdf import FPDF as _FPDF
import re


class PDFGenerator:
    def __init__(self, text):
        self.text = text

    def generate_pdf(self):
        clean_text = re.sub(r'[^\x00-\x7F]+', '-', self.text)

        pdf = _FPDF()
        pdf.add_page()
        pdf.set_font("helvetica", size=12)
        pdf.multi_cell(0, 10, clean_text)
        pdf.output("simple_example.pdf")
        print('Done.')
