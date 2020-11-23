#Dette er eit program som forenklar ein funksjon gitt på kanonisk form ved hjelp av tabell metoden


def dec2binary(dec, length):  # gjer eit desimalt tal om til binært tal med lengda length
    binary = str(bin(dec)[2:])
    binary = "0" * (length - len(binary)) + binary
    return binary

def antalEin(binary): #Returnerer antal eittal i binært tal
    antal = 0
    for siffer in binary:
        if siffer == "1":
            antal += 1
    return antal

def mintermar2tabell(mintermar): #Tar inn mintermar ag gjere det om til tabell slik som i tabellmetoden
    tabell = []
    for minterm in mintermar:
        binary = dec2binary(minterm, len(variablar))
        tabell.append([antalEin(binary), tuple([minterm]), binary, False])
    return tabell

def maketabell(tabellMintermar):
    tabell = [None for i in range(len(variablar)+1)]

    for minterm in tabellMintermar:
        if tabell[minterm[0]]:
            tabell[minterm[0]].append(minterm)
        else:
            tabell[minterm[0]] = [minterm]

    return tabell

def forkjellEin(bin1, bin2): #returnerer forenkla binært tal dersom forskjellen er ein ellers None
    forskjell = 0
    for i in range(len(bin1)):
        if bin1[i] != bin2[i]:
            if bin1[i] == "-" or bin2[i] == "-":
                return None
            forenkla = list(bin1)
            forenkla[i] = "-"
            forenkla = "".join(forenkla)
            forskjell += 1
    if forskjell == 1:
        return forenkla
    return None

def tabellmetoden(tabell): #reknar ut neste tabell
    nyTabell = [None for i in range(len(tabell)-1)]
    for i in range(len(tabell)-1):
        if not tabell[i] or not tabell[i+1]:
            continue
        for q in range(len(tabell[i])):
            for w in range(len(tabell[i+1])):
                bin1 = tabell[i][q][2]
                bin2 = tabell[i+1][w][2]
                if forkjellEin(bin1, bin2):
                    tabell[i][q][3] = True
                    tabell[i+1][w][3] = True
                    if nyTabell[i]:
                        nyTabell[i].append([i, tabell[i][q][1] + tabell[i+1][w][1], forkjellEin(bin1, bin2), False])
                    else:
                        nyTabell[i] = [[i, tabell[i][q][1] + tabell[i+1][w][1], forkjellEin(bin1, bin2), False]]
    return nyTabell, tabell

def printTabell(tabell): #printer tabellen på eit "fint" format
    maxSub = len("Subkube")
    maxVerdi = len("Verdi")
    for i in range(len(tabell)):
        if tabell[i]:
            for j in range(len(tabell[i])):
                Sub = len(str(tabell[i][j][1]))
                Verdi = len(tabell[i][j][2])
                if Sub > maxSub:
                    maxSub = Sub
                if Verdi > maxVerdi:
                    maxVerdi = Verdi

    lengdTabell = len("|Gruppa|  |  | Dekka |") + maxSub + maxVerdi

    print("-"*lengdTabell)
    print("|Gruppa| " + "Subkube".ljust(maxSub) + " | " + "Verdi".ljust(maxVerdi) + " | Dekka |")
    print("-"*lengdTabell)
    for i in range(len(tabell)):
        if tabell[i]:
            for minterm in tabell[i]:
                print("|   " + str(minterm[0]) + "  | " + str(minterm[1]).ljust(maxSub) + " | " + str(minterm[2]).ljust(maxVerdi) + " | ", end= "")
                if minterm[3]:
                    print(str(minterm[3]) + "  |")
                else:
                    print(str(minterm[3]) + " |")
                print("-"*lengdTabell)
    print()


def printPI(PI, mintermar):
    kopi = [x[:] for x in PI]
    uttrykk = irredudant(kopi, mintermar)
    maxminterm = len("Mintermar")
    maxuttrykk = len("Uttrykk")
    for primImp in PI:
        if len(bin2boolsk(primImp[2])) > maxuttrykk:
            maxuttrykk = len(bin2boolsk(primImp[2]))
        if len(str(primImp[1])) > maxminterm:
            maxminterm = len(str(primImp[1]))

    essensiel = [] #Finn mintermane som berre er dekka av ein primimplikant
    for minterm in mintermar:
        antal = 0
        for primImp in PI:
            if minterm in primImp[1]:
                antal += 1
        if antal == 1:
            essensiel.append(minterm)

    mintermar.sort()
    maxsiffer = len(str(mintermar[-1]))
    lengd = len("|  |  |") + len(mintermar)*(3 + maxsiffer) + len(" Valgt |") + maxminterm + maxuttrykk
    print("-"*lengd)
    print("| " + "Uttrykk".ljust(maxuttrykk)+ " | " + "Mintermar".ljust(maxminterm) + " |", end="")
    for minterm in mintermar:
        print(" " + str(minterm).ljust(maxsiffer) + " |", end="")
    print(" Valgt |")
    print("-"*lengd)
    for primImp in PI:
        boolsk = bin2boolsk(primImp[2])
        print("| " + boolsk.ljust(maxuttrykk) + " | " + str(primImp[1]).ljust(maxminterm) + " |", end="")
        for minterm in mintermar:
            if minterm in primImp[1]:
                if minterm in essensiel:
                    print(" " + "o".ljust(maxsiffer) + " |", end="")
                else:
                    print(" " + "x".ljust(maxsiffer) + " |", end="")
            else:
                print(" " + " ".ljust(maxsiffer) + " |", end="")
        if primImp in uttrykk:
            print(" True  |")
        else:
            print(" False |")
        print("-"*lengd)
    print()



def essensielPI(PI, mintermar): #Finner essensielle primimplikantar. Endrer så veriden til True
    for minterm in mintermar:
        dekkt = 0
        for i in range(len(PI)):
            if minterm in PI[i][1]:
                dekkt += 1
                primImp = i
        if dekkt == 1:
            PI[primImp][3] = True
    return PI

def delDuplicat(PI): #Fjerner duplikat av primimplikantar
    kopi = [x[:] for x in PI]
    """for i in range(len(PI)-1):
        for q in range(i+1, len(PI)):
            if PI[i][2] == PI[q][2]:
                print(PI[i])
                kopi.remove(PI[i])"""
    for i in range(len(PI)-1,0,-1):
        for q in range(i-1,-1,-1):
            if PI[i][2] == PI[q][2]:
                kopi.pop(i)
                break
    return kopi

def irredudant(PI, mintermar): #finner irredudant dekkning ved å velge dei mintermane som dekke flest udekka mintermar
    uttrykk = []
    mintermar = set(mintermar)
    dekkt = None
    for primImp in PI:
        if primImp[3]:
            if not dekkt:
                dekkt = set(primImp[1])
            else:
                dekkt = dekkt.union(set(primImp[1]))
            uttrykk = uttrykk + [primImp]
            PI.remove(primImp)
    manglar = mintermar.difference(dekkt)
    while manglar:
        maks = 0
        for i in range(len(PI)):
            if len(set(PI[i][1]).intersection(manglar)) > maks:
                maks = len(set(PI[i][1]).intersection(manglar))
                maksInd = i
        uttrykk = uttrykk + [PI[maksInd]]
        dekkt = dekkt.union(set(PI[maksInd][1]))
        manglar = mintermar.difference(dekkt)
        PI.pop(maksInd)

    return uttrykk


def irredudant2boolsk(irredudant): #Gjer irredudant dekning om til boolskfunksjon
    boolsk = ""
    for primImp in irredudant:
        uttrykk = ""
        for i in range(len(primImp[2])):
            if primImp[2][i] == "1":
                uttrykk += variablar[i]
            elif primImp[2][i] == "0":
                uttrykk += variablar[i] + "'"
        uttrykk += " + "
        boolsk += uttrykk
    return boolsk[:-3]

def bin2boolsk(binstr):
    boolsk = ""
    for i in range(len(binstr)):
        if binstr[i] == "1":
            boolsk += variablar[i]
        elif binstr[i] == "0":
            boolsk += variablar[i] + "'"
    return boolsk


def main(variabla,mintermar):
    global variablar
    variablar = variabla
    tabellMintermar = mintermar2tabell(mintermar)
    tabellMintermar.sort(key= lambda minterm: minterm[0])
    nyTabell = maketabell(tabellMintermar)
    PI = [] #Prim implikantar
    print("\nTabellar:")
    while True: #Kjører tabellmetoden til det ikkje går an å forenkla meir
        nyTabell,tabell = tabellmetoden(nyTabell)
        if nyTabell == [None for i in range(len(nyTabell))]:
            for i in range(len(tabell)):
                if tabell[i]:
                    for q in range(len(tabell[i])):
                        PI.append(tabell[i][q])
            printTabell(tabell)
            break
        for i in range(len(tabell)):
            if tabell[i]:
                for q in range(len(tabell[i])):
                    if not tabell[i][q][3]:
                        PI.append(tabell[i][q])
        printTabell(tabell)

    PI = delDuplicat(PI)
    PI = essensielPI(PI, mintermar)
    print("Tabell for å finna minimaldekkning:")
    printPI(PI, mintermar)

    uttrykk = irredudant(PI, mintermar)
    boolsk = irredudant2boolsk(uttrykk)
    print("Forenkla boolsk funksjon:")
    print("F = " + boolsk)
