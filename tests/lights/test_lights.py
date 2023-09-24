from lights.driver import Lights_Driver

def test_import_light_driver():
    lights_driver = Lights_Driver()
    assert isinstance(lights_driver, Lights_Driver) == True

def test_light_switched_on(mocker):
    lights_driver = Lights_Driver()
    Lights_Driver.light_on = mocker.MagicMock()
    lights_driver.light_on()
    Lights_Driver.light_on.assert_called_once()
    