from machine import Pin, PWM

class Lights_Driver:

    def __init__(self) -> None:
        self.lights = []
        self.init_all_lights()
        self.MAX_DUTY = 65535

    def init_all_lights(self):
        for i in range(0,16):
            self.lights.append(self.light_pwm_init(Pin(i, Pin.OUT)))

    def light_on(self, id: int):
        try:
            self.check_valid_light_gpio(id)
            self.set_brightness(self.lights[id], 1)
            return self.lights[id]
        except ValueError as err:
            print(err)
            raise
    
    def light_off(self, id: int):
        try:
            self.check_valid_light_gpio(id)
            self.set_brightness(self.lights[id], 0)
            return self.lights[id]
        except ValueError as err:
            print(err)
            raise
    
    def light_pwm_init(self, light: Pin):
        pwm_light = PWM(light)
        pwm_light.freq(1000)
        return pwm_light
    
    def set_brightness(self, light: PWM, brightness: float):
        try:
            self.check_valid_light_brightness(brightness)
            light.duty_u16(int(brightness * self.MAX_DUTY))
        except ValueError as err:
            print(err)
            raise

    def light_set_brightness(self, id: int, brightness: float):
        self.set_brightness(self.lights[id], brightness)

    def check_valid_light_gpio(self, pin):
        if pin >=0 and pin <= 15:
            return True
        else:
            raise ValueError("GPIO pin should be between 0-15")
        
    def check_valid_light_brightness(self, brightness):
        if brightness >=0 and brightness <= 1:
            return True
        else:
            raise ValueError("Brightness value should be between 0-1")
        
    def all_lights_off(self):
        for light in range(0, 16):
            self.light_off(light)
    
    def all_lights_on(self):
        for light in range(0, 16):
            self.light_on(light)