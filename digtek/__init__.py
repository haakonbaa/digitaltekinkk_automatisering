"""En modul for atomatisering av tidkrevende/kjedelige/unødvendige/repetitive
oppgaver i faget TFE4101 Krets og Digitalteknikk. Modulen er skrevet med den
hensikt å gi oversiklige fremmgangsmåter og enkle verifiserings-funskjoner for
å enkelt kunne avgjøre om man har gjort en oppgave riktig i faget.
"""

from builtins import print as original_print
from digtek.boolfunctions import *

SAFEPRINT = False # endrer ikke 'print' funcksjonen i 'True' mode

try:
    from IPython.core.display import display, HTML
except:
    raise DigtekWarning("Cannot import IPython module! Are you not using Jupyter?")

# redefinerer print til å tolke alt input som HTML!
# Dette er veldig dårlig 'practice' og bør egentlig ikke gjøres i det heletatt!
global print
def print(*args,**kwargs):
    if SAFEPRINT:
        original_print(*args,**kwargs)
    else:
        try:
            for text in args:
                display(HTML(str(text)))
        except:
            original_print(*args,**kwargs)
