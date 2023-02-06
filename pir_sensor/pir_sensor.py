from machine import Pin
pir = Pin(0, Pin.IN)

while True:
    motion = pir.value()
    if motion == 1:
        print("Motion detected")
    else:
        print("No motion detected")