#SSC0801 - EX06 - Programa DESHTMLIZADOR

def entrada():
    nome_arquivo = input().strip()
    return nome_arquivo

def ler_arquivo(_nome_arquivo):
    with open(_nome_arquivo, 'r') as arquivo:
        texto = arquivo.readlines()
    return texto

def checar_vazio(_string):
    if(len(_string) == 0):
        return True
    else: return False

def numero_tags(_string):
    num_tags = sum([1 for i in range(len(_string)) if _string[i] == '<'])
    return num_tags

def indice_proxima_tag(_string):
    for i in range(len(_string)):
        if(_string[i] == '<'):
            ind_abertura = i
        if(_string[i] == '>'):
            ind_fechamento = i
            break
    return (ind_abertura, ind_fechamento)

def remover_tags(_lista):
    for i in range(len(_lista)):
        if(checar_vazio(_lista[i])):
            continue
        numero_de_tags = numero_tags(_lista[i])
        if(numero_tags(_lista[i]) == 0):
            continue
        for j in range(numero_de_tags):
            ind_abertura, ind_fechamento = indice_proxima_tag(_lista[i])
            _lista[i] = _lista[i][:ind_abertura] + _lista[i][ind_fechamento+1:]

def escrever_arquivo(_nome_arquivo ,_lista):
    with open(_nome_arquivo, 'w') as arquivo:
        for line in _lista:
            print(line, end = '')
            arquivo.write(line)
    return 0

def remover_buracos(_lista):
    texto_puro = [i for i in _lista if i != '\n']
    return texto_puro


nome = entrada()
texto = ler_arquivo(nome)
remover_tags(texto)
texto_puro = remover_buracos(texto)
escrever_arquivo(nome, texto_puro)