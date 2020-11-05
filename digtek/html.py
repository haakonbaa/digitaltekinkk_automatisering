"""For håndtering av HTML"""

# Definerer hvilke variabler som brukes når en funksjon printes
VARS = "xyzwabcdefghijklmnopqrstuvABCDEFGHIJKLMNOPQRSTUVWXYZ"

# INPUT tuple
# OUTPUT: string
def tuple_to_string(t):
    if len(t) == 1:
        return f"({t[0]})"
    return str(tuple(t)).replace(" ","")

# INPUT: mintermer i itererbar form, mintermene som tupler eks: [(0,1,1,0,1),(1..
#       minterm eller maxterm
# OUTPUT: HTML Minterm/Maxterm-funksjon
def termfunction(iterable,minterms,var=VARS,name="F",minterm=True):
    variables = len(minterms[0])
    terms = []
    if minterm:
        for term in minterms:
            terms.append("".join(str(var[i]) if term[i] else r"\bar{" + var[i] + r"}" for i in range(variables)) )
        terms = "+".join(terms)
    else:
        for term in minterms:
            terms.append('(' + "+".join(str(var[i]) if not term[i] else r"\bar{" + var[i] + r"}" for i in range(variables)) + ')')
        terms = "".join(terms)
    return('$' + name + "(" + ",".join(str(var[i]) for i in range(variables)) + ') = ' + ('\\Sigma' if minterm else '\\Pi') + tuple_to_string(iterable) + ' = ' + terms + '$')

def table(func):
    if not isinstance(func,BoolFunction):
        raise Exception("Cannot draw table of non-BoolFunction objects!")
    termnumbers = [i for i in range(2**func.variables)]
    binary = [number_to_binary(i,func.variables) for i in termnumbers]
    function = [func(*b) for b in binary]

    _shift = len(str(termnumbers[-1]))
    for i in range(len(termnumbers)):
        print(f"| {str(termnumbers[i]).rjust(_shift)} | {''.join(str(i) for i in binary[i])} | {1 if function[i] else 0} |")

def karnaugh(func,var=VARS):
    print(TABLE44.format("".join(str(l) for l in var[0:2]),"".join(str(l) for l in var[2:4]),*[1 if func(*number_to_binary(i,4)) else 0 for i in range(16)]))
