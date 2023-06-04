from sympy import symbols, Function, latex

x, a, b, c, d = symbols('x a b c d')

# Definisci la funzione f(x)
f = Function('f')(x)

# Definisci l'espressione di f(x)
espressione = (a * x + b) / (c * x + d)

# Converte l'espressione in LaTeX
espressione_latex = latex(espressione)

# Crea la stringa di testo in LaTeX con l'espressione
stringa_latex = fr"La funzione \( {latex(f)} \) è definita come: \( {espressione_latex} \)"

# Stampa la stringa di testo in LaTeX
print("La stringa di testo in LaTeX è:")
print(stringa_latex)
