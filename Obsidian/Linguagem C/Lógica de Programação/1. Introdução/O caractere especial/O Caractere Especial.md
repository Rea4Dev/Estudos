Utilizamos o caractere especial  \\ em duas ocasiões:
1. Quando queremos usar um símbolo apenas como seu caractere, ou seja, retirar a especialidade de um símbolo.
2. Quando queremos representar um caractere que, de outro modo, seria difícil ou quase impossível de representar.

## 1
O primeiro caso pode ser verificado ao tentar executar o seguinte código:
```c
printf(“Hoje está um “lindo” dia.”);
```
Este código teria um erro de compilação, pois consideraria as aspas que eram para ser simples caracteres como um delimitador.
Para evitar este erro, seria necessário utilizar o caractere especial \ que retiraria sua especialidade e a transformaria num simples caractere.
```c
printf(“Hoje está um \”lindo\” dia.”);
```

## 2
Um exemplo que temos utilizado até agora foi o \n, para fazer a quebra de linha.

# Lista
Segue abaixo a lista completa das representações que podem ser feitas utilizando o caractere especial \\ :
![[Pasted image 20241020125504.png]]


