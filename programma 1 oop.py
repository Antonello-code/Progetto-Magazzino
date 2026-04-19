import random

class Persona:
    def __init__(self, nome, cognome, età):
        self.nome = nome
        self.cognome = cognome
        self.età = età

class Giocatore(Persona):
    def __init__(self, nome, cognome, età, ruolo, squadra, allenatore):
        super().__init__(nome, cognome, età)
        self.ruolo = ruolo
        self.squadra = squadra
        self.allenatore = allenatore

    def presentazione(self):
        print("Io sono " + self.nome + " " + self.cognome + " e sono un " + self.ruolo + "\n")

    def tiro(self):
        tiro = random.randint(0, 1)
        if tiro == 0:
            print("Mi dispiace non hai segnato \n")
            self.allenatore.parla_male(self.cognome)
        if tiro == 1:
            print("Fantastico, hai appena fatto gol! \n")
            self.squadra.gol_segnati()
            self.allenatore.parla_bene(self.cognome)

class Allenatore(Persona):
    def __init__(self, nome, cognome, età, squadra_allenata, anni_di_esperienza):
        super().__init__(nome, cognome, età)
        self.squadra_allenata = squadra_allenata
        self.anni_di_esperienza = anni_di_esperienza

    def presentazione(self):
        print("Ciao a tutti, io sono " + self.nome + " " + self.cognome + " alleno la " + self.squadra_allenata + " ho " + self.età + " anni, e alleno da " + self.anni_di_esperienza + " anni"+ "\n")

    def parla_male(self, calciatore):
        print(f"Peccato {calciatore}, la palla è andata fuori di poco!! (commento di Mr. {self.cognome}) \n")

    def parla_bene(self, calciatore):
        print(f"EVVAI {calciatore}, la palla è entrata. Complimenti per il gran goal! (commento di Mr. {self.cognome}) \n ")

class Squadra():
    def __init__(self, nome):
        self.nome = nome
        self.lista_calciatori = []
        self.gol = 0

    def aggiungi_calciatori(self, calciatore):
        self.lista_calciatori.append(calciatore)

    def mostra_squadra(self):
        print(f"Ciao, noi siamo la {self.nome}, siamo la nuova squadra professionistica! \n")
        print("I nostri giocatori sono: ")
        for c in self.lista_calciatori:
            print(f"{c.cognome} {c.nome} {c.ruolo} \n")
        print(f"la squadra {self.nome} ha fatto {self.gol} \n")
            
    def tiro_casuale(self):
        calciatore = random.choice(self.lista_calciatori)
        print(f"Tira {calciatore.nome} {calciatore.cognome}!\n")
        calciatore.tiro()

    def gol_segnati(self):
        self.gol += 1 
        
        

   
#main
squadra_1 = Squadra("Inter")
squadra_2 = Squadra("Juventus")
allenatore_2 = Allenatore("Luciano", "Spalletti", "67", "juventus", "30")
allenatore_1 =Allenatore("Cristian", "Chivu", "45", "Inter", "8")
while True: 
    nome = input("Nome: \n").capitalize()
    cognome = input("Cognome: \n").capitalize()
    età = input("Età: \n")
    ruolo = input("Ruolo: \n").lower()
    scelta_squadra = input("In quale squadra vuoi inserire il giocatore? \n").capitalize()
    if scelta_squadra == 'Juventus':
        calciatore = Giocatore(nome, cognome, età, ruolo, squadra_2, allenatore_2)
        squadra_2.aggiungi_calciatori(calciatore)
    elif scelta_squadra == 'Inter':
        calciatore = Giocatore(nome, cognome, età, ruolo, squadra_1, allenatore_1)
        squadra_1.aggiungi_calciatori(calciatore)
    continua = input("vuoi inserire altri calciatori? \n").lower()
    if continua == 'no':
        break

scelta = input("vuoi tirare? \n").lower()

if scelta == 'si':
    squadra_1.tiro_casuale()
    squadra_2.tiro_casuale()

squadra_1.mostra_squadra()
squadra_2.mostra_squadra()

