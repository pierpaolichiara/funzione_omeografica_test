""" 
Questa funzione genera una funzione omeografica
    
Parametri in input
===================
a, b, c, d: coefficienti della funzione omeografica

Output
========
f(x)=(a*x+b)/(c*x+d)


"""


from sympy import symbols

def genera_fz_omeografica(a,b,c,d):
    #import sympy as sp
    #from sympy import symbols
    x=symbols("x")
    f_x=(a*x+b)/(c*x+d)
    return f_x



y=genera_fz_omeografica(1,2,-2,4)
print ("f(x)=",y)

y=genera_fz_omeografica(1,2,0,4)   #e'una retta
print ("f(x)=",y)


