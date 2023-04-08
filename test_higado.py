import Higado

def test_higado():
    higado = Higado.higado(1, 2, 3, 2.7, 0.021, 0.009, 0.0618, 0.0079)
    assert higado() == 2
