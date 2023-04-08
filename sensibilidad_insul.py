def InsulinSensivity(K_m0, InsSen, Tsen, Pvar, t):

    def CalcVar(K_m0, Pvar, InsSen, Tsen):
        maxI = max(InsSen)
        PorVar = K_m0 * (Pvar / 100)
        minK = K_m0 - PorVar
        maxK = K_m0 + PorVar
        Dvar = maxK - minK
        varSen = [0] * len(InsSen)
        for i in range(len(InsSen) - 1):
            varSen[i] = (maxI - InsSen[i]) / maxI
        for i in range(len(InsSen) - 1):
            varSen[i] = varSen[i] / max(varSen)
        for i in range(len(InsSen) - 1):
            varSen[i] = varSen[i] * Dvar
        for i in range(len(Tsen) - 1):
            if (Tsen[i + 1] - Tsen[i]) == 0:
                varSen[i] = 0
                varSen[i + 1] = 0
                if Tsen[i] != 0 and Tsen[i + 1] != 0:
                    Tsen[i + 1] = 0
                else:
                    Tsen[i + 1] = 1
        return varSen, minK, Tsen
    
    KmxSen = [0] * len(InsSen)
    varSen, minK, Tsen = CalcVar(K_m0, Pvar, InsSen, Tsen)

    for i in range(len(Tsen) - 1):
        if t < Tsen[i]:
            KmxSen[i] = 0
        elif t >= Tsen[i] and t <= Tsen[i + 1]:
            KmxSen[i] = (varSen[i + 1] - varSen[i]) / (Tsen[i + 1] - Tsen[i]) * (t - Tsen[i])
        elif t > Tsen[i + 1]:
            KmxSen[i] = varSen[i + 1] - varSen[i]

    KmxSenTot = sum(KmxSen) + varSen[0] + minK
    return KmxSenTot


if __name__ == "__main__":
    print('Esta corriendo el modulo de sensibilidad_insul.py')