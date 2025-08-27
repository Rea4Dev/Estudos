---
data_criacao: 26-08-2025
flashcards: Feito
revisão: Não feita
---

---

# 🔹 Complemento de Dois (C2)

- **Ideia**: método padrão para representar números inteiros com sinal na computação.
- **Motivo**: elimina o problema do "zero duplo" e facilita operações aritméticas em hardware.
- **Como**:  com base na quantidade de bits, a metade superior do espaço total que teria (quando MSB = 1) é reinterpretada somente para números negativos.

> [!Importante]  MSB - Most Significant Bit
> Em números binários com sinal (C2), o **MSB (bit mais significativo)** indica o **sinal**.
> 
> - `0` → número **positivo**
>     
> - `1` → número **negativo**

> [!Warning] Importante: o intervalo depende da quantidade de bits!
> Em $n$ bits **complemento de dois**: valores vão de
$-2^{\,{(n-1)}}$   <small>até</small>   $+2^{\,{(n-1)}} - 1$.
>- Com **4 bits (1 nibble)** → valores possíveis: **-8 até +7**.
>- Com **8 bits (1 byte)** → valores possíveis: **-128 até +127**.
><br>Obs: O expoente "n-1" é por conta do índice e o "-1"  é por conta do zero.

## Como calcular um número negativo:

1. Representa o número positivo em binário (com **N bits**).
2. Inverte todos os bits (como no complemento de um).
3. Soma **1** ao resultado.

``Exemplo (em 4 bits)``: -3

- +3         → `0011`
- Inverte  → `1100`
- Soma 1 → `1101`

✅ Logo, **-3 em 4 bits C2 = 1101**

## Vantagens do C2

- Apenas **um zero** (`0000`).
- Operações de **soma e subtração** funcionam direto no hardware.
- Implementação simples e eficiente.

---