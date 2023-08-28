#bibliotecas úteis
import math

#funções úteis
def negativeChecker(entrada):
    if(entrada < 0): return True
    else: return False

def calcArea(raio):
    area = math.pi * raio ** 2
    return area

def calcPerimetro(raio):
    perimetro = 2 * math.pi * raio
    return perimetro

def wayOfKings(raio):
    if(negativeChecker(raio)):
        print("Nao existe circunferencia de raio negativo!")
        return 0
    else:
        area = calcArea(raio)
        perimetro = calcPerimetro(raio)        
        print('{0:.2f}'.format(area))
        print('{0:.2f}'.format(perimetro))
        return 0

#Entrada e programa
raio = float(input())
wayOfKings(raio)



