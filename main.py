from utime import sleep
from machine import Pin

a = 'Hello!'
pin7 = Pin(7, Pin.OUT)

while True:
    pin7.value(1)
    print(a)
    sleep(2)
    pin7.value(0)
    sleep(1)
