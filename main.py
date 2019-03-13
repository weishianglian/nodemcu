from machine import Pin
import time

led = Pin(2, Pin.OUT)
# for i in range(10):
while True:
    led.off()
    time.sleep(0.5)
    led.on()
    time.sleep(0.5)