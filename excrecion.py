def renal_E(G_p, k_e1 = 0.0005, k_e2 = 339):
    if G_p <= k_e2:
        E = 0
    else:
        E = k_e1 * (G_p - k_e2)
    return E
