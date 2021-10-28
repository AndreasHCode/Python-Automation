import threading, time
print('Start Program')

def takeANap():
    print('Sleep\n')
    time.sleep(1)
    print('Wake Up!')

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('Ended Program')
