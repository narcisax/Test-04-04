###Es 1: Crea un sistema ripetibile che si occupi di dividere su tre possibili liste
#i tipi basilari di dato che riceve in entrata. 
#Deve poter stampare una lista singola o tutte.  
#Si deve ripetere X volte definite all'inizio dall'utente

lista_int =  []
lista_str = []
lista_bool = []


def funz_tip():
    valore = input("Inserisci un valore di tipo int/str/bool: ")
    if type(valore) == int:
        lista_int.append(valore)
        print("Valore {valore} inserito nella lista degli interi")
        print(lista_int)
    elif type(valore) == str:
        lista_str.append(valore)
        print("Valore {valore} inserito nella lista delle stringhe")
        print(lista_str)
    elif type(valore)== bool:
        lista_bool.append(valore)
        print("Valore {valore} inserito nella lista dei booelani")
        print(lista_bool)
    else:
        print("Valore inserito non valido")
        
while True:
    funz_tip()
    scelta = input("Vuoi continuare? si/no: ")
    if scelta.lower() == "no":
        break
