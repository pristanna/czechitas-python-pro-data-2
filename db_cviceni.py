import pymongo
uzivatelskeJmeno = "ap85"
heslo = "TLMCbwtI"
adresaServeru = "czechitas.westus2.cloudapp.azure.com"
databaze = "ap85"
klient = pymongo.MongoClient(f"mongodb://ap85:TLMCbwtI@czechitas.westus2.cloudapp.azure.com:27017/ap85")
databaze = klient["ap85"]

'''
Pomocí zakomentování částí kódu spouštím vždy jen tu část kódu, kterou chci
'''
### Každý má svou pravdu

kolekce = databaze["hry"]

hra = {
    "Představení" : "Modrovous",
    "Délka v minutách" : 70,
    "Premiéra" : "2018-12-15",
}
id = kolekce.insert_one(hra)
print(id)

hra = {
    "Představení" : "Každý má svou pravdu",
    "Premiéra" : "2020-02-08",
}
id = kolekce.insert_one(hra)
print(id)

hra = {
    "Představení" : "Expres na západ",
    "Délka v minutách" : 120,
    "Derniéra" : "2019-11-13",
}
id = kolekce.insert_one(hra)
print(id)

# vrátí první záznam
kolekce = databaze["hry"]
vysledek = kolekce.find_one()
print(vysledek)

### Knihovna

kolekce = databaze["knihy"]

zaznamy = [
  {
    "Název" : "Smrt bere jackpot",
    "Počet stran" : 542,
    "Oběť" : "Freddy Brower",
    "Vrah" : "Leon Lamarr",
  },
  {
    "Název": "Zaklínač I. - Poslední přání",
    "Autor" : "Andrzej Sapkowski",
    "Počet povídek" : 8,
    "Počet stran" : 274,
  },
  {
    "Název" : "Matyáš Sandorf",
    "Podtitul" : "Nový hrabě Monte Christo",
    "Autor" : "Jules Verne",
    "Počet stran" : 442,
  },
]

id = kolekce.insert_many(zaznamy)
print(id)

# vrátí první záznam
kolekce = databaze["knihy"]
vysledek = kolekce.find_one()
print(vysledek)

# vrátí všechny záznamy odpovídající dotazu
dotaz = {"Název": "Smrt bere jackpot"}
vysledek = kolekce.find(dotaz)
print(vysledek)
for dokument in vysledek:
    print(dokument)


#### Druhá část úkolů
## Expres na západ

# vrátí všechny záznamy odpovídající dotazu

kolekce = databaze["hry"]
dotaz = {"Představení": "Expres na západ"}
vysledek = kolekce.find(dotaz)
print(vysledek)
for dokument in vysledek:
    print(dokument)

# Změna/pridani záznamu
kolekce = databaze["hry"]
dotaz = {"Představení": "Expres na západ"}
noveHodnoty = { "$set": { "Premiéra": "2015-11-10" } }
kolekce.update_many(dotaz, noveHodnoty)

# Kontrola
vysledek = kolekce.find(dotaz)
for dokument in vysledek:
    print(dokument)

## Hodnocení knih


kolekce = databaze["goodreads"]
vysledek = kolekce.find_one()
print(vysledek)

# autor
kolekce = databaze["goodreads"]
dotaz = {"authors" : "Robert Graves"}
vysledek = kolekce.find(dotaz)
for dokument in vysledek: # vypíšeme jednotlivé položky seznamu
    print(dokument)

### Oprava chyby

kolekce = databaze["goodreads"]
dotaz = {"publication_date" : "6/31/1982"}
vysledek = kolekce.find(dotaz)
for dokument in vysledek:
  print(dokument)

# uprava
dotaz = {"title" : "Montaillou  village occitan de 1294 à 1324"}
noveHodnoty = { "$set": { "publication_date": "7/1/1982" } }
kolekce.update_one(dotaz, noveHodnoty)

# kontrola
vysledek = kolekce.find(dotaz)
for dokument in vysledek:
  print(dokument)

### Větší než

kolekce = databaze["goodreads"]
dotaz = {"ratings_count" : {"$gt" : 2000000}}
vysledek = kolekce.find(dotaz)
for dokument in vysledek:
  print(dokument)








