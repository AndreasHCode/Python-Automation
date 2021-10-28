import time, subprocess

timeleft = 3
while timeleft > 0:
    print(timeleft)
    time.sleep(1)
    timeleft = timeleft - 1

subprocess.Popen(['start', 'resources/mats/alarm.wav'], shell=True)
