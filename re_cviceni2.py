###########
# Cviceni #
###########
'''
### Uživatelské jméno

import re

regularniVyraz = re.compile(r"[a-ž]{,8}")
vstup = input("Zadej uzivatelske jmeno: ")
hledani = regularniVyraz.fullmatch(vstup)
if hledani:
    print("Uživatelské jméno je v pořádku!")
else:
    print("Nesprávné uživatelské jméno! Uživatelské jméno smí obsahovat pouze malá písmena a smí být maximálně 8 znaků dlouhé")


### Email s tečkou

import re

regularniVyraz = re.compile(r"\w+.?\w+@\w+\.cz")
email = input("Zadej e-mail: ")
hledani = regularniVyraz.fullmatch(email)
if hledani:
    print("Email je v pořádku!")
else:
    print("Nesprávný email!")


### Záznamy
import re
regularniVyraz = re.compile(r"\+\d{12}")

zaznamy = """
searchNumber: pavca.czechitas action: search phone number of user dita
user: pavca action: send sms to phone number +420728123456
user: jirka: action: send 2 sms to phone number +420734123456
"""

anonymniZapis = regularniVyraz.sub("X" * 12, zaznamy)
print(anonymniZapis)

### Adresy stránek '''
import re
# regularniVyraz = re.compile(r"https?://(w{3}|docs)?.?\w*\.(cz|org|com)") # toto zde nefunguje, ale zde ano - https://regex101.com/
regularniVyraz = re.compile(r"https?://(?:w{3}|docs)?.?\w*\.(?:cz|org|com)") # musela se doplnit otaznik a dvojtecka (findall je nejak vazana na specificke chovani zavorek)

#regularniVyraz = re.compile(r"https?://[a-z.]*\.[czorgm]{1,3}")

emailSRadami = """
Ahoj,
posílám ti pár tipů, kam se podívat. https://realpython.com nabízí spoustu článků i kurzů. http://docs.python.org nabízí tutorial i rozsáhlou dokumentaci. http://www.learnpython.org nabízí hezky strukturovaný kurz pro začátečníky, rozebírá ale i nějaká pokročilejší témata. https://www.pluralsight.com je placený web, který ale kvalitou kurzů víceméně nemá konkurenci. Určitě ale sleduj i web https://www.czechitas.cz.
"""

vysledek = regularniVyraz.findall(emailSRadami)
print(vysledek)