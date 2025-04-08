# export/pdf_export.py
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO

def generate_pdf(groupes):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    y = height - 50

    c.setFont("Helvetica-Bold", 16)
    c.drawString(180, y, "Répartition des équipes compatibles")
    y -= 40
    c.setFont("Helvetica", 12)

    for num, equipe in groupes.items():
        c.drawString(50, y, f"ÉQUIPE {num+1}")
        y -= 25
        for membre in equipe:
            line = f"- {membre['nom']} ({membre['zodiac']} – {membre['element']})"
            c.drawString(70, y, line)
            y -= 20
            if y < 50:
                c.showPage()
                y = height - 50
                c.setFont("Helvetica", 12)
        y -= 10

    c.save()
    buffer.seek(0)
    return buffer