# implement a program that prompts the user for their name and outputs, using fpdf2, with these specifications:

# The orientation of the PDF should be Portrait.
# The format of the PDF should be A4, which is 210mm wide by 297mm tall.
# The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
# The shirt’s image should be centered horizontally.
# The user’s name should be on top of the shirt, in white text.

# shirtificate.png

from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_text_color(0, 0, 0) # set to black
        self.set_font("Helvetica", "B", size = 30)
        self.cell(0, 30, "CS50 Shirtificate", align="C", ln=True)

# Instantiation of inherited class
def main():
    # collect name
    name = input("Name: ")
    s = f"{name} took CS50"

    # set up pdf in correct orientation and format
    pdf = PDF(orientation="portrait", format="A4")
    pdf.add_page()

    shirt_width = 180
    width = 210
    height = 297

    # import image, horizontal center
    pdf.image("shirtificate.png", x = 15, y = 60, w = shirt_width)

    # add text in middle
    pdf.set_font("Helvetica", size = 20)
    pdf.set_text_color(255,255,255) # set to white
    pdf.set_xy(0, 130)
    pdf.cell(0, 10, s, align = "C")

    # output as pdf
    
    pdf.output("shirtificate.pdf")



if __name__ == "__main__":
    main()