class Prodotto:
    def __init__(self, nome, codice):
        self.nome = nome
        self.codice = codice

class Magazzino:
    def __init__(self):
        self.stiva = {}

    def riempimento(self, prodotto):
        if (prodotto.codice) in self.stiva or prodotto.nome in self.stiva.values():
            print("il prodotto è già presente ")
        else:
            self.stiva[str(prodotto.codice)] = prodotto.nome
            with open("Magazzino_file.txt", "a") as file:
                riga = f"{prodotto.codice},{prodotto.nome}\n"
                file.write(riga)
            print(f"Aggiunto: {prodotto.nome} con il codice {prodotto.codice}")

    def mostra_magazzino(self):
        print("\nStato del magazzino")
        for codice, prodotto in self.stiva.items():
            print(f"{codice} {prodotto}")

    def rimozione(self, codice_rimozione):
        if codice_rimozione in self.stiva:
            del self.stiva[codice_rimozione]
            with open("Magazzino_file.txt", "w") as file:
                file.write(str(self.stiva))
        else:
            print("\nprodotto non presente nel magazzino")

            
        

magazzino = Magazzino()

while True:
    domanda = int(input("\ncosa vuoi fare? (1) Inserire, (2) Vedere, (3) Cancellare, (4) Esci "))
    match domanda:
        case 1:
            nome = input("\ninserisci il nome del prodotto: ").capitalize()
            while True:
                try:
                    codice = int(input("\ninserisci il codice a barre del prodotto: "))
                    break
                except ValueError:
                    print("devi inserire solo numeri ")
            prodotto = Prodotto(nome, codice)
            magazzino.riempimento(prodotto)
            
        case 2:
            magazzino.mostra_magazzino()
            
        case 3:
            while True:
                try:
                    codice_rimozione = input("\ninserisci il codice a barre del prodotto da eliminare: ")
                    break
                except ValueError:
                    print("devi inserire solo numeri ")
            magazzino.rimozione(codice_rimozione)
            
        case 4:     
            print("\nGrazie per aver usato il programma")
            break
        
