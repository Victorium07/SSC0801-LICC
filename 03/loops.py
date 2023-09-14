#EX03 - Programa com Loops FOR e WHILE (Vale Nota)
# Bibliotecas úteis
import math

#funções úteis
def entradas(numeros):
    lista = []
    for items in range(0, numeros):
        lista.append(float(input()))
    return lista

def minMax(lista):
    minimo = lista[0]
    maximo = lista[0]
    contador = 0
    while(contador < len(lista)-1):
        if(minimo > lista[contador+1]):
            minimo = lista[contador+1]
        elif(maximo < lista[contador+1]):
            maximo = lista[contador+1]
        contador += 1
    return(minimo, maximo)

def amplitude(lista):
    minimo, maximo = minMax(lista)
    return maximo - minimo

def somaTotal(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma

def media(lista):
    med = somaTotal(lista)/len(lista)
    return med

def variancia(lista):
    med = media(lista)
    var = 0
    for i in lista:
        var += (i-med)**2
    var = var/len(lista)
    return var

def desvioPadrao(lista):
    dp = math.sqrt(variancia(lista))
    return dp   

def listaResultados(lista):
    listaFinal = []
    mini, maxi = minMax(lista)
    listaFinal.append(mini)
    listaFinal.append(maxi)
    listaFinal.append(amplitude(lista)) 
    listaFinal.append(somaTotal(lista))
    listaFinal.append(media(lista))
    listaFinal.append(desvioPadrao(lista))
    listaFinal.append(variancia(lista))
    return listaFinal

def Oathbringer():
    nums = int(input())
    resultados = listaResultados(entradas(nums))
    
    for i in resultados:
        print(f'{i:.3f}')

    return 0

Oathbringer()