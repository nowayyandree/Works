from datetime import datetime
#Variabili
nome_barman = "Edo" + "Bot"        
drink_speciale = "DigitalVodka"
prezzo_drink = 5.50
alcolici = ["Mojito","White Russian","Jack Daniels"]
analcolici = ["Limonata","Gazosa"]
drink_disponibili = []
    
def whiletrue ():
    print("\nEcco i drink consigliati per te:")
    for drink_disponibile in drink_disponibili:    #Stampiamo tutti i drink con il ciclo for
        print(drink_disponibile)

    drink_scelto = input()
    if drink_scelto in drink_disponibili:
        #print(f"Hai scelto {drink_scelto},ottima scelta!")
        return f"Hai scelto {drink_scelto},ottima scelta!"                                                #Termina ciclo while
    print("Il drink selezionato non è disponibile al momento.")
    whiletrue()



#whiletrue()

    
    #Inizio programma

print("Benvenuti nel Pub Drink&Codici")
print(f"Mi chiamo {nome_barman}...e sono pronto a servirti!")
print(f"Il nostro drink speciale è: {drink_speciale}")
print("Compralo a soli.."+str(prezzo_drink)) #print(f"Compralo a soli {prezzo_drink}")
print(f"\nI drink alcolici sono: {len(alcolici)}")
print(f"I drink analcolici sono: {len(analcolici)}")
print("Per iniziare inserisci il tuo nome!")
nome_cliente = input()
if nome_cliente == "Geidor":
    print("Ciao Geidor, che piacere rivederti!")
else:
    print(f"Ciao {nome_cliente}, benvenuto!")
print("\nInserisci il tuo anno di nascita")     #Carattere speciale
anno_nascita = int(input())
anni_cliente = datetime.now().year - anno_nascita

print("Hai "+str(anni_cliente)+" anni")
#print(f"Hai {anni_cliente} anni")


if anni_cliente <18:
    print("\nSei minorenne, puoi ordinare solo analcolici!") #indentazione e condizione
    drink_disponibili += analcolici
elif anni_cliente >85:
    print("\nZio, sei un po' vecchiotto eh, vacci piano!!!")
    drink_disponibili += alcolici+analcolici #concatenazione
else:
    print("\nSei maggiorenne, puoi ordinare sia alcolici che analcolici")
    drink_disponibili += alcolici+analcolici

variabile1 = whiletrue()

print(variabile1)


# LISTE
#print("\nEcco i drink alcolici dispoibili:")
#print(alcolico[0])
#print(alcolico[1])
#print(alcolico[2])
#for alcolico in alcolici:
   #print(alcolico)