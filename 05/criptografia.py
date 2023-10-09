#EX05 – SSC0801 – Programa com Strings (Criptografia)

def cript(texto, senha, tamTexto):
    saida = []
    for i in range(0, tamTexto):
        charIndex = ord(texto[i]) + ord(senha[i%6]) - 48
        newChar = chr(charIndex)
        saida.append(newChar)

    return ''.join(saida)

def decript(texto, senha, tamTexto):
    saida = []
    for i in range(0, tamTexto):
        charIndex = ord(texto[i]) - ord(senha[i%6]) + 48
        newChar = chr(charIndex)
        saida.append(newChar)

    return ''.join(saida)

entrada = int(input())
texto = [s for s in input()]
texto.remove('\r')
senha = [s for s in input()]
tamTexto = len(texto)
if(entrada == 1): print(cript(texto, senha, tamTexto))
else: print(decript(texto, senha, tamTexto))