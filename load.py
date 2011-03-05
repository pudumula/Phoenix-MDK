import serial, time
fd = serial.Serial(port='/dev/ttyUSB0', baudrate=19200)
print fd
fd.setDTR(1)
time.sleep(0.1)
fd.setDTR(0)

