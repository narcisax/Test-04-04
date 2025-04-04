###Es 1: Crea un sistema ripetibile che si occupi di dividere su tre possibili liste
#i tipi basilari di dato che riceve in entrata. 
#Deve poter stampare una lista singola o tutte.  
#Si deve ripetere X volte definite all'inizio dall'utente

lista_int =  []
lista_str = []
lista_bool = []


def funz_tip():
    valore = input("Inserisci un valore di tipo int/str/bool: ")
    
    if valore.isdigit(): #dato che dopo una serie di prove mi sono ricordata che un input 
        #restituirà sempre una stringa, 
        #ho trovato questo comando per verificare se il valore è un intero oppure no 
        lista_int.append(int(valore))
        print("Valore {valore} inserito nella lista degli interi")
        print(lista_int)
#qui controllo se è un bool ma metto i valori tra virgolette per lo stesso motivo di prima
    elif valore == "True" or valore == "False":
        lista_bool.append(bool(valore))
        print("Valore {valore} inserito nella lista dei booelani")
        print(lista_bool)
    else: # in questo caso meglio inserire questo controllo nell'else perchè se non è un bool o un int è per forza una stringa
        lista_str.append(valore)
        print("Valore {valore} inserito nella lista delle stringhe")
        print(lista_str)
        
while True:
    funz_tip()
    scelta = input("Vuoi continuare? si/no: ")
    if scelta.lower() == "no":
        print("Lista degli interi:", lista_int)
        print("Lista delle stringhe:", lista_str)
        print("Lista dei booleani:", lista_bool)
        break
       