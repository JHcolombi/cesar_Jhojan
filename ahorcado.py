import math
import random
import os
intentos=0
vector1=["h",'jhoan',"felipe","gaitan","hernandez","parangaturimicaro"]

def principio():
     palabras,guiones=palabra()
     intentos=0
     while guiones != palabras and intentos<5:
         print(f"palabra: {guiones}")
         leer_por_teclado=input("escrba una letra ")
         if leer_por_teclado in palabras:
             guiones=reeplazar_guiones(palabras,guiones,leer_por_teclado)
             print("excelente atinaste")
         else:
             if intentos==0:
                 print("---------")
                 print("         |")
             print("intenta de nuevo no le atinaste")
             while intentos==5:
                break;
             intentos=intentos+1
            #leer_por_teclado=input("escrba una letra ")
     if guiones==palabras:
         print(f"grandioso adivinaste ")    
     else:
         print(f"lo siento la palabra era {palabras} ")            

#esta devolviendo guiones determinado por la cantidad de palabras que tenga el elemento de la lista vector1
def palabra():
    palabras=random.choice(vector1)
    guiones="_"*len(palabras)
    return palabras,guiones

def reeplazar_guiones(palabras,guiones,simbolo):
    #cuantas veces aparece en la cadena original
    cantidad=palabras.count(simbolo)
    inicio=0
    for i in range(cantidad):
        #esta buscando segun la palabra original y la esta remplazando
        ubicacion=palabras.find(simbolo,inicio)#indica donde esta el simbolo a partir de la ubicacion de inicio desde la primer inncicacion del simbolo
        guiones=guiones[:ubicacion]+simbolo+guiones[ubicacion+1:]
        inicio=ubicacion+1
    return guiones

def ahorcado():
    print(f"Hola, tendras que adivinar la palabra secreta \n\
          recurda que tienes {intentos} intentos para jugar\n\
          !Buena Suerte¡\n\
          \nselecciona una letra por favor: ")
    principio()
    os.system('cls')
ahorcado()



"""guiones=reeplazar_guiones('hola','___','la')
print(guiones)"""
"""palabra_completa,cantidad_guienes=palabras()
print(palabra_completa)
print(cantidad_guienes)"""


"""#esta devolviendo guiones determinado por la cantidad de palabras que tenga el elemento de la lista vector1
def palabra():
    import random
    import os
    intentos=0
    vector1=["h",'jhoan',"felipe","gaitan","hernandez","parangaturiicaro"]
    palabras=random.choice(vector1)
    guiones="_"*len(palabras)
    return palabras,guiones

def reeplazar_guiones(palabras,guiones,simbolo):
    #cuantas veces aparece en la cadena original
    cantidad=palabras.count(simbolo)
    inicio=0
    for i in range(cantidad):
        #esta buscando segun la palabra original y la esta remplazando
        pos=palabras.find(simbolo,inicio)
        guiones=guiones[:pos]+simbolo+guiones[pos+1:]
        inicio=pos+1
        return guiones

def ahorcado(palabras,guiones,simbolo):
    print(f'Hola, tendras que adivinar la palabra secreta \
          recurda que tienes 5 intentos para jugar\
          !Buena Suerte¡\n\
          \n recieselecciona una letra por favor: ')
    import random
    intentos=0
    vector1=["h",'jhoan',"felipe","gaitan","hernandez","parangaturiicaro"]
    leer_por_teclado=input("escrba una letra ")
    print (len(vector1))
    while guiones != palabras and intentos <= 4:
        print(palabras,guiones)
        if leer_por_teclado in vector1:
         for   i in vector1:
            if leer_por_teclado in i:
                 print(f" {leer_por_teclado} esta en el indice {vector1.index(i)} de la lista")
                 intentos=intentos+1
                 while intentos == 5:
                     vector1.pop(5)
                     vector1.pop(4)
                     vector1.pop(3)
                     vector1.pop(2)
                     vector1.pop(1)
                     vector1.pop(0)
                     break
        else:
            intentos=intentos+1
    print("vuelva otra vez")



def main():
    ahorcado()
    
if __name__=='__main__':
    main()"""


