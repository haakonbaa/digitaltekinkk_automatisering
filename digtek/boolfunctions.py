""" Definisjon av bolske funksjoner"""

from IPython.core.display import display, HTML

import digtek.util as util
import digtek.html
import digtek.errors

__all__ = ["BoolFunction","LambdaFunction","MintermFunction","MaxtermFunction"]
# Definerer hvilke variabler som brukes når en funksjon printes
VARS = "xyzwabcdefghijklmnopqrstuvABCDEFGHIJKLMNOPQRSTUVWXYZ"



# En superklasse for alle typer bolske funksjoner
class BoolFunction:
    def __init__(self,*args,**kwargs):
        raise digtek.errors.DigtekError("Cannot define function using class BoolFunction! Try Lambda/Minterm/Maxterm-Function instead!")

    def __eq__(self,other):
        if isinstance(other,BoolFunction):
            if self.variables != other.variables:
                return False
            for b in [util.number_to_binary(n,self.variables) for n in range(2**self.variables)]:
                if self(*b) != other(*b):
                    return False
            return True
        return False

    def print(self,*args,**kwargs):
        return display(HTML(self.__str__(*args,**kwargs)))

class LambdaFunction(BoolFunction):
    def __init__(self,func):
        self.variables = func.__code__.co_argcount
        self.function = func

    def __call__(self,*args):
        return self.function(*args)

    # Fordi det er vanskilig å konvertere en funskjon til en string vil
    # denne funskjonen returnere en string av den optimaliserte funskjonen
    # i stedet. Dette kan fikses ved å bruke moduler som 'inspect'..osv, men
    # løsningen blir lite elegant, tar tid å implementere.
    def __str__(self):
        raise digtek.errors.DigtekWarning("Cannot return string of LambdaFunction")
        return self.__repr__()


class MintermFunction(BoolFunction):
    def __init__(self,iterable,variables):
        self.iterable = set(iterable)
        self.variables = variables

    def __call__(self,*args):
        return 1 if util.binary_to_number(*args) in self.iterable else 0

    def __str__(self,name="F",var=VARS):
        return digtek.html.termfunction(self.iterable,tuple(b for b in (util.number_to_binary(n,self.variables) for n in range(2**self.variables)) if self(*b)),var=var,name=name)

class MaxtermFunction(BoolFunction):
    def __init__(self,iterable,variables):
        self.iterable = set(iterable)
        self.variables = variables

    def __call__(self,*args):
        return 0 if util.binary_to_number(*args) in self.iterable else 1

    def __str__(self,name="F",var=VARS):
        return digtek.html.termfunction(self.iterable,tuple(b for b in (util.number_to_binary(n,self.variables) for n in range(2**self.variables)) if not self(*b)),var=var,name=name,minterm=False)
