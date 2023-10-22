from lights import LightModule
from lights.driver import Lights_Driver

def test_import_light_module():
    light_module = LightModule()
    assert isinstance(light_module, LightModule) == True

def test_light_module_has_light_driver():
    light_module = LightModule()
    assert isinstance(light_module.light_driver, Lights_Driver) == True