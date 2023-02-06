from machine import Pin

touch_sensor = Pin(0, Pin.IN)
led = Pin("LED", Pin.OUT)


while(True):
    if(touch_sensor.value()):
        led.on()
    else:
        led.off()