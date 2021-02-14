import asyncio

from gdx import gdx
from sender_msg import produce

gdx_sensor = gdx()
gdx_sensor.open_ble("GDX-RB 0K200655")
print("initialize bluetooth connection successful")
gdx_sensor.select_sensors([1,2,4,5])
print("open sensors successful")
gdx_sensor.start(1000)
print("start collecting from sensors")

while True:
  measurements = gdx_sensor.read()
  if measurements == None:
      break
  print(measurements)
  measurements_str =' '.join([str(elem) for elem in measurements])
  print(measurements_str)
  asyncio.run(produce(event_name='new message', message=measurements_str, host='localhost', port=4000))

gdx_sensor.stop()
gdx_sensor.close()
