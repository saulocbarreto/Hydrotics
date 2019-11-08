#!/usr/bin/env python

from __future__ import print_function
import RPi.GPIO as GPIO
import time, sys
from datetime import datetime
import serial
import os.path

import time
from struct import *
from RF24 import *
from RF24Network import *

FLOW_SENSOR = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)
tries = 100
successful = 0
global count
count = 0
# ------------------------------------------------------------------------------------------------
# --------------------------- Variaveis de Tempo e Rotina do Programa ---------------------------
# -----------------------------------------------------------------------------------------------
deltaT_counting = 3
timesleep = 1
# ------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------
def countPulse(channel):
   global count
   if start_counter == 1:
      count = count+1    


#------------------------------------------------------------------------------------------------
# --------------------------------------- Radio Setup -----------------------------------

radio = RF24(RPI_V2_GPIO_P1_15, RPI_V2_GPIO_P1_24, BCM2835_SPI_SPEED_8MHZ)
network = RF24Network(radio)

millis = lambda: int(round(time.time() * 1000)) & 0xffffffff
octlit = lambda n:int(n, 8)

# Address of our node in Octal format (01,021, etc)
this_node = octlit("01")

# Address of the other node
other_node = octlit("00")

#ms -  How long to wait before sending the next message
interval = 100

radio.begin()
time.sleep(0.1);
network.begin(90, this_node)    # channel 90
radio.printDetails()
packets_sent = 0
last_sent = 0
# -----------------------------------------------------------------------------------------------
# --------------------------- Dados para calculo do Volume micromedido --------------------------
# -----------------------------------------------------------------------------------------------
factor = 1.8819444/3.64
volume = 0
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
GPIO.add_event_detect(FLOW_SENSOR, GPIO.FALLING, callback=countPulse)
#f = open("data.txt", "a")


 
while True:
    try:
        network.update()
        now = millis()
        start_counter = 1
        time.sleep(timesleep)
        start_counter = 0
        flow = ((count*factor)/deltaT_counting)  #(count)/(deltaT_counting))/(1.881944444)
        #volume = ((count/deltaT_counting))/(factor*deltaT_counting)
        volume += flow/60
#        print ("\n")
#        print (datetime.now())
#        print ("\n The Flow is: %.3f Liter/min" % (flow))
#        print ("\n The Flow is: %.3f Liter/s" % (flow/60))
#        print ("\n The Qt of Pulse in %.1f seconds are: %.3f " % (deltaT_counting,count))
#        print ("\n The Total Volume is: %.3f \n" % (volume))
        #f.write("Data: {0} ".format(datetime.now()))
        #f.write("Pulsos: {0}\n".format(count/deltaT_counting))
        #f.write("Fluxo1: {0}\n".format(flow))

        
    # If it's time to send a message, send it!
        if ( now - last_sent >= interval  ):
                last_sent = now
                print('Sending ..')
        
        
                packets_sent += 1
                msg = str(datetime.now())
                msg += " " + str(flow) + " " + str(volume)
                print (msg)
        
               
                while (successful < tries):
                        ok = network.write(RF24NetworkHeader(other_node), str(msg))
                        if ok:
                                print('ok - {0}'.format(successful)) 
                                successful = tries + 1
                        else:
                                successful += 1  
                                if successful == tries:
                                        print('failed - {0}'.format(successful))

        
        successful = 0
        count = 0
        time.sleep(deltaT_counting)
    except KeyboardInterrupt:
        print ('\ncaught keyboard interrupt!, bye')
        GPIO.cleanup()
        #f.close()
        sys.exit()
