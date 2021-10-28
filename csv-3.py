#removeCSVHeader

import csv, os

try:
    os.mkdir('./resources/cleanedCSV')
except FileExistsError:
    print('Folder \"cleanedCSV\" already exists\n')

for file in os.listdir('resources'):
    if not file.endswith('.csv'):
        continue
    
    print('removing header from ' + file)   
        
    csvRows = []
    filepath = str('resources\\' + file)
    print(filepath)
    csvFileObj = open(filepath)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue
        csvRows.append(row)
    csvFileObj.close()

    csvFileObj = open(os.path.join('resources\cleanedCSV', file), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    
