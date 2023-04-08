import sympy as sp
import numpy as np
EGP_b, G_pb, G_tb, I_pb = sp.symbols('EGP_b G_pb G_tb I_pb')

def newton_raphson(fun, x0, tol, max_iter):
    print(f'SOY NW, Y ME HAN LLEGADO: {fun}, {x0}\n\n')
    sym_x = EGP_b, G_pb, G_tb
    n = len(sym_x)

    # Crear una función simbólica a partir de 'fun'
    sym_fun = sp.Matrix(fun)

    # Calcular la matriz jacobiana de 'fun' con respecto a 'sym_x'
    J = sym_fun.jacobian(sym_x)

    # Convertir 'sym_fun' y 'J' en funciones numéricas para su evaluación
    fun_eval = sp.lambdify(sym_x, sym_fun, 'numpy')
    J_eval = sp.lambdify(sym_x, J, 'numpy')

    # Convertir 'x0' a un arreglo numpy si es necesario
    x0 = np.asarray(x0)

    # Iterar hasta que se alcance la tolerancia o el número máximo de iteraciones
    for i in range(max_iter):
        # Evaluar 'fun' y 'J' en 'x0'
        fun_eval_x0 = fun_eval(*x0)
        print(f'fun_eval_x0: {fun_eval_x0}\n')

        J_eval_x0 = J_eval(*x0)

        # Calcular la dirección de búsqueda 'delta_x' mediante la inversión de 'J_eval_x0'
        try:
            J_inv = np.linalg.inv(J_eval_x0)
        except np.linalg.LinAlgError:
            print("La matriz jacobiana es singular en la iteración", i)
            break
        
        delta_x = -J_inv.dot(fun_eval_x0)

        # Actualizar 'x0'
        x0 = np.asarray(x0) + delta_x

        # Verificar la condición de parada
        # if np.linalg.norm(delta_x, np.inf) < tol:
        #    break

    n_iter = i + 1
    error = np.linalg.norm(fun_eval(*x0), np.inf)

    return x0, n_iter, error

