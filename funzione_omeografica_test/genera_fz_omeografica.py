""" 
Questa funzione genera una funzione omeografica a partire da 4 coefficienti
    
Parametri in input
------------------
a, b, c, d: coefficienti della funzione omeografica

Output
------
f(x)=(a*x+b)/(c*x+d)


"""


from sympy import symbols

def genera_fz_omeografica(a,b,c,d):
    x=symbols("x")
    f_x=(a*x+b)/(c*x+d)
    return f_x


def parse_function_domain(domain_extremes: str) -> tuple:
    # TODO
    return tuple()

if __name__ == "__main__":
    y=genera_fz_omeografica(1,2,-2,4)
    print ("f(x)=",y)

    y=genera_fz_omeografica(1,2,0,4)   #e'una retta
    print ("f(x)=",y)


