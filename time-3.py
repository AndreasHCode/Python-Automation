import time

print('Enter to start timer')
input()
print('Started')
startTime = time.time()
lastTime = startTime
lapNum = 1
times = []

while True:
    try:
        input()
        currTime = time.time()
        passedTime = round(currTime - lastTime, 3)
        times.append(passedTime)
        lastTime = currTime
        print(str(passedTime) + ' milliseconds have passed since last lap')
    except KeyboardInterrupt:
        print('Ended timer')
        print('Total ellapsed time: ' + str(round(lastTime - startTime, 3)))
        break
    
