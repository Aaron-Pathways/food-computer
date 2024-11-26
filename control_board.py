import RPi.GPIO as GPIO
class control_board:

  LIGHT = 29
  FAN_TOP = 35
  FAN_BOTTOM = 33

  def __init__(self):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LIGHT, GPIO.OUT)
    GPIO.setup(FAN_TOP, GPIO.OUT)

    self.light_status = "OFF"
    self.fan_status = "OFF"
    

  def toggle_light(self, duration):
    GPIO.output(LIGHT, GPIO.LOW) 
    self.light_status = __get_updated_status(self.light_status)

  def toggle_fan(self, duration):
    GPIO.output(FAN_TOP, GPIO.LOW) 
    self.fan_status = __get_updated_status(self.fan_status)
  
  def __get_updated_status(current_status):
    if current_status == "OFF":
      return "ON"
    return "OFF"
