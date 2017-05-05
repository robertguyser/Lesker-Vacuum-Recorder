import sys
import glob
import serial
import time
import csv

def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


print(serial_ports())

ser = serial.Serial('COM5', timeout=1)
ser.baudrate = 19200


text_file = open("VacuumChar-05-01-2017.csv", 'w')

while (True):
    msg = '#01RD\r\n'
    ser.write(msg)
    time.sleep(0.05)
    out = ''
    while ser.inWaiting() > 0:
        out += ser.readline().decode('utf-8')
        if out != '':
            print ">>" + out
            val= str(float(out[3:])) + '\n'
            text_file.writelines(val)
        text_file.flush()
    time.sleep(1)

text_file.close()
ser.close()
