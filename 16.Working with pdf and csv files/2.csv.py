import csv
data=open('example.csv')
csv_reader=csv.reader(data)
data_lines=list(csv_reader)
print(data_lines[0])
print(len(data_lines))
All_emails=[]
for cols in data_lines[1:]:
    All_emails.append(cols[3])
for x in range(len(All_emails)):
    print(All_emails[x])
    
print('\n')

All_names=[]
for items in data_lines[1:]:
    All_names.append(items[1]+' '+items[2])
for x in range(len(All_names)):
    print(All_names[x])
    
file_to_output=open('to_save_file.csv',mode='w',newline='')
csv_writer=csv.writer(file_to_output,delimiter=',')
csv_writer.writerows([['1','2','3'],['4','5','6'],['7','8','9']])
file_to_output.close()
