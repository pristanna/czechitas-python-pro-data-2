############
# Příklady #
############

### Overeni formatu

import re
regulerniVyraz = re.compile(r"\d{6}/?\d{3,4}")
retezec = "951112/8234"
print(regulerniVyraz.match(retezec))
print(retezec + " vysledek:" + str(regulerniVyraz.match(retezec)))
retezec = "9511128234"
print(retezec + " vysledek:" + str(regulerniVyraz.fullmatch(retezec)))

### Pristnejsi overeni formatu
import re
regularniVyraz = re.compile(r"\d{9,10}")

rezetec = "9511121234"
print(regularniVyraz.match(rezetec))
rezetec = "9511121234$ je moje rodné číslo"
print(regularniVyraz.fullmatch(rezetec))

### Zapojeni podminky

import re

regularniVyraz = re.compile(r"\d{6}/?\d{3,4}")
vstup = input("Zadej rodné číslo: ")
hledani = regularniVyraz.fullmatch(vstup)
if hledani:
    print("Rodné číslo je v pořádku!")
else:
    print("Nesprávné rodné číslo!")

### Emaily

import re

regularniVyraz = re.compile(r"\w+@\w+\.cz")
email = input("Zadej e-mail: ")
hledani = regularniVyraz.fullmatch(email)
if hledani:
    print("Email je v pořádku!")
else:
    print("Nesprávný email!")


### Vyhledavani

zapis = """
Zápisy o provedených vyšetřeních:
Pacient 6407156800 trpěl bolestí zad a byl poslán na vyšetření. 
Pacientka 8655057477 přišla na kontrolu po zranění kontníku.
Do ordinace telefonovala pacientka 7752126712, které byl elektronicky vydán recept na Paralen. 
"""
import re
regularniVyraz = re.compile(r"\d{9,10}")
vysledky = regularniVyraz.findall(zapis) # vrací výsledky jako seznam
print(vysledky)
for vysledek in vysledky:
    print(vysledek)

### Nahrazovani aneb priklad anonymizace

zapis = """
Zápisy o provedených vyšetřeních:
Pacient 6407156800 trpěl bolestí zad a byl poslán na vyšetření. 
Pacientka 8655057477 přišla na kontrolu po zranění kontníku.
Do ordinace telefonovala pacientka 7752126712, které byl elektronicky vydán recept na Paralen. 
"""

import re
regularniVyraz = re.compile(r"\d{9,10}")
anonymniZapis = regularniVyraz.sub("X" * 9, zapis)
print(anonymniZapis)