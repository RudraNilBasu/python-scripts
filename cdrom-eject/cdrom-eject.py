import platform
import os
import ctypes


# windows
if platform.system() == 'Windows':
	# need 'u' before "", if you are using UTF-8. if not you don't need to put it.
	ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)
	print "Ejected on Windows"
# OSX
elif platform.system() == 'Darwin':
	os.system("drutil tray open")
	print "Ejected on Darwin"

# Linux
elif platform.system() == 'Linux':
	os.system("eject cdrom")
	print "Ejected on Linux"

else:
	print "OS Unsupported\n"
	
