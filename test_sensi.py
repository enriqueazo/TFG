from sensibilidad_insul import InsulinSensivity
import time

def test_sensi():
    assert InsulinSensivity(225.59, [180, 200, 160, 200, 210, 170], [0, 240, 360, 600, 720, 1020], 0, time.time()) == 225.59
