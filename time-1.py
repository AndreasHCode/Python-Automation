import time

def calcProd():
    product = 1
    for i in range(1, 100000):
        product *= i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('%s seconds have passed' % (int) (endTime - startTime))
