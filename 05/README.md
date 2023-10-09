SSC0801 - Laboratório de Introdução à Ciência de Computação I
EX05 – RunCodes.ICMC – SSC0801 – VALENDO NOTA - Programa com Strings (Criptografia) # V01
Disciplina: SSC0801 - Laboratório de Introdução à Ciência de Computação I (F.Osório)

O ALUNO DEVERÁ programar todas as funções “a mão”, usando apenas os comandos básicos da
linguagem (For, While, If, funções matemáticas básicas (buil-in), e funções criadas por você mesmo,
que podem ser baseados nos exemplos e códigos vistos em aula).
O único pacote que pode ser usado é o MATH (padrão pré-instalado no Python): import math
Como deve ser o programa PYTHON para Criptografia (codificar e decodificar) textos (strings):
1. Leia um valor numérico inteiro digitado pelo usuário (entrada do teclado, ou, caso de teste).
Este valor deve ser:
1 => Indica que queremos fazer a CRIPTOGRAFIA (Codificação do Texto)
2 => Indica que queremos fazer a DESCRIPTOGRAFIA (Decodificação do Texto)
2. Leia um texto na forma de uma string digitada pelo usuário ((entrada do teclado, ou, caso de
teste). Esta string será usada como entrada para o algoritmo de codificação ou de decodificação,
conforme selecionado pela primeira entrada digitada (1 – Codifica, 2 – Decodifica).
Por exemplo: “Hello world” (esse seria o texto a ser criptografado.
3. Leia um texto com a “SENHA” do usuário, que é composta de uma string de entrada (digitada)
com 6 caracteres representando dígitos (“000000” a “999999” como senha). A senha pode ter
apenas dígitos na forma de texto, sendo que a senha sempre deverá ser composta por 6 (SEIS)
caracteres com dígitos entre 0 e 9. Esta senha serve tanto para codificar como para decodificar o
texto.
4. Codificação: Vamos usar uma codificação “inspirada na Cifra de César” (vista em aula), porém os
caracteres serão somados com o código dos caracteres da senha MENOS 48 (este é o código de
Zero, ou seja, ORD(“0”) é 48. Usar os dígitos da senha de modo circular, por exemplo: (Use os
códigos obtidos pelas funções “ORD” e “CHR”, como foi visto em aula)
> De modo circular ficará algo mais ou menos assim... com os devidos “ord” e “chr”
Texto [0] + Senha [0] – 48; Texto [6] + Senha [0] – 48; (Texto[6] volta ao Senha[0])
Texto [1] + Senha [1] – 48; Texto [7] + Senha [1] – 48;
Texto [2] + Senha [2] – 48; Texto [8] + Senha [2] – 48;
Texto [3] + Senha [3] – 48; Texto [9] + Senha [3] – 48;
Texto [4] + Senha [4] – 48; Texto [10] + Senha [4] – 48;
Texto [5] + Senha [5] – 48; Texto [11] + Senha [5] – 48; ... Texto[12] + Senha[0] - 48 ... :^)
Esta codificação é MUITO mais difícil de ser quebrada, inclusive porque depende da senha “secreta”
Note que se a senha for “111111” estaremos reproduzindo a Cifra de César (soma +1 no código).
Pois, o “1” – 48 resulta em 1 (valor inteiro UM), que será somado ao caractere do texto original.
Sabendo que o ord(“1”) é 49, logo 49-48 = 1. Somando 1 em cada caractere, temos a Cifra de
César mais simples, que pega a letra seguinte. 
5. Decodificação: Vamos usar o processo inverso da codificação, ou seja, subtrai de modo circular os
caracteres da senha dos caracteres do texto codificado, obtendo o texto original. Exemplo:
Texto [0] - Senha [0] - 48; Texto [6] - Senha [0] - 48; (Texto[6] volta ao Senha[0])
Texto [1] - Senha [1] - 48; Texto [7] - Senha [1] - 48;
Texto [2] - Senha [2] - 48; Texto [8] - Senha [2] - 48;
Texto [3] - Senha [3] - 48; Texto [9] - Senha [3] - 48;
Texto [4] - Senha [4] - 48; Texto [10] - Senha [4] - 48;
Texto [5] - Senha [5] - 48; Texto [11] - Senha [5] - 48; ... Texto[12] - Senha[0] – 48 ... :^)
6. Exibir na tela o texto final, seja codificado ou decodificado, conforme a opção do usuário.
NOTAS:
(i) Os primeiros casos de teste serão feitos usando o exemplo acima (igual ao exemplo):
 1
 HELLO WORLD
 111111
 IFMMP!XPSME
 2
 IFMMP!XPSME
 111111
 HELLO WORLD
 Podem ser usados outros dados de entrada (texto e senha), em alguns dos casos de teste.
(ii) Os programas devem OBRIGATORIAMENTE implementar pelo menos 2 funções, com o “DEF” do python,
 conforme foi estudado em aula. Uma função de codificação e uma função de decodificação.
Bom trabalho!