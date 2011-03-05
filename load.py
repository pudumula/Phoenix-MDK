import serial, time
import os, sys
fd = serial.Serial(port='/dev/ttyUSB0', baudrate=19200)
print fd
fd.setDTR(1)
time.sleep(.1)
fd.setDTR(0)
cmd = 'avrdude -b 19200 -P /dev/ttyUSB0 -pm32 -c stk500v1 -U ' + sys.argv[1]
os.system(cmd)
