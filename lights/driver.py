from machine import Pin, PWM

class Lights_Driver:
    def __init__(self) -> None:
        self.lights = []
        self.init_all_pins()
        self.pwm_lights = []


    def init_all_pins(self):
        for i in range(0,15):
            self.lights.append(Pin(i, Pin.OUT))

    def init_all_pwm_pins(self):
        for i in range(0,15):
            self.pwm_lights.append(self.light_pwm_init(self.lights[i]))

    def light_on(self, id: int):
        try:
            self.check_valid_light_gpio(id)
            self.lights[id].on()
            return self.lights[id]
        except ValueError as err:
            print(err)
            raise
    
    def light_off(self, id: int):
        try:
            self.check_valid_light_gpio(id)
            self.lights[id].off()
            return self.lights[id]
        except ValueError as err:
            print(err)
            raise
    
    def light_pwm_init(self, light: Pin):
        light = PWM(light)
        light.freq(1000)
        return light

    def check_valid_light_gpio(self, pin):
        if pin >=0 and pin <= 15:
            return True
        else:
            raise ValueError("GPIO pin should be between 0-15")