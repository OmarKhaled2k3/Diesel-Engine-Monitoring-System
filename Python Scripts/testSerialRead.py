import serial
import time
arduino = serial.Serial(port='COM8', baudrate=115200,timeout=0)
while True:
        arduino.write(b'g')
        data = arduino.readline()
        #print(data.decode('utf-8'))
        arduino.flushInput()
        arduino.flushOutput()
        arduino.flush()
        x = (data.decode('utf-8')).split("|")
        print(x)
        time.sleep(0.1)
        
    #arduino.flushInput()
    #arduino.flushOutput()
    #arduino.flush()
    
