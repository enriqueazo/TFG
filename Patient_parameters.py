import nr as nr
import numpy as np

print('ESTAS USANDO LOS PARÁMETROS DEL PACIENTE')

# Definir las variables simbólicas
from sympy import symbols
EGP_b, G_pb, G_tb = symbols('EGP_b G_pb G_tb')

# Parámetros Insulina
z = (1/5831.648)*(10**6)  # (-)
k_d = 0.0164  # (1/min)
k_a1 = 0.0018  # (1/min)
k_a2 = 0.0182  # (1/min)


# switch health
health = 0

if health == 0:         # PACIENTE SANO
    # Dinámica de la glucosa
    V_G = 1.88         # (dl/kg)
    k_1 = 0.065        # (1/min)
    k_2 = 0.079        # (1/min)

    # Hígado
    k_p1 = 2.70        # (mg/kg/min)
    k_p2 = 0.0021      # (1/min)
    k_p3 = 0.009       # (mg/kg/min por pmol/L)
    k_p4 = 0.0618      # (mg/kg/min por pmol/kg)
    k_i = 0.0079       # (1/min)

    # Utilización de glucosa
    F_cns = 1          # (mg/kg/min)
    V_m0 = 2.50        # (mg/kg/min)
    V_mx = 0.047       # (mg/kg/min por pmol/L)
    K_m0 = 225.59      # (mg/kg)
    K_mx = 0           # (mg/kg por pmol/L)
    p_2U = 0.0331      # (1/min)

    # Extracción renal
    k_e1 = 0.0005      # (1/min)
    k_e2 = 339         # (mg/kg)

    # Dinámica de la insulina
    V_I = 0.05         # (L/kg)
    m_1 = 0.190        # (1/min)
    m_2 = 0.484        # (1/min)
    m_4 = 0.194        # (1/min)
    m_5 = 0.0304       # (min * kg/pmol)
    m_6 = 0.6471       # (-)
    HE_b = 0.6         # (-)

    # Tracto gastrointestinal
    k_max = 0.0558     # (1/min)
    k_min = 0.0080     # (1/min)
    k_abs = 0.057      # (1/min)
    k_gri = 0.0558     # (1/min)
    f = 0.90           # (-)
    b = 0.82           # (-)
    c = 0.01           # (-)
    alpha_oral = 0.00013   # (1/mg)
    beta_oral = 0.00236    # (1/mg)

    # Práncreas
    K = 2.30           # (pmol/kg por mg/dl)
    alpha = 0.050      # (1/min)
    beta = 0.11        # (pmol/kg/min por mg/dl)
    gamma = 0.5        # (1/min)

    # Condiciones Iniciales
    m_30 = HE_b * m_1 / (1 - HE_b)

    S_b = (m_6 - HE_b) / m_5
    I_pob = S_b / gamma

    I_pb = (2 * S_b * (1 - HE_b))/(5 * m_4)
    I_lb = (S_b - m_4 * I_pb) / m_30

elif health == 1:       # PACIENTE CON T1D
    # Dinámica de la glucosa
    V_G = 1.88         # (dl/kg)
    k_1 = 0.065        # (1/min)
    k_2 = 0.079        # (1/min)

    # Hígado

    k_p1 = 2.70        # (mg/kg/min)
    k_p2 = 0.0021      # (1/min)
    k_p3 = 0.009       # (mg/kg/min por pmol/L)
    k_p4 = 0.0618      # (mg/kg/min por pmol/kg)
    k_i = 0.0079       # (1/min)

    # Utilización de glucosa

    F_cns = 1          # (mg/kg/min)
    V_m0 = 2.50        # (mg/kg/min)
    V_mx = 0.047       # (mg/kg/min por pmol/L)
    K_m0 = 225.59      # (mg/kg)
    K_mx = 0           # (mg/kg por pmol/L)
    p_2U = 0.0331      # (1/min)

    # Extracción renal

    k_e1 = 0.0005      # (1/min)
    k_e2 = 339         # (mg/kg)
    
    # Dinámica de la insulina

    V_I = 0.05         # (L/kg)
    m_1 = 0.190        # (1/min)
    m_2 = 0.484        # (1/min)
    m_4 = 0.194        # (1/min)
    m_5 = 0.0304       # (min * kg/pmol)
    m_6 = 0.6471       # (-)
    HE_b = 0.6         # (-)
    
    # Tracto gastrointestinal

    k_max = 0.0558     # (1/min)
    k_min = 0.0080     # (1/min)
    k_abs = 0.057      # (1/min)
    k_gri = 0.0558     # (1/min)
    f = 0.90           # (-)
    b = 0.82           # (-)
    c = 0.01           # (-)
    alpha_oral = 0.00013   # (1/mg)
    beta_oral = 0.00236    # (1/mg)

    # Práncreas

    K = 2.30           # (pmol/kg por mg/dl)
    alpha = 0.050      # (1/min)
    beta = 0.11        # (pmol/kg/min por mg/dl)
    gamma = 0.5        # (1/min)

    # Condiciones Iniciales

    m_30 = HE_b * m_1 / (1 - HE_b)
    S_b = 0
    I_pob = S_b / gamma
    I_pb = 0
    I_lb = 0

elif health == 2:       # PACIENTE CON T2D
   # Dinámica de la glucosa
    V_G = 1.49         # (dl/kg)
    k_1 = 0.042        # (1/min)
    k_2 = 0.071        # (1/min)

    # Hígado
    k_p1 = 3.09        # (mg/kg/min)
    k_p2 = 0.0007      # (1/min)
    k_p3 = 0.005       # (mg/kg/min por pmol/L)
    k_p4 = 0.0786      # (mg/kg/min por pmol/kg)
    k_i = 0.0066       # (1/min)

    # Utilización de glucosa
    F_cns = 1          # (mg/kg/min)
    V_m0 = 4.65        # (mg/kg/min)
    V_mx = 0.034       # (mg/kg/min por pmol/L)
    K_m0 = 466.21      # (mg/kg)
    K_mx = 0           # (mg/kg por pmol/L)
    p_2U = 0.0840      # (1/min)

    # Extracción renal
    k_e1 = 0.0007      # (1/min)
    k_e2 = 269         # (mg/kg)

    # Dinámica de la insulina
    V_I = 0.04         # (L/kg)
    m_1 = 0.379        # (1/min)
    m_2 = 0.673        # (1/min)
    m_4 = 0.269        # (1/min)
    m_5 = 0.0526       # (min * kg/pmol)
    m_6 = 0.8118       # (-)
    HE_b = 0.6         # (-)

    # Tracto gastrointestinal
    k_max = 0.0465     # (1/min)
    k_min = 0.0076     # (1/min)
    k_abs = 0.023      # (1/min)
    k_gri = 0.0465     # (1/min)
    f = 0.90           # (-)
    b = 0.68           # (-)
    c = 0.09           # (-)
    alpha_oral = 0.00006   # (1/mg)
    beta_oral = 0.00023    # (1/mg)

    # Secreción de insulina
    K = 0.99           # (pmol/kg por mg/dL)
    alpha = 0.013      # (1/min)
    beta = 0.05        # (pmol/kg/min por mg/dL)
    gamma = 0.5        # (1/min)

    # Condiciones Iniciales
    m_30 = HE_b * m_1 / (1 - HE_b)

    S_b = (m_6 - HE_b) / m_5
    I_pob = S_b / gamma

    I_pb = (2 * S_b * (1 - HE_b))/(5 * m_4)
    I_lb = (S_b - m_4 * I_pb) / m_30

# Definir las ecuaciones del sistema
eq1 = EGP_b + k_p2 * G_pb + k_p3 * (I_pb / V_I) + k_p4 * I_pob - k_p1
eq2 = F_cns - EGP_b + k_1 * G_pb - k_2 * G_tb
eq3 = K_m0 * EGP_b + G_tb * EGP_b - K_m0 * F_cns - (F_cns + V_m0) * G_tb

# Definir la condición inicial
x0 = np.array([2, 100 * V_G, 140])

# Definir la tolerancia y el número máximo de iteraciones
tol = 1e-6
max_iter = int(1e7)

# Resolver el sistema de ecuaciones utilizando el método de Newton-Raphson
from sympy import Matrix
from sympy.abc import x
from sympy.solvers.solvers import solve
 
f = Matrix([eq1, eq2, eq3])
x, num_iter = nr.newton_raphson(f, x0, tol, max_iter)

# Asignar las soluciones a las variables EGP_b, G_pb y G_tb
EGP_b, G_pb, G_tb = x[0], x[1], x[2]
print(f'EGP_b = {EGP_b} mg/kg/min\nG_pb = {G_pb} mg/kg\nG_tb = {G_tb} mg/kg')

# Calcular las variables G  _b e I_b
I_b = I_pb / V_I
G_b = float(G_pb[0]) / V_G
print(f'G_b = {G_b} mg/dL\nI_b = {I_b} pmol/L')
