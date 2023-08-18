import random
import sys

#Creare una funzione o metodo per generare un numero casuale.
#Creare un'interfaccia testuale per il simulatore di dado.
#Implementare un loop principale che consente all'utente di eseguire più lanci di dado senza dover riavviare il programma.



#Funzione che genera un numero casuale da 1 a 6 (simula il dado)
def lancia_dado():
    number = random.randrange(1,6)
    return number

print("--------------------------------")
print("Benvenuto nel gioco dei dadi!")
print("Sfida il software a chi fà il numero piu alto.")
print("--------------------------------")



while True:
    user_choice = input("Premi Y per tirare il dado oppure X per uscire dal programma.\n")
    
    if user_choice.upper() == 'Y':
        user_dado = lancia_dado()
        banco_dado = lancia_dado()
    elif user_choice.upper() == 'X':
        quit()
    else:
        print("Opzione non valida.")
        
    if user_dado > banco_dado:
        print(f"Hai fatto {user_dado} ed hai vinto!")
        print(f"Il banco ha fatto {banco_dado}")
    elif user_dado == banco_dado:
        print(f"Tu e il banco avete fatto lo stesso numero!\nNumero: {user_dado}")
    else:
        print("Ops, hai perso! Ritenta!")
        print(f"Banco: {banco_dado}\nTuo numero: {user_dado}")