# Digitalteknikk-automatisering
*Automatisering av tidkrevende/kjedelige/unødvendige/repetitive oppgaver i faget TFE4101 Krets og Digitalteknikk*

# setup (*for Windows*)

## 1. Last ned Python
Last ned siste versjon av Python fra https://www.python.org/. Sørg for at *python.exe* filen ligger i %PATH%
## 2. Last ned pip
*pip* skal allerede være installert med nyere versjoner av Python. For å sjekke; åpne terminalen (Søk på *cmd* eller *ledetekst* i søkefeltet, trykk enter), kjør kommandoen:
```shell
pip help
```
Hvis det kommer opp en feilmelding må du installere *pip*, bruk guiden her: https://www.liquidweb.com/kb/install-pip-windows/
## 3. Last ned jupyter modulen
Sørg for at *pip* er *up-to-date*:
```shell
pip install --upgrade pip
```
Last ned Jupyter-notebook med kommandoen:
```shell
pip install notebook
```
## 4. Last ned og kjør koden
Last ned koden fra https://github.com/haakonbaa/digitalteknikk_automatisering
Pakk ut zip-fila og naviger inn i mappa. Start terminalen fra denne mappa, gjør dette ved å skrive *cmd* inn i navigasjonsfeltet øverst til venstre i viduet. Kjør kommandoen:
```shell
jupyter notebook
```
dobbeltklikk på *intro.ipynb*
