fileObj = open('hello.txt', 'w')
fileObj.write('Hello')
fileObj.close()

import subprocess, os, time
notepad = subprocess.Popen(['start', 'hello.txt'], shell=True)
time.sleep(10)

os.remove('hello.txt')
