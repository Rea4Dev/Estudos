# 📜 Manifesto de Fixação de Conteúdos — v1.0

Sistema pessoal de consolidação do conhecimento, aplicado no Obsidian.md + extensão de Flashcards.

---

## 🧠 Princípio Fundamental

> "A memória falha, o sistema corrige."

Sempre que terminar de estudar algo, **fica a seu critério** criar flashcards ou não.

O que se torna **regra inegociável** é:

> **Sempre que falhar em lembrar de algo estudado, investigue a origem dessa falha.**

---

## 🔍 Processo em caso de falha

1. **Verifique se o assunto estava registrado no Obsidian.**

   - ❌ **Não estava?**
     - Você não tinha como lembrar.
     - ➤ Registre o conteúdo agora no Obsidian.

   - ✅ **Estava?**
     - Sua memória falhou.
     - ➤ Crie um flashcard **específico** sobre a informação que falhou.

---

## 🔄 Revisão e Manutenção

A extensão de Flashcards cuidará da lógica de repetição (revisão espaçada) com base no seu desempenho. Confie nela.

---

## ⚠️ Pontos de Atenção

- Nem sempre você errará o que está esquecendo.
  - ➤ Considere revisões periódicas do conteúdo já estudado mesmo sem falhas detectadas.

- Revisão não é punição. É refinamento.
  - ➤ Relembrar é consolidar.

---

## ✍️ Atualizações Futuras

Este manifesto é um organismo vivo.
Sempre que uma melhoria for percebida, **registre e versione.**

---

> _"O conhecimento que não é revisado se apaga como traço na areia."_

# Engenharia de Computação
## Algoritmos e Programação de Computadores I
#EngComp/Algoritmos_Prog_Comp1

Comp) 11aaee ?:X:Aaa

Comp) aaee?
X^X
Raa
X%X

## Introdução a Conceitos de Computação
#Comp/EngComp/Introducao_Conceitos_Computacao

Comp1) Converta o *binário 1011* para **decimal**::A resposta é `11`.
<!--SR:!2025-09-05,11,274-->

Comp2) Converta o octal 230,4 para decimal
^
A resposta é `152,5`.
<!--SR:!2025-09-03,7,274-->
%

Comp3) Converta o hexa 4BF para decimal
^
A resposta é `1215`.
<!--SR:!2025-09-01,5,254-->
%

Comp4) Converta o 12,4 decimal para binário (três números após a vírgula)
^
A resposta é `1100,011`.
<!--SR:!2025-09-05,11,274-->
%

Comp5) Converta o 1215,53 decimal para hexadecimal (três números após a vírgula)
^
A resposta é `4BF,87A`.
<!--SR:!2025-09-05,11,270-->
%

Comp6) Converta o decimal 342,625 para octal
^
A resposta é `526,5`.
<!--SR:!2025-09-09,15,290-->
%

Comp7) Como convertemos de qualquer base Universal para Decimal?
^
Através de somatório - UDS (universal decimal somatório).
<!--SR:!2025-08-29,4,277-->
%

Comp8) Como convertemos de Decimal para qualquer base Universal?
^
Através de divisões - DUD (decimal universal divisões).
<!--SR:!2025-08-29,4,277-->
%

Comp9) Quais são as duas formas de converter bases para parte fracionaria?
^
DUD - multiplicar o fracionário pela base colhendo o inteiro
UDS - UDS
<!--SR:!2025-08-29,4,281--> 
%

Comp10) Como ler binários visualmente?:: Considerando que cada posição representa uma **potência de 2** da direita para a esquerda (2^0, 2^1, 2^2, ...).
<!--SR:!2025-08-30,4,282-->

Comp11) Descreva a ideia do complemento de 1, dê um exemplo e diga qual o problema dele
^

---

# 🔹 Complemento de Um (C1)

- **Ideia**: inverter todos os bits de um número positivo para representar o negativo.

## Exemplo em 4 bits:

- `+5` → `0101`
- `-5` em C1 → `1010` (inversão bit a bit)

>[!Warning] Problema
>Gera **duas representações para o zero** (positivo e negativo).
>- `0000` → zero positivo
>  - `1111` → zero negativo
>  
>  Isso gera ambiguidade e complica operações aritméticas.

---
<!--SR:!2025-08-31,4,284-->
%


Comp12) Descreva a ideia e o motivo do complemento de 2, diga como usá-lo, sua faixa, dê um exemplo para 4 bits e diga quais as vantagens
^
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
<!--SR:!2025-08-30,3,265-->
%

Comp13) Fale sobre o MSB::MSB significa Bit mais Significativo, ele é o bit mais a esquerda e o bit de maior peso $2^{{(n-1)}}$.<br>Em Complemento de 2, quando 1 ele indica negativo e quando 0 ele indica positivo.
<!--SR:!2025-08-30,3,265-->

## Sistemas Computacionais
#EngComp/Sistemas_Comp

Comp) 33aaee ?X:X:Ccc

EC) aaee?
X^X
Raa
X%X
