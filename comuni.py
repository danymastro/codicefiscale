import json

f = open("Elenco-comuni-italiani.json", "r")
lista = json.loads(f.read())
for x in lista['CODICI al 03_03_2022']:
  x['Denominazione in italiano'] = x['Denominazione in italiano'].capitalize()
