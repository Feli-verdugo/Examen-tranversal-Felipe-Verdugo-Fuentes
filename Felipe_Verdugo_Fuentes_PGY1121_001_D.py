import numpy as np

import random

import time

from os import system

def limpiar():
    system("cls")

limpiar()

tick = True

timed = 2.5

timed_1 = 1

global validar_1

validar_1 = True

entradas = 0

m = 0

global total_ganado
global total_plat
global total_silver
global total_gold
global cont_gold
global cont_platino
global cont_silver
global total_cont

total_cont= 0
total_ganado = 0 

cont_platino = 0
cont_gold = 0
cont_silver = 0

total_plat = 0
total_gold = 0
total_silver = 0




matriz_entrada= np.zeros((10,10),dtype=object)

def precio_entrada():
    print("\n  Hay 3 tiers para las entradas")
    print("-----------------------------------")
    print("\n [Platinum] (Desde los asientos 1 al 2)")
    print("      Valor: $ 120.000\n")
    print("-----------------------------------")
    print("\n [Gold] (Desde los asientos 21 al 50)")
    print("      Valor: $ 80.000\n")
    print("-----------------------------------")
    print("\n [Silver] (Desde los asientos 51 al 100)")
    print("      Valor: $ 50.000\n")
    
    
    
def mostrar_asientos():
    print("\n<< Estado actual de las entradas >>\n")
    for i in range(len(matriz_entrada)):
        for j in range(len(matriz_entrada[i])):
            if matriz_entrada[i][j] == 0:
                print(i * 10 + j + 1, end='\t')
            else:
                print('x', end='\t')
        print("\n")



def comprar_entrada():
    global total_plat
    global total_silver
    global total_gold
    global cont_gold
    global cont_platino
    global cont_silver
    global validar_1
    global rut
    validar_1 = True
    mostrar_asientos()
    precio_entrada()
    
    while validar_1 == True:
        cant_entradas = int(input("Indique cuantas entradas piensa comprar (Solo pueden ser maximo 3):\n>> "))
        if cant_entradas < 1 or cant_entradas > 3:
            print(" ERROR! Por favor indique una cantidad valida")
        elif cant_entradas >= 1 or cant_entradas <= 3:
            print(f"\n Usted a elegido comprar {cant_entradas} entrada/s \n")
            time.sleep(timed_1)
            validar_1 = False
            break
        
    for m in range(cant_entradas):
        
        print(f"\nEntrada numero: {m+1} \n")
        m += 1
        entradas = int(input("\nPor favor, eliga el asiento a comprar:\n>> "))
        if entradas >=1 and entradas <=20:
            total_plat+=120000
            cont_platino+=1 
        elif entradas >=21 and entradas <=50:
            total_gold+=80000
            cont_gold+=1   
        elif entradas >=51 and entradas <=100:
            total_silver+=50000
            cont_silver+=1
        
        if entradas < 1 or entradas > 100:
            print("\nEse asiento no existe !")
            return
    
        if matriz_entrada[(entradas - 1) // 10][(entradas - 1) % 10] != 0:
            
            print("\nEl asiento ya esta tomado :c")
            
        else:
            print("\nSus entradas han sido compradas exitosamente ;D")
                     
            rut = input("\nIngrese el RUT del asistente para poder registrarlo al sistema (sin puntos o guiones):\n>> ")
            matriz_entrada[(entradas - 1) // 10][(entradas - 1) % 10] = rut
    print("\n Procesando datos, por favor espere....\n")
    time.sleep(timed)
    limpiar()

def lista_asistentes():
    asistentes = []
    for i in range(len(matriz_entrada)):
        for j in range(len(matriz_entrada[i])):
            if matriz_entrada[i][j] != 0:
                asistentes.append(matriz_entrada[i][j])
    
    asistentes.sort()
    print("\nLista de asistentes:")
    for asistente in asistentes:
        print(asistente)


def total_ganancias():
    total_ganado = total_plat+total_gold+total_silver
    total_cont = cont_gold+ cont_platino + cont_silver
    print("\n>------------------Ganancias totales------------------<\n")
    print(f"< Platino > [{cont_platino} entradas vendidas] , total ganancia: $ {total_plat} \n")
    print("--------------------------------------------------------------\n")
    print(f"< Gold > [{cont_gold} entradas vendidas] , total ganancia: $ {total_gold} \n")
    print("--------------------------------------------------------------\n")
    print(f"< Silver > [{cont_silver} entradas vendidas] , total ganancia: $ {total_silver} \n")
    print("--------------------------------------------------------------\n")
    print("                Total de entradas vendidas"   )
    print(f"                      >> {total_cont} <<")
    print("--------------------------------------------------------------\n")
    print("                    Total remunerado")
    print(f"                    <  $ {total_ganado}  >")
    print("\n--------------------------------------------------------------\n")



def menu():
    print("\n--------Menu del sistema--------\n")
    print("\n  ¿Que opcion desea elegir?     \n")
    print(" 1) Comprar entradas")
    print(" 2) Revisar ubicaciones disponibles")
    print(" 3) Listado de asistentes")
    print(" 4) Ganancias totales")
    print("\n         5) Salir      \n")
    
    

while tick == True:
    menu()
    
    opcion = int(input("Elija una opcion:\n>> "))
    
    if opcion == 1:
        comprar_entrada()
    elif opcion == 2:
        mostrar_asientos()
    elif opcion == 3:
        lista_asistentes()
    elif opcion == 4:
        total_ganancias()
    elif opcion == 5:
        break
    else:
        print("\n<< Error, intente otra vez >>")

print("\n Gracias por usar nuestro servicio, vuelva prontooo\n")

print("Hasta la Proximaaaa!")

print("\n Felipe Ignacio Verdugo Fuentes  (Aka: Fulaxo) \n\n Fecha: 10/07/2023")


