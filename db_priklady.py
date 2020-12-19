import pymongo
uzivatelskeJmeno = "ap85"
heslo = "TLMCbwtI"
adresaServeru = "czechitas.westus2.cloudapp.azure.com"
databaze = "ap85"
klient = pymongo.MongoClient(f"mongodb://ap85:TLMCbwtI@czechitas.westus2.cloudapp.azure.com:27017/ap85")
databaze = klient["ap85"]

# Toto slouží pro test
kolekce = databaze["nakupy"]
nakup = kolekce.find_one()
print(nakup)

'''
Pomocí zakomentování částí kódu spouštím vždy jen tu část kódu, kterou chci
'''

### vlozeni jednoho noveho zaznamu

kolekce = databaze["nakupy"]
nakup = {
    "Jméno": "Petr",
    "Věc": "Prací prášek",
    "Částka v korunách": 399,
    "Datum": "2020-03-04",
    "Značka": "Persil",
    "Hmotnost": 7.8
}
id = kolekce.insert_one(nakup)
print(id)


### vlozeni vice zaznamu

kolekce = databaze["nakupy"]

zbyvajici_nakupy = [
    {
        "Jméno": "Petr",
        "Věc": "Toaletní papír",
        "Částka v korunách": 65,
        "Počet rolí": 6,
    },
    {
        "Jméno": "Libor",
        "Věc": "Pivo na kolaudačku",
        "Částka v korunách": 124,
        "Vratná záloha": 20,
        "Datum": "2020-03-01",
        "Poznámka": "Vrátit otevírák sousedům",
    },
    {
        "Jméno": "Petr",
        "Věc": "Pytel na odpadky",
        "Částka v korunách": 75,
        "Objem pytle": 10,
        "Upozornění": "Příště koupit větší!!!",
    },
    {
        "Jméno": "Míša",
        "Věc": "Utěrky na nádobí",
        "Částka v korunách": 130,
        "Barva": "modrá",
        "Počet kusů v balení": 10,
    },
    {
        "Jméno": "Ondra",
        "Věc": "Toaletní papír",
        "Částka v korunách": 120,
        "Počet rolí": 15,
        "Běžná cena": 150,
    },
    {
        "Jméno": "Míša",
        "Věc": "Pečící papír",
        "Částka v korunách": 30,
        "Místo nákupu": "Albert",
        "Délka v metrech": 30,
        "Poznámka": "Peče celá země",
    },
    {
        "Jméno": "Zuzka",
        "Věc": "Savo",
        "Částka v korunách": 80,
        "Poznámka": "Dokoupit rukavice",
    },
    {
        "Jméno": "Pavla",
        "Věc": "Máslo",
        "Částka v korunách": 50,
        "Datum trvanlivosti": "2020-05-01",
    },
    {
        "Jméno": "Ondra",
        "Věc": "Káva",
        "Částka v korunách": 300,
        "Počet kusů": 2,
        "Značka": "Davidoff",
        "Poznámka": "Nejvíc vypila Míša",
    },
]

kolekce.insert_many(zbyvajici_nakupy)


### Čtení dat

# test načtení dat - vrátí první vložený záznam
kolekce = databaze["nakupy"]

vysledek = kolekce.find_one() # vrací slovník
print(vysledek)
print(vysledek["Jméno"]) # mohu tedy vypsat jen požadovanou položku 


# Sestavení dotazu - vrátí první odpovídající záznam

kolekce = databaze["nakupy"]

dotaz = {"Jméno": "Libor"}
vysledek = kolekce.find_one(dotaz)
print(vysledek)

# Sestavení dotazu - vrátí všechny odpovídající záznamy
kolekce = databaze["nakupy"]

dotaz = {"Jméno": "Libor"}
vysledek = kolekce.find(dotaz) # vrací seznam, v tomto případě to je JSON
print(vysledek)
for dokument in vysledek: # vypíšeme jednotlivé položky seznamu
    print(dokument)

# Sestavení dotazu na základě více klíčů: 

kolekce = databaze["nakupy"]

dotaz = {"Jméno": "Petr", "Věc": "Toaletní papír"}
vysledek = kolekce.find(dotaz)
for dokument in vysledek:
    print(dokument)

# Větší než, menší než
kolekce = databaze["nakupy"]
dotaz = {"Částka v korunách": {"$gt": 100}} # greater than, $lt, $gte, $lte, dolar přidáváme, aby si MongoDB zkratku nespletlo s názvem sloupce. 
vysledek = kolekce.find(dotaz)
for dokument in vysledek:
    print(dokument)

# Výběr hodnoty ze seznamu
kolekce = databaze["nakupy"]
dotaz = {"Jméno": {"$in": ["Libor", "Míša"]}}
vysledek = kolekce.find(dotaz)
for dokument in vysledek:
    print(dokument)

### Úprava dat
kolekce = databaze["nakupy"]
dotaz = { "Věc": "Pivo na kolaudačku" }
vysledek = kolekce.find(dotaz)
for dokument in vysledek:
    print(dokument)

# Změna záznamu
kolekce = databaze["nakupy"]
dotaz = { "Věc": "Pivo na kolaudačku" }
noveHodnoty = { "$set": { "Poznámka": "Otevírák jsme vrátili. " } }
kolekce.update_many(dotaz, noveHodnoty)

# Kontrola
vysledek = kolekce.find(dotaz)
for dokument in vysledek:
    print(dokument)

# Přidání nové poznámky
kolekce = databaze["nakupy"]
dotaz = { "Jméno": "Petr" }
noveHodnoty = { "$set": { "Poznámka": "Chybí účtenka." } }
kolekce.update_many(dotaz, noveHodnoty) # Udate upraví jen jednu první položku

# Kontrola
kolekce = databaze["nakupy"]
dotaz = { "Jméno": "Petr" }
vysledek = kolekce.find(dotaz) 
for dokument in vysledek:
    print(dokument)






