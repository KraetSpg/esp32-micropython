import machine
import time

touchPin1 = machine.TouchPad(machine.Pin(14))
led1 = machine.Pin(2, machine.Pin.OUT)

gelesenerWert = 0
toggleState = False # Status der LED
schalterWurdeBereitsUmgeschaltet = False

while True:
    gelesenerWert = touchPin1.read()
    if gelesenerWert < 100:
        print("TouchPad berührung gemessen ({zeitstempel})".format(zeitstempel = time.time_ns()))
        
        if schalterWurdeBereitsUmgeschaltet is False:
            schalterWurdeBereitsUmgeschaltet = True
            toggleState = not toggleState
            print("Schalter wird umgeschaltet")
            led1.value(toggleState)            
        else:
            print("Schalter wurde schon umgeschaltet - mache nichts")
    else:
        schalterWurdeBereitsUmgeschaltet = False
        
    time.sleep(0.1)