'''
Mockups of hardware specific modules
Create classes and functions in modules to mock
Create sys objects for the modules
Populate the new modules with the classes and functions
Insert the new modules in the sys.modules dictionary
'''

import sys
import os
import asyncio
import errno
import socket
import time
import binascii

# Define classes and functions to be mocked in testing
# machine module
class Pin:
    IN = 0 # type: int
    OUT = 1 # type: int
    PULL_DOWN = 2 # type: int
    PULL_UP = 1 # type: int

    def __init__(self, id: int|str, /, mode: int = IN, pull: int = PULL_UP) -> None:
        pass
    
    def off(self) -> None:
        """
        Sets the pin to be off.
        """
        pass

    def on(self) -> None:
        """
        Sets the pin to be on.
        """
        pass
    
    def toggle(self) -> None:
        """
        Sets the pin to high if it's currently low, and vice versa.
        """
        pass
    
class I2C:
    def __init__(self, id: int, sda, scl, freq: int):
        pass

    def scan(self):
        pass

class PWM:
    """
    Pulse width modulation (PWM), allows you to give analogue behaviours to digital
    devices, such as LEDs. This means that rather than an LED being simply on or
    off, you can control its brightness.

    Example usage::

       from machine import PWM

       pwm = PWM(pin)          # create a PWM object on a pin
       pwm.duty_u16(32768)     # set duty to 50%

       # reinitialise with a period of 200us, duty of 5us
       pwm.init(freq=5000, duty_ns=5000)

       pwm.duty_ns(3000)       # set pulse width to 3us

       pwm.deinit()
    """

    def __init__(self, pin: Pin):
        """
        Construct and return a new PWM object using the following parameters:

           - *pin* should be the pin to use.
        """
        pass

    def freq(self, frequency: int|None=...):
        """
        With no arguments the frequency in Hz is returned.

        With a single *value* argument the frequency is set to that value in Hz.  The method may raise a ``ValueError`` if the frequency is outside the valid range.
        """
        pass

    def duty_u16(self, duration: int|None=...):
        """
        Get or Set the current duty cycle of the PWM output, as an unsigned 16-bit value in the range 0 to 65535 inclusive.

        With no arguments the duty cycle is returned.

        With a single *value* argument the duty cycle is set to that value, measured as the ratio ``value / 65535``.
        """
        pass

# network module
class WLAN():
    def __init__(self, interface) -> None:
        pass

    def config(self, item: str) -> bytes:
        return bytes(0)
    
    def active(self, mode: bool):
        pass

    def connect(self, ssid: str, password: str):
        pass

    def status(self):
        return 3
    
    def ifconfig(self):
        config = ["192.168.1.100"]
        return config

# rp2 module
def rp2_country(id: str):
    return 0

# build mocked modules for testing using functions and classes above
machine = type(sys)('machine')
machine.Pin = Pin
machine.I2C = I2C
machine.PWM = PWM

network = type(sys)('network')
network.WLAN = WLAN
network.STA_IF = 0

rp2 = type(sys)('rp2')
rp2.country = rp2_country

# Insert mocked modules into testing environment
sys.modules['machine'] = machine
sys.modules['uasyncio'] = asyncio
sys.modules['uos'] = os
sys.modules['uerrno'] = errno
sys.modules['usocket'] = socket
sys.modules['utime'] = time
sys.modules['network'] = network
sys.modules['rp2'] = rp2
sys.modules['ubinascii'] = binascii
