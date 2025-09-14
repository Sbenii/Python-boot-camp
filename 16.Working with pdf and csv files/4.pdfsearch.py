import pypdf
import re
f=open('Exercise_Files/Find_the_Phone_Number.pdf','rb')
text=''
pdf_reader=pypdf.PdfReader(f)
for item in range( pdf_reader.get_num_pages()):
    page=pdf_reader.get_page(item)
    page_text=page.extract_text()
    text+=page_text
number_search=re.search(r"\d{3}\D\d{3}\D\d{4}",text)
number_search.group()
