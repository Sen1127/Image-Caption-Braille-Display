from time import sleep
import serial
from msvcrt import getch

def connect2arduino(str):
    ##==============================================================================
    ser = serial.Serial("COM3", 115200, timeout=2) # Establish the connection on a specific port
    ##==============================================================================

    ##======Write Serial Command to arduino============
    def SerialWrite(word):
        word=word.encode("utf-8")
        ser.write(word)
        rv=ser.readline()
        print (rv.decode("utf-8")) # Read the newest output from the Arduino
        sleep(1) # Delay for one tenth of a second
        ser.flushInput()
    ##====================================

    ##=======Get  Ready================
    print("Connecting to Arduino.....")
    while 1:
        rv=ser.readline()
        print("Loading...")
        #Debug print (rv) # Read the newest output from the Arduino
        print (rv.decode("utf-8")) 
        ser.flushInput()
        sleep(1) # Delay for one tenth of a secon
        Str=rv.decode("utf-8")
        #Debug print(Str[0:5])
        if Str[0:5]=="Ready":  
            print("Get Arduino Ready !")
            break
    ##------------------------------------------------------

    for i in range(len(str)):               # show just one alphabet each time
        SerialWrite(str[i])                 # write into Arduino

    ser.close()