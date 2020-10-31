<<<<<<< HEAD
=======
# Dette er eit program som sjekke om to boolske funksjonar er like.
# Den ein funksjonen er gitt på kanonisk form, medan den andre er som ein vanleg boolsk funksjon
# Ein skriv fyrst inn variablane frå MSB til LSB
# skriv så inn mintremane til funksjonen på kanonisk form
# Til slutt skriv ein inn utrykket ein har forenkla den til
# Ein får så tilbake melding på om dei er like eller ikkje

>>>>>>> 56a0bf48b26e750151172c108ba99d7282b25300
def sannhetstabell(variablar, mintermar): #Lager sannhetstabell for ein funskjon vha. mintermane til funksjonen og antal variablar
    tabell = [0 for i in range(2**variablar)]
    for minterm in mintermar:
        tabell[minterm] = 1
    return tabell

def dec2binary(dec,length): #gjer eit desimalt tal om til binært tal med lengda length
        binary = str(bin(dec)[2:])
        binary = "0"*(length-len(binary)) + binary
        return binary


def F(lista, variablar): #Definerer den boolske funksjonen ut frå input func og lista med verdi på variablane
    for i in range(len(variablar)):
        exec("%s = %d" % (variablar[i], lista[i]))
    return int(eval(func))


def main():
    global func
    variablar = input("Skriv inn variablar separert med mellomrom: ").split()
    mintermar = input("Skrvi inn mintermar separert med mellomrom: ").split()
    func = input("Skriv inn funksjonen din: ")
    mintermar = list(map(lambda x: int(x), mintermar))
    fasit = sannhetstabell(len(variablar), mintermar)
    svar = []
    for i in range(len(fasit)):
            binary = dec2binary(i, len(variablar))
            list1 = list(map(lambda x: bool(int(x)), list(binary)))
            svar.append(F(list1, variablar))
    if svar == fasit:
        print("Funksjonane er like")
    else:
        print("\nFunksjonane er ulike")
        print("Fasit: ".ljust(6) + str(fasit) )
        print("Din: ".ljust(7) + str(svar) )
main()
