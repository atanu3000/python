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
import getpass, os
pdfwriter=PdfWriter()
# pdf=PdfReader()
pdf = []
for items in os.listdir():
  if items.endswith('.pdf'):
    pdf.append(PdfReader(items))

# if os.listdir().endswith('.pdf'):
#   pdf = PdfReader(items in os.listdir())
for pdfs in pdf:
    for page_num in range(len(pdfs.pages)):
        pdfwriter.add_page(pdfs.pages[page_num])

passw=getpass.getpass(prompt='Enter Password: ')
pdfwriter.encrypt(passw)
with open('ho.pdf','wb') as f:
  pdfwriter.write(f)
