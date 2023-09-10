Faça um programa sequencial de cálculo estatístico seguindo a descrição abaixo:

    O programa deve usar a "biblioteca statistics"
    Use o comando: import statistics ou import statistic as stat

    Defina dois conjuntos de dados, por exemplo: (inicialmente com ZERO)

    x = [0.0, 0.0, 0.0, 0.0, 0.0] 
    y = [0.0, 0.0, 0.0, 0.0, 0.0] 



    Agora leia do teclado 5 dados "float" para colocar no lugar dos 5 valores do primeiro conjunto de dado, "x" no exemplo acima
    A atribuição funciona assim, por exemplo:

      x[0] = 1.0; x[1] = 2.0;  ... ; x[4] = 5.0   



    Faça a leitura do teclado com a função "input" , convertendo para "float" e armazenando na lista de dados

    Agora leia do teclado mais 5 dados (float) para colocar no lugar dos 5 valores do segundo conjunto de dado, "y" no exemplo acima

    Usando as funcões estatísticas da biblioteca importada... USE O HELP e GOOGLE para ver detalhes da "statistics"
    Exiba os seguintes resultados na tela (são 7 prints ao total) , sendo todos valores com 2 casas após a vírgula:
    "print" de 3 valores (com somente 2 casas após a vírgula) referentes aos dados do primeiro conjunto "x"
        Media (mean)
        Mediana (median)
        Desvio Padrão (stdev)
        "print" de 3 valores (com somente 2 casas após a vírgula) referentes aos dados do primeiro conjunto "y"
        Media (mean)
        Mediana (median)
        Desvio Padrão (stdev)
        "print" da correlação entre os 2 conjuntos de dados "x" e "y"
        Correlação (correlation)

        ATENÇÃO: import statistics: precisa da versao python 3.10 ou superior para ter a funcao "correlation"!
        O RUNCODES usa a versão python 3.11, logo, funciona. Se no seu micro a versão for inferior a 3.10, não vai funcionar o correlation.

        Bom trabalho! 