import time

class Auto:
    def __init__(self, targa):
        self.targa = targa
        self.orario_ingresso = time.time()

class Parcheggio:
    def __init__(self):
        self.stiva = {}

    def entra_auto(self, auto):
        if len(self.stiva) >= 10:
            print("il parcheggio è al momento pieno, ripassa più tardi")
        else:
            self.stiva[auto.targa] = auto.orario_ingresso

    def esce_auto(self, auto):
        orario_uscita = time.time()
        differenza_oraria = orario_uscita - auto.orario_ingresso 
        costo = (6/3600) * differenza_oraria
        print(f"il prezzo da pagare per aver usato il parcheggio della macchina {auto.targa} è: {costo: .2f}€ ")

parcheggio = Parcheggio()       
auto_1 = Auto('AA000AA')

parcheggio.entra_auto(auto_1)
domanda = input("stai uscendo dal parcheggio? ").lower()
if domanda == 'si':
    parcheggio.esce_auto(auto_1)
