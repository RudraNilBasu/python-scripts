import time
import os
from gi.repository import Notify

not_executed = 1
hr=input("Enter hour: ")
mn=input("Enter minute: ")
msg=raw_input("Enter message: ")
while(not_executed):
	dt = list(time.localtime())
	hour = dt[3]
	minute = dt[4]
	if hour == hr and minute == mn:
		Notify.init("Start")
		st=Notify.Notification.new("Alarm",msg,"dialog-information")
		st.show()
		#os.popen2("open /Users/rudra/alarm.mp3")
		not_executed = 0
