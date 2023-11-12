SSC0801 - Laboratório de Introdução à Ciência de Computação I
EX06 – RunCodes.ICMC – SSC0801 – VALENDO NOTA - Programa DESHTMLIZADOR # V01
Faça um programa que usa arquivos textos (HTML) lidos do disco, e usando funções criadas por você
para realizar estas tarefas, ELIMINA os TAGS HTML do arquivo, seguindo a descrição abaixo:
O programa NÃO deve usar "biblioteca externas" (não padrão) como é o caso, por exemplo, da
“biblioteca/módulo” pycrypto (ou qualquer outro modulo similar). O RunCodes não usa/aceita
bibliotecas ou funções específicas que realizem diretamente a criptografia de textos, portanto, não aceita
funções que não sejam “padrão básico” do Python.
O ALUNO DEVERÁ programar todas as funções “a mão”, usando apenas os comandos básicos da
linguagem (For, While, If, funções matemáticas básicas (buil-in), e funções criadas por você mesmo,
que podem ser baseados nos exemplos e códigos vistos em aula).
O único pacote que pode ser usado é o MATH (padrão pré-instalado no Python): import math
Como deve ser o programa PYTHON para Criptografia (codificar e decodificar) textos (strings):
1. Leia o nome do arquivo texto (HTML) que vai ser lido do disco. Ler de entrada padrão (teclado) o
nome do arquivo, por exemplo “arq.html”, e depois abrir este arquivo em modo texto para leitura.
2. Para cada linha de texto lida do arquivo, elimite os “tags” de HTML, ou seja, ignore o texto entre o
“<” (sinal de menor) até o próximo “>” (sinal de maior). As “tags” do HTML são sempre delimitadas
pelo “<” e “>”, como por exemplo: <body> <pre> </pre> </body>, portanto se você ignorar o
texto entre < e >, vai ficar apenas com o “texto puro” sem os “tags” (marcações) do HTML.
3. Todo o texto que estiver “fora” das “tags”, ou seja, fora do “<” até o “>” é considerado um “texto
puro” e deve gerar uma saída no programa. Por exemplo: <b>TEXTO</b> deve gerar como saída
“TEXTO”. A saída deve ser escrita na tela e também em um arquivo texto em disco denominado
de “out.txt”. Note que o mesmo “TEXTO” é escrito na tela (print) e no arquivo em disco.
4. Se a linha não contiver texto, não precisa pular uma nova linha. Se a linha tiver algum texto
(“texto puro”), é bom ao terminar a linha pular para a próxima linha.
5. O programa deve ser feito com o uso de funções (modular) e deve ter pelo menos uma função
que recebe a linha completa (HTML) e devolve uma linha sem os “tags” do HTML (texto puro).
6. O programa deve repetir esta DESHTMLIZAÇÃO até encontrar o final do arquivo de entrada (fim
de arquivo). Fechando os arquivos de entrada e de saída e terminando a execução.
 Os programas devem OBRIGATORIAMENTE implementar pelo menos 1 funções, com o “DEF” do python,
 conforme foi estudado em aula e indicado acima.
Veja a seguir alguns exemplos de DESHTMLIZAÇÃO...
Entrada (arquivo lido):
<HTML><BODY>HELLO WORLD</BODY></HTML>
Saída (na tela e no disco):
HELLO WORLD
===
Entrada (arquivo lido):
<HTML>
<HEAD>
<TITLE>PAGINA EXEMPLO</TITLE>
</HEAD>
<BODY>
<B>HELLO WORLD!</B><BR>
PYTHON IS GREAT!<BR>
</BODY>
</HTML>
Saída (na tela e no disco):
PAGINA EXEMPLO
HELLO WORLD!
PYTHON IS GREAT!
===
Bom trabalho!