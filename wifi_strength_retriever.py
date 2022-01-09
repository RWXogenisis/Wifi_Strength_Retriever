import subprocess
import time
from sys import stdout as p
import winsound
while True:
    result=str(subprocess.check_output(["netsh","wlan","show","interface"],shell=True))#here shell=True prevent th ecode from opening cmd
    values=[result.find("SSID"),result.find("BSSID"),result.find("Signal")]
    name=result[values[0]:values[1]-8]
    strength=result[values[2]+25:values[2]+28]
    if values[0]>0:
        print(name)
        print(strength)
        if int(strength.rstrip("%"))<60:
            winsound.Beep(3000,500)#SYNTAX:winsound.Beep(frequency,duration)
        else:
            pass
    else:
        print("You are disconnected")
    time.sleep(1.5)
