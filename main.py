from asyncio import constants
from os import strerror
import comuni

mesi = {
  "GENNAIO" : "A",
  "FEBBRAIO" : "B",
  "MARZO" : "C",
  "APRILE" : "D",
  "MAGGIO" : "E",
  "GIUGNO" : "H",
  "LUGLIO" : "L",
  "AGOSTO" : "M",
  "SETTEMBRE" : "P",
  "OTTOBRE" : "R",
  "NOVEMBRE" : "S",
  "DICEMBRE" : "T"
}

resto = {
  "0" : "A",
  "1" : "B",
  "2" : "C",
  "3" : "D",
  "4" : "E",
  "5" : "F",
  "6" : "G",
  "7" : "H",
  "8" : "I",
  "9" : "J",
  "10" : "K",
  "11" : "L",
  "12" : "M",
  "13" : "N",
  "14" : "O",
  "15" : "P",
  "16" : "Q",
  "17" : "R",
  "18" : "S",
  "19" : "T",
  "20" : "U",
  "21" : "V",
  "22" : "W",
  "23" : "X",
  "24" : "Y",
  "25" : "Z"
}

tab_dispari = {
  "0" : "1",
  "1" : "0",
  "2" : "5",
  "3" : "7",
  "4" : "9",
  "5" : "13",
  "6" : "15",
  "7" : "17",
  "8" : "19",
  "9" : "21",
  "A" : "1",
  "B" : "0",
  "C" : "5",
  "D" : "7",
  "E" : "9",
  "F" : "13",
  "G" : "15",
  "H" : "17",
  "I" : "19",
  "J" : "21",
  "K" : "2",
  "L" : "4",
  "M" : "18",
  "N" : "20",
  "O" : "11",
  "P" : "3",
  "Q" : "6",
  "R" : "8",
  "S" : "12",
  "T" : "14",
  "U" : "16",
  "V" : "10",
  "W" : "22",
  "X" : "25",
  "Y" : "24",
  "Z" : "23"
}

tab_pari = {
  "0" : "0",
  "1" : "1",
  "2" : "2",
  "3" : "3",
  "4" : "4",
  "5" : "5",
  "6" : "6",
  "7" : "7",
  "8" : "8",
  "9" : "9",
  "A" : "0",
  "B" : "1",
  "C" : "2",
  "D" : "3",
  "E" : "4",
  "F" : "5",
  "G" : "6",
  "H" : "7",
  "I" : "8",
  "J" : "9",
  "K" : "10",
  "L" : "11",
  "M" : "12",
  "N" : "13",
  "O" : "14",
  "P" : "15",
  "Q" : "16",
  "R" : "17",
  "S" : "18",
  "T" : "19",
  "U" : "20",
  "V" : "21",
  "W" : "22",
  "X" : "23",
  "Y" : "24",
  "Z" : "25"
}

def anno():
  condition = False
  while (condition == False) or (anno.isnumeric() == False):
    anno = str(input("Inserisci l'anno di nascita per intero(es -> 1965): "))
    anno = anno.replace(" ", "")
    if len(anno) == 4 and anno.isnumeric() == True:
      annodata = anno[2:5]
      return annodata
    else:
      print("Inserimento dell'anno di nascita errato. Devi inserire l'anno utilizzando solo numeri. (es. -> 1965)\n")

def mese():
  ver = 0
  while ver == 0:
    mese = str(input("Inserisci il mese di nascita (es -> maggio): "))
    mese = mese.upper()
    mese = mese.replace(" ", "")
    for x in mesi:
      if mese == x:
        dnmese = mesi[x]
        return dnmese
    print("Mese inserito non correttamente. Hai inserito numeri o caratteri sconosciuti?")

def giorno():
  sesso = str(input("Inserisci il tuo sesso.( M -> Uomo | F -> Donna ): "))
  sesso = sesso.upper()
  sesso = sesso.replace(" ", "")
  while sesso != "M" and sesso != "F":
    print("Inserimento del sesso errato, inserisci 'M' o 'F'.")
    sesso = str(input("Inserisci il tuo sesso.( M -> Uomo | F -> Donna ): "))
    sesso = sesso.upper()
    sesso = sesso.replace(" ", "")
  dngiorno = "_null_"
  condition = False
  while (condition == False) or (dngiorno.isnumeric() == False):
    dngiorno = str(input("Inserisci il giorno di nascita(es -> 24): "))
    dngiorno = dngiorno.replace(" ", "")
    if len(dngiorno) == 1 and dngiorno.isnumeric() == True:
      zero = "0"
      dngiorno = zero + dngiorno
    if len(dngiorno) == 2 and dngiorno.isnumeric() == True:
      if sesso == "F":
        numgiorno = int(dngiorno)
        numgiorno = numgiorno + 40
        return str(numgiorno)
      if sesso == "M":
        return dngiorno
    else:
      print("Inserimento del giorno di nascita errato. Devi inserire il giorno utilizzando solo numeri (es -> 24).\n")
  

def formnome():
  vocali = consonanti = ""
  nomeutente = "_null_"
  while nomeutente.isalpha() == False:
    nomeutente = str(input("Inserisci il nome per intero, utilizza solo lettere: "))
    nomeutente = nomeutente.replace(" ", "")
    nomeutente = nomeutente.replace("'", "")
    nomeutente = nomeutente.upper() 
    if nomeutente.isalpha() == False:
      print("Hai inserito un carattere non riconoscibile, hai inserito caratteri speciali o numeri?\n")
    else:
      print("Nome inserito correttamente.")
      aplha = "AEIOU"
      for x in nomeutente:
        if (x in aplha) == True:
          vocali = vocali+x
        else:
          consonanti = consonanti+x
      #--------------------
      #Costruzione del nome
      #--------------------
      ccons = ""
      if len(consonanti) >= 4:
        ccons = ccons + consonanti[0] + consonanti[2] + consonanti[3]
        return ccons
      if len(consonanti) == 3:
        ccons = consonanti[:3]
        return ccons
      if len(consonanti) < 3:
        while len(consonanti)<3:
          if len(vocali+consonanti) >= 3:
            for x in vocali:
              if len(consonanti) < 3:
                consonanti = consonanti+x
          else:
            consonanti = consonanti + vocali
            while len(consonanti)<3:
              consonanti = consonanti+"X"

  return consonanti[:3]




def formcognome():
  vocali = consonanti = ""
  cognomeutente = "_null_"
  while cognomeutente.isalpha() == False:
    cognomeutente = str(input("Inserisci il cognome per intero, utilizza solo lettere: "))
    cognomeutente = cognomeutente.replace(" ", "")
    cognomeutente = cognomeutente.replace("'", "")
    cognomeutente = cognomeutente.upper() 
    if cognomeutente.isalpha() == False:
      print("Hai inserito un carattere non riconoscibile, hai inserito caratteri speciali o numeri?\n")
    else:
      print("Cognome inserito correttamente.")
      aplha = "AEIOU"
      for x in cognomeutente:
        if (x in aplha) == True:
          vocali = vocali+x
        else:
          consonanti = consonanti+x
      #------------------------
      #Costruzione del cognome
      #------------------------
      if len(consonanti) < 3:
        while len(consonanti)<3:
          if len(vocali+consonanti) >= 3:
            for x in vocali:
              if len(consonanti) < 3:
                consonanti = consonanti+x
          else:
            consonanti = consonanti + vocali
            while len(consonanti)<3:
              consonanti = consonanti+"X"

  return consonanti[:3]
   


def codicecatastale() :
  ver = 0
  while ver == 0:
    nomecomune = str(input("Inserisci il nome del comune: "))
    nomecomune = nomecomune.capitalize()
    print("\nLista dei comuni trovati tramite ricerca:")
    print("-----------------------------------------")
    for x in comuni.lista['CODICI al 03_03_2022']:
      if nomecomune in x['Denominazione in italiano']:
        ver = ver + 1
        print("\nNome comune: ", x['Denominazione in italiano'], "\nProvincia: ",x["Denominazione dell'Unità territoriale sovracomunale \n(valida a fini statistici)"], "\nCodice Catastale: ", x["Codice Catastale del comune"])      
        ccstmp = x["Codice Catastale del comune"]

    if ver == 1:
      ccs = ccstmp
      print("---------------------\nCodice catastale trovato.\n\nDati scelti:")
    elif ver > 1:
      ccs = str(input("\nI comuni sono più di 1, inserisci il codice catastale del comune desiderato: "))
    elif ver == 0:
      print("Comune non trovato. Hai inserito il nome corretto? Controlla gli spazi e le lettere.")

    if ver >= 1:
      for x in comuni.lista['CODICI al 03_03_2022']:
          if ccs == x['Codice Catastale del comune']:
            comscelto = x['Denominazione in italiano']
            provinciascelta = x["Denominazione dell'Unità territoriale sovracomunale \n(valida a fini statistici)"]
      try:
        print("------------------\nComune scelto: ",comscelto,"\nProvincia: ",provinciascelta, "\nCodice catastale: ", ccs )
      except NameError:
        print("Il codice catastale appena inserito non corrisponde con quelli proposti :(")
      controllo = input("\nDesideri utilizzare un altro comune?\nScrivi 'prosegui' se ritieni che il comune sia quello giusto, oppure 'ricomincia' se vuoi cercare un nuovo comune: ")
      if controllo != "prosegui":
        ver = 0
      else:
        return ccs
    
  
def codcont(codice):
  i = somma = 0
  for x in codice:
    i = i + 1
    if i % 2 == 0:
      val = int(tab_pari[x])
      somma = somma + val
    else:
      val = int(tab_dispari[x])
      somma = somma + val
  restoval = somma%26
  for x in resto:
    if str(restoval) == x:
      codicecontrollo = resto[x]
      return codicecontrollo


nome = formnome()
cognome = formcognome()
codice = codicecatastale()
dnanno = anno()
dnmese = mese()
dngiorno = giorno()
code = cognome + nome + dnanno + dnmese + dngiorno + codice
controlcode = codcont(code)
codfinito = code + controlcode
print("\n--------------------------------------------------------------------------------------------------------------------------------------")
print("\n                                              CODICE FISCALE CALCOLATO CON SUCCESSO ;)\n")
print("                           Il codice fiscale calcolato da pizzuto e mastropaolo è --> ",codfinito)