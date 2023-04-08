import kempt
import control as c

# HAY QUE REVISAR LA REALIMENTACION DE KEMPT CON Q_STO

class tracto():
    def __init__(self, D, d, k_gri, k_abs, fBW):
        self.d = d
        self.D = D
        self.k_gri = k_gri
        self.k_abs = k_abs
        self.fBW = fBW
    def __call__(self):
        qsto1 = c.tf([self.d], [1, self.k_gri])
        kemp = kempt.k_empt(self.D)
        a = c.tf([self.k_gri], [1, kemp])
        qsto2 = qsto1 * a
        print(qsto2)
        Q_sto = qsto1 + qsto2
        kemp = float(kempt.k_empt(self.D, c.dcgain(Q_sto)))
        b = c.tf([kemp], [1, self.k_abs])
        qgut = qsto2 * b
        return qgut * self.fBW * self.k_abs

if __name__ == "__main__":
    print("Esta corriento el modulo tracto_gastro.py")
