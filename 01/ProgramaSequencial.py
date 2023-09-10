#importando bibliotecas
import statistics

#funções úteis
def checker(entrada):
    try:
        entrada = float(entrada)
        return False
    except:
        print("Relembrando, precisamos de números reais! ;)")
        return True

def saida(vetor):
    for i in range(3):
        print('{0:.2f}'.format(vetor[i]))
    return 0

#vetores vazios
vetor1 = [0.0, 0.0, 0.0, 0.0, 0.0]
vetor2 = [0.0, 0.0, 0.0, 0.0, 0.0]

#loops para entrada de números
for i in range(0, 5):
    numero = input()
    while(checker(numero)):
        numero = input()
    vetor1[i] = float(numero)

for i in range(0, 5):
    numero = input()
    while(checker(numero)):
        numero = input()
    vetor2[i] = float(numero)

statsVetor1 = [round(statistics.mean(vetor1), 2), round(statistics.median(vetor1), 2), round(statistics.stdev(vetor1), 2)]
statsVetor2 = [round(statistics.mean(vetor2), 2), round(statistics.median(vetor2), 2), round(statistics.stdev(vetor2), 2)]
correlation = round(statistics.correlation(vetor1, vetor2), 2)

saida(statsVetor1)
saida(statsVetor2)
print('{0:.2f}'.format(correlation))
