from lights.driver import Lights_Driver
from time import sleep
from lights.i2c_driver import Lights_I2C_Driver

lights_driver = Lights_Driver()
lights_i2c_driver = Lights_I2C_Driver()

test_all_lights_on = True
test_all_lights_off = True
test_lights_driver = True
test_lights_i2c_driver = True
sleep_time = 0.5

if test_all_lights_on == True:
    lights_driver.all_lights_on()
    sleep(sleep_time)    

if test_all_lights_off == True:
    lights_driver.all_lights_off()
    sleep(sleep_time)

if test_lights_driver == True:
    lights_driver.all_lights_off()
    
    d = 0

    for light in lights_driver.lights:
        lights_driver.set_brightness(light, d)
        d += 0.06

    sleep(sleep_time)

    lights_driver.light_off(3)

    sleep(sleep_time)

    lights_driver.light_on(3)

    lights_driver.light_set_brightness(0, 0.9)
    lights_driver.light_set_brightness(13, 0.1)
    
    sleep(sleep_time)

if test_lights_i2c_driver == True:
    lights_driver.all_lights_off()
    
    sleep(sleep_time)
    lights_i2c_driver.process_I2C(bytearray([0x10])) # 0x00 = light 0 on
    sleep(sleep_time)
    lights_i2c_driver.process_I2C(bytearray([0x11])) # 0x00 = light 1 on
    sleep(sleep_time)
    lights_i2c_driver.process_I2C(bytearray([0x13])) # 0x00 = light 3 on
    sleep(sleep_time)
    lights_i2c_driver.process_I2C(bytearray([0x00])) # 0x00 = light 0 off
    sleep(sleep_time)
    lights_i2c_driver.process_I2C(bytearray([0x01])) # 0x00 = light 1 off
    sleep(sleep_time)
    lights_i2c_driver.process_I2C(bytearray([0x03])) # 0x00 = light 3 off
    sleep(sleep_time)
    lights_i2c_driver.process_I2C(bytearray([0x20, 0x0f])) # 0x00 = light 0 dim
    sleep(sleep_time)
    lights_i2c_driver.process_I2C(bytearray([0x21, 0x7f])) # 0x00 = light 1 half
    sleep(sleep_time)
    lights_i2c_driver.process_I2C(bytearray([0x23, 0xff])) # 0x00 = light 3 full

    sleep(sleep_time)