import math as m

def k_empt(D, k_min = 0.008, k_max = 0.0558, alpha_oral = 0.00013, beta_oral = 0.0024, b = 0.82, c = 0.01, Q_sto = 0):
    k_empt = k_min + ((k_max - k_min) / 2) * (m.tanh(alpha_oral * (Q_sto - b *D)) - m.tanh(beta_oral * (Q_sto - c * D)) + 2)
    return k_empt


if __name__ == "__main__":
    print('Esta corriendo el modulo kempt.py')