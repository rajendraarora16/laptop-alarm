import psutil
import winsound
import threading
import os


def check_battery():
    hasBattery = psutil.sensors_battery()
    print "Current battery %s%%" % hasBattery.percent

    if hasBattery.power_plugged == True:
        print "**Charging**"
        if hasBattery.percent == 99:
            Freq = 2500
            Dur = 2000
            winsound.Beep(Freq, Dur)
            print "Your battery is full please unplugged your charger!"
    else:
        print "You have not plugged in your charger"

def trigger():
    threading.Timer(5.0, trigger).start()
    clear = lambda: os.system('cls')
    clear()
    check_battery()

if __name__ == "__main__":
    trigger()

