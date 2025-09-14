# THe correct result is shown below, if you can't download from Google Drive, 
f = open('Exercise_Files/find_the_link.csv')
csv_reader = csv.reader(f)
csv_data = list(csv_reader)
link = ''
# Outer loop over rows
for row_num in range(len(csv_data)):
    # Inner loop over columns
    for col_num in range(len(csv_data[row_num])):
        # Pick only the diagonal element (row index == column index)
        if row_num == col_num:
            link += csv_data[row_num][col_num]
print(link)
