import sympy as sp

t = sp.Symbol('t')

matrix = sp.Matrix([sp.cos(t), -sp.sin(t), 0],
                   [sp.sin(t), sp.cost(t), 0],
                   [0, 0, 1])

sp.pprint(matrix)
print("--------------------------")
evalueate_matrix = matrix.subs(t, 20*sp.pi/180)
sp.pprint(evalueate_matrix)
print("--------------------------")
numeric_matrix = evalueate_matrix.evalf()
sp.pprint(numeric_matrix)