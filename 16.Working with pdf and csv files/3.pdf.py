import pypdf
f=open('Working_Business_Proposal.pdf','rb')
pdf_reader=pypdf.PdfReader(f)
print(pdf_reader.get_num_pages())
page_one=pdf_reader.get_page(0)
print(page_one)
page_one_text=page_one.extract_text()
print('\n')
print(page_one_text)
#Writing to a new pdf page
pdf_writer=pypdf.PdfWriter()
pdf_writer.add_page(page_one)
pdf_output=open('some_brandnew.pdf','wb')
pdf_writer.write(pdf_output)
#Displaying all text in a pdf file
All_texts=[]
pdf_reader=pypdf.PdfReader(f)
for item in range(pdf_reader.get_num_pages()):
    page=pdf_reader.get_page(item)
    All_texts.append(page.extract_text())
print('\n')
for item in range(len(All_texts)):
    print(f'Page{item+1}:')
    print(All_texts[item])
    print('\n')

