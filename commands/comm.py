# examples of using commands in python
import commands
print commands.getoutput('pwd')
print commands.getoutput('upower -i /org/freedesktop/UPower/devices/battery_BAT0')
print commands.getoutput('upower -i /org/freedesktop/UPower/devices/battery_BAT0| grep -E "state|to\ full|percentage"')

