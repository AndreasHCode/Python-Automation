import csv

csvfile = open('example.csv')
csvwriter = csv.reader(csvfile)

for row in csvreader:
    print('Row #' + str(csvreader.line_num) + ': ' + str(row))

