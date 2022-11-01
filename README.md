# faculdade_disciplina_IoT

# Trabalho IoT

Aluno: Brunno Santana Soares

Matricula: 202002770317

## Problema:

Poluição térmica.

### Descrição

A água quente resultante de processos de resfriamento em siderúrgicas, usinas elétricas, usinas nucleares, refinarias e indústrias em geral, quando despejada sem tratamento em rios e oceanos, pode provocar graves alterações na temperatura dos mesmos. Isso faz com que a quantidade de oxigênio na água seja diminuída, causando a morte de diversas espécies que dependem do ar para sobreviver.

Fonte: [pensamento verde](https://www.pensamentoverde.com.br/meio-ambiente/entenda-o-que-e-e-pode-ser-considerado-poluicao-termica-e-como-afeta-o-meio-ambiente/)

## Solução:

Um sensor que monitora a temperatura da água e que dispara um alerta quando atinge a temperatura ideal (temperatura ambiente), permitindo assim o despejo da água. 

## Código:

```python
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
```

## Protótipo:

![Untitled](Trabalho%20IoT%200ae3f766ea114f6ebb9f546932106fe1/Untitled.png)

### diagram.json:

```jsx
{
  "version": 1,
  "author": "Brunno Santana",
  "editor": "wokwi",
  "parts": [
    {
      "type": "wokwi-esp32-devkit-v1",
      "id": "esp",
      "top": 0,
      "left": 0,
      "attrs": { "env": "micropython-20220618-v1.19.1" }
    },
    {
      "type": "wokwi-dht22",
      "id": "dht1",
      "top": -35.37,
      "left": 142,
      "attrs": { "temperature": "67.4" }
    },
    {
      "type": "wokwi-led",
      "id": "led1",
      "top": -2.7,
      "left": -149.33,
      "attrs": { "color": "red" }
    }
  ],
  "connections": [
    [ "esp:TX0", "$serialMonitor:RX", "", [] ],
    [ "esp:RX0", "$serialMonitor:TX", "", [] ],
    [ "dht1:VCC", "esp:3V3", "red", [ "v0" ] ],
    [ "dht1:GND", "esp:GND.1", "black", [ "v0" ] ],
    [ "esp:D15", "dht1:SDA", "green", [ "h0" ] ],
    [ "led1:C", "esp:GND.2", "green", [ "v0" ] ],
    [ "esp:D13", "led1:A", "green", [ "h0" ] ]
  ]
}
```
