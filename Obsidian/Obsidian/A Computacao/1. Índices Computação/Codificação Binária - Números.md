---
data_criacao: 25-08-2025
flashcards: Não feito
revisão: Não feita
---

---

# Codificação Binária sem Sinal
Em $n$ bits **sem sinal**, os valores vão de:
$0$ <small>até</small> $2^{{(n-1)}}$  
<small style="font-size:90%">(este "-1" por conta de índice, pois começamos a contar do zero).</small>

> [!Importante]  MSB - Most Significant Bit
> Significa *bit mais significativo*:
> - é o bit mais a esquerda
> - ele é o bit de maior peso $-2^{\,{(n-1)}}$ 

# Codificação Binária com Sinal

## Para inteiros

Em computadores, os **números negativos são representados em binário** através de técnicas chamadas de **complemento**. Os métodos principais são:

- [[Sinal e magnitude (bit de sinal)]]
- [[Complemento de Um (C1)]]
- [[Complemento de Dois (C2)]]

Essas representações (mais a C2, na verdade) são essenciais para permitir **operações aritméticas binárias** (como soma e subtração) entre números com sinal, mantendo a lógica de circuitos simples e eficiente.

## Para ponto flutuante (float)

Em representações **ponto flutuante** (como o padrão [[IEEE 754]]), o número é separado em três partes: *sinal*, *expoente* e *mantissa* (ou fração).
O **expoente** é armazenado em binário, mas **não usa sinal direto**. Em vez disso, adota-se uma técnica chamada:

- [[Notação por excesso]]