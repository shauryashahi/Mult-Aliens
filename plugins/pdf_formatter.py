from reportlab.platypus import (SimpleDocTemplate,
                                Paragraph,
                                Table,
                                Image,
                                Spacer)
from reportlab.lib.styles import getSampleStyleSheet


PADDING = 5
FILE_NAME = "report/aliens_report.pdf"


def pdf_formatter(data):
    elements = []
    logo = "static_assets/aliens.jpg"
    image = Image(logo, 20, 30)
    elements.append(image)
    title = "Aliens DATABASE"
    paragraph_text = '<font size=18>{}</font>'.format(title)
    styles = getSampleStyleSheet()
    elements.append(Paragraph(paragraph_text, styles["Normal"]))
    elements.append(Spacer(1, 24))
    doc = SimpleDocTemplate(FILE_NAME)
    table = Table(data)
    elements.append(table)
    doc.build(elements)
