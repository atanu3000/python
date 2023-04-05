# from PyPDF2 import PdfWriter, PdfReader
# pdfwriter = PdfWriter()
# pdf = PdfReader("voter_id.pdf")
# for page_num in range(len(pdf.pages)):
#     pdfwriter.add_page(pdf.pages[page_num])

# password = "14112003"
# pdfwriter.encrypt(password)

# with open('protected.pdf', 'wb') as f:
#     pdfwriter.write(f)
#     f.close()

from PyPDF2 import PdfWriter, PdfReader
import getpass
pdfwriter=PdfWriter()
pdf=PdfReader("voter_id.pdf")
for page_num in range(len(pdf.pages)):
  pdfwriter.add_page(pdf.pages[page_num])
passw=getpass.getpass(prompt='Enter Password: ')
pdfwriter.encrypt(passw)
with open('ho.pdf','wb') as f:
  pdfwriter.write(f)
