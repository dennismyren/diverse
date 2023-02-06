from machine import Pin, ADC
import utime as time

# The Analog Sound Noise Microphone Sensor needs to convert the Analog signal to digital.
# Therefore we need to use the ADC, it converts the analog signal to a digital one.

microphone = ADC(26)
led = Pin("LED", Pin.OUT)

while True:
    time.sleep_ms(100)
    value = microphone.read_u16()
    if(value > 400):
        led.on()
    else:
        led.off()
    print(value)