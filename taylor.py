import sympy as sp

# Definición de variables y función
t = sp.Symbol("t")
y = sp.Function("y")(t)

# EDO inicial
EDO = 3 * t**3 - y

# Valores iniciales y paso
y0 = 1
t0 = 0
h = 1

# Derivadas sucesivas
y_prime = EDO
y_double_prime = sp.diff(y_prime, t).subs(sp.Derivative(y, t), EDO)
y_double_prime = y_double_prime.subs(sp.Derivative(y, t), EDO)

y_triple_prime = sp.diff(y_double_prime, t).subs(sp.Derivative(y, t), EDO)
y_triple_prime = y_triple_prime.subs(sp.Derivative(y, t, 2), y_double_prime)

# Evaluación en el punto inicial (t0, y0)
y_prime_eval = y_prime.subs({y: y0, t: t0})
y_double_prime_eval = y_double_prime.subs({y: y0, t: t0})
y_triple_prime_eval = y_triple_prime.subs({y: y0, t: t0})

# Serie de Taylor hasta la tercera derivada
result = (y0 
          + h * y_prime_eval 
          + (h**2 / sp.factorial(2)) * y_double_prime_eval 
          + (h**3 / sp.factorial(3)) * y_triple_prime_eval)

# Imprimir resultados
print("EDO: ", EDO)
print("Primera derivada: ", y_prime)
print("Segunda derivada: ", y_double_prime)
print("Tercera derivada: ", y_triple_prime)
print("Serie de Taylor (aproximación): ", result)
