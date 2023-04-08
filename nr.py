from scipy.optimize import newton
import numpy as np
import newton_raphson as nr
from sympy import symbols, Matrix
from sympy.utilities.lambdify import lambdify

# Variables de prueba
k_p1 = 2.7
k_p2 = 0.021
k_p3 = 0.009
k_p4 = 0.0618
k_1 = 0.065
k_2 = 0.079
K_m0 = 225.59
V_m0 = 2.5
I_pb = 1.2778
V_I = 0.05
I_pob = 3.0987
F_cns = 1
V_G = 1.88
EGP_b, G_pb, G_tb, I_pb = symbols('EGP_b G_pb G_tb I_pb')

def newton_raphson4(fun, x0, tol, max_iter):
    print(f'SOY NW, Y ME HAN LLEGADO: {fun}, {x0}')
    sym_x = EGP_b, G_pb, G_tb
    J = Matrix([fun]).jacobian(sym_x)
    print(f'{J}')
    J_inv = J.inv()

    x = np.array(x0).reshape(-1, 1)

    for i in range(max_iter):
        J_inv_eval = J_inv.subs(list(zip(sym_x, x.flatten())))
        J_inv_eval = np.array(J_inv_eval).astype(np.float64)

        fun_eval = Matrix([fun]).subs(list(zip(sym_x, x.flatten())))
        fun_eval = np.array(fun_eval).astype(np.float64)

        x_aux = x.copy()

        x = x - np.dot(J_inv_eval, fun_eval).reshape(-1, 1)

        if np.linalg.norm(x - x_aux, np.inf) <= tol:
            break

    n_iter = i + 1
    error = np.linalg.norm(x - x_aux, np.inf)
    return x.flatten(), n_iter, error


fun = [EGP_b + k_p2 * G_pb + k_p3 * (I_pb / V_I) + k_p4 * (I_pb / V_I) - k_p1,
       F_cns - EGP_b + k_1 * G_pb - k_2 * G_tb,
       K_m0 * EGP_b + G_tb * EGP_b - K_m0 * F_cns - (F_cns + V_m0) * G_tb]

x0 = np.array([2, 100 * V_G, 140])
# x0 = [2, 100 * V_G, 140]
tol = 1e-6
max_iter = int(1e7)
x, _, _ = nr.newton_raphson(fun, x0, tol, max_iter)
# x = newton(fun, x0, tol=tol, maxiter=max_iter)

EGP_b = x[0]
G_pb = x[1]
G_tb = x[2]

I_b = I_pb / V_I
G_b = G_pb / V_G


if __name__ == "__main__":
    print("Estas probando el modulo Newton_Raphson.py")
    print(f'x: {x}')
    print(f'EGP_b: {EGP_b}')
    print(f'G_pb: {G_pb}')
    print(f'G_tb: {G_tb}')
    print(f'I_b: {I_b}')
    print(f'G_b: {G_b}')
