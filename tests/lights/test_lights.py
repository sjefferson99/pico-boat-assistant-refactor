from lights.driver import light_driver

def test_import_light_driver():
    ld = light_driver()
    assert isinstance(ld, light_driver) == True


    