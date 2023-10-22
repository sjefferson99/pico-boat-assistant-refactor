from lights import LightModule

def test_import_light_module():
    light_module = LightModule()
    assert isinstance(light_module, LightModule)