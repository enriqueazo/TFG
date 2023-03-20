from sympy import Matrix, Symbol, diff

def newton_raphson(f, x0, tol, max_iter):
    sym_x = f.free_symbols
    J = Matrix([[diff(fi, xj) for xj in sym_x] for fi in f])
    J_inv = J.inv()
    x = Matrix(x0)

    for i in range(max_iter):
        J_inv_eval = J_inv.subs(list(zip(sym_x, x)))
        J_inv_eval = J_inv_eval.evalf()
        fun_eval = f.subs(list(zip(sym_x, x)))
        fun_eval = fun_eval.evalf()
        x_aux = x.copy()
        x = x - J_inv_eval * fun_eval
        if (x - x_aux).norm() < tol:
            return x.tolist(), i+1

    print("El método de Newton-Raphson no converge")
    return x.tolist(), max_iter

# HAY UN PROBLEMA, RESUELVE DE FORMA ALEATORIA EL SISTEMA DE ECUACIONES

