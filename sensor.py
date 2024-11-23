import board
import adafruit_si7021 as fruit

sensor = fruit.SI7021(board.I2C())
print(sensor.temperature)
print(sensor.relative_humidity)


#   Can you convert the temperature to fahrenheit?
### The conversion formula is °F = °C × (9/5) + 32