import control as c

class higado():
    def __init__(self, Ipo, I, Gp, k_p1, k_p2, k_p3, k_p4, k_i):
        self.Ipo = Ipo
        self.I = I
        self.Gp = Gp
        self.k_p1 = k_p1
        self.k_p2 = k_p2
        self.k_p3 =  k_p3
        self.k_p4 = k_p4
        self.k_i = k_i
    def __call__(self):
        loop1 = c.tf([-self.k_i], [1, 0])
        loop1 = c.feedback(loop1, 1)
        loop1 = loop1 - self.I
        loop2 = c.tf([-self.k_i], [1, 0])
        loop2 = c.feedback(loop2, 1)
        id = loop2 - loop1
        EGP = self.k_p1 - (self.k_p2 * self.Gp) - (self.k_p3 * id) - (self.k_p4 * self.Ipo)
        EGP = int(EGP.dcgain())
        if EGP < 0:
            return 0
        else:
            return EGP


if __name__ == "__main__":
    print("Esta corriendo el modulo higado.py")
