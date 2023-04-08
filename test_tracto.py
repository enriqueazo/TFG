import kempt
import control as c
import Tracto_gastro as tg

def test_kempt():
    assert kempt.k_empt(2, 0.008, 0.0558, 0.00013, 0.0024, 0.82, 0.01, 2) == 0.05568754657487301

def test_tracto():
    trc = tg.tracto(2, 2, 0.0558, 0.057, 0.9/90)
    assert c.dcgain(trc()) == 0.022122263262238574