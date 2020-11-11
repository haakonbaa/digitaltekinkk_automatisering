"""For håndtering av HTML"""

from IPython.core.display import display, HTML
import digtek.methods.html_karnaugh

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

# printer et skjema over funskjonene
def table(rows,function_names,var):
    data = "<tr>" + "".join("<th>" + str(v) + "</th>" for v in var) + "".join("<th style=\"width: 10px;text-align:center;\">" + name + "</th>" for name in function_names) + "</tr>"
    for row in rows:
        data += "<tr>" + "".join( ("<th>" + str(el) + "</th>") for el in row ) + "</tr>\n"
    display(HTML("<table>" + data + "</table>"))

def karnaugh(variables,*args):
    return digtek.methods.html_karnaugh.run(variables,*args)
