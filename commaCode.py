def addSeperators(stringList):
    for i in range(len(stringList)):
        if i == len(stringList) - 1:
            print("and " + stringList[i])
        else:
            print(stringList[i] + ", ", end="")

spam = ["Apple", "Banana", "Citrus", "Dogfood"]

addSeperators(spam)
