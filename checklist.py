from reportlab.lib.colors import gray
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

width, height = letter
margin = 27 # 27 72nds of an inch aka three eights of an inch
line_height = 34 # little less than half an inch
half_width = width / 2
half_height = height / 2
line_width = half_width - 2 * margin

c = canvas.Canvas("checklist.pdf", pagesize=letter)
c.setLineCap(1) # Round cap

# Divide the page into quadrants and make a 10 item blank checklist in each one
for x_quad in range(2):
    for y_quad in range(2):
        x_corner = margin if x_quad == 0 else margin + half_width
        y_corner = margin if y_quad == 0 else margin + half_height

        # Draw lines to write down tasks and circles to fill in when they're done
        for line_idx in range(10):
            y = y_corner + line_height * line_idx
            c.setLineWidth(1)
            c.circle(x_corner, y + line_height / 2 - 2, line_height * 5 / 16)
            c.setLineWidth(1.25)
            c.line(x_corner + line_height * 5 / 16, y, x_corner + line_width, y)

        # Draw a line to fill in the date
        date_start_x = x_corner + half_width * 4 / 8
        date_end_x = half_width - margin if x_quad == 0 else width - margin
        date_y = half_height - margin if y_quad == 0 else height - margin
        c.setLineWidth(1)
        c.line(date_start_x, date_y, date_end_x, date_y)

# Draw faint lines for cutting the pages up
c.setLineWidth(.01)
c.setStrokeColor(gray)
c.setDash(1, 4) # One one, four off
c.line(half_width, 0, half_width, height)
c.line(0, half_height, width, half_height)

# End the PDF page and save it to disk
c.showPage()
c.save()
