import csv

csvfile = open('example.csv', 'a+', newline='')
csvwriter = csv.writer(csvfile)

csvwriter.writerow(['green', 'eggs', 'ham', 'sam'])

csvreader = csv.reader(csvfile)
print(list(csvreader))

csvfile.close()
