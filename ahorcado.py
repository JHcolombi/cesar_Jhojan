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


