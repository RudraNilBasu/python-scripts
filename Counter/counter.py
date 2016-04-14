import time
from gi.repository import Notify
def main():
    h=int(input("Enter no of Hours: "))
    m=int(input("Enter no of Minutes: "))
    s=int(input("Enter no of Seconds: "))
    x=s+(m*60)+(h*60*60)
    #x = int(input("Enter number of seconds: "))
    for i in range(x + 1):
        time.sleep(1)
        print(formatTime(x))
        x -= 1
    Notify.init("Time Up")
    Hello=Notify.Notification.new ("Time Over!",
                               "Your Time is over!",
                               "dialog-information")
    Hello.show ()
def formatTime(x):
    minutes = int(x / 60)
    seconds_rem = int(x % 60)
    if (seconds_rem < 10):
        return(str(minutes) + ":0" + str(seconds_rem))
    else:
        return(str(minutes) + ":" + str(seconds_rem))
main()
