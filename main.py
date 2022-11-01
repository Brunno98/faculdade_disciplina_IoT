import time
from machine import Pin
import dht
import ujson

def blink(led):
  led.on()
  time.sleep(1)
  led.off()

sensor = dht.DHT22(Pin(15))
alert = Pin(13, Pin.OUT)

while True:
  print("Medindo temperatura da água... ")
  sensor.measure() 
  temperature = sensor.temperature()
  if (temperature > 25):
    print("Temperatura acima do ideal! aguardando resfriamento...")
    time.sleep(3)
    continue
  print("temperatura OK.")
  print("Emitindo notificação para liberação da água")
  blink(alert)