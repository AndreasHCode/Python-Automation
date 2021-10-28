tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goosebumbs'],
['Text', 'Which is longer than', 'the other', 'texts']]

maxSizes = [0]
maxSizes *= len(tableData)
columnLength = len(tableData[0])

for i in range(len(tableData)):
    for j in tableData[i]:
        if len(j) > maxSizes[i]:
            maxSizes[i] = len(j)

print(str(maxSizes))

def printTable():
    for i in range(columnLength):
        for j in range(len(tableData)):
            missingSpace = maxSizes[j] - len(tableData[j][i])
            print(tableData[j][i].rjust(maxSizes[j], " "), end=" ")
        print()

printTable()
