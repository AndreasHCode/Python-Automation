import subprocess, threading

for i in range (10):
    cmd = subprocess.Popen(["cmd.exe", "/c color fc&&dir "])
    cmd.poll()
    cmd.wait()

print("Cmd finished")
