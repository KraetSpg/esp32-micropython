import machine
import time

pushButtonBoot = machine.Pin(0, machine.Pin.IN)

# für IRQs siehe auch: https://docs.micropython.org/en/latest/library/machine.Pin.html

def irq_pushButton(pin):
    print("IRQ aufgerufen")

# pushButtonBoot.irq(irq_pushButton) # beide Flanken RISING und FALLING
pushButtonBoot.irq(handler=irq_pushButton, trigger=machine.Pin.IRQ_FALLING)
# pushButtonBoot.irq(lambda pin:print("lamda mit {0}".format(pin)))

while True:
    print("Schleife (dummy)")
    time.sleep(1)