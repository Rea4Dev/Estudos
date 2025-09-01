---
data_criacao: 28-08-2025
flashcards: Não feito
revisão: Não feita
---

---

# Operações Lógicas e Tabela Verdade

“Ela (a Lógica) lhe dará clareza de pensamento, a habilidade de ver seu caminho através de um quebra-cabeça, o hábito de arranjar suas ideias numa forma acessível e ordenada e, mais valioso que tudo, o poder de detectar falácias e despedaçar os argumentos ilógicos e inconsistentes que você encontrará tão facilmente nos livros, jornais, na linguagem cotidiana e mesmo nos sermões e que tão facilmente enganam aqueles que nunca tiveram o trabalho de instruir-se nesta fascinante arte”
>Lewis Carrol.

## Definição

Lógica, segundo dicionário Merriam-Webster:
- “Uma ciência que lida com os princípios e critérios de validade da inferência e demonstração: a ciência dos princípios formais do raciocínio” 
- “O arranjo dos elementos do circuito (como em um computador) necessário para o cálculo”

## Origem

- A lógica proposicional deriva da filosofia na Grécia antiga com Sócrates e Aristóteles em particular.
- A lógica booleana aparece com o trabalho do matemático inglês George Boole (1815-1864)
- Apenas na década de 30 do século XX, Claude Shannon identifica a importância da álgebra booleana para os circuitos.

![[Pasted image 20250828224352.png | center]]

---
# Lógica Proposicional

**Proposição**: sentença que é falsa ou verdadeira.

- Vinte é maior que cem ❌
- Azul é um número ❌
- Vinte é menor que cem ✅
- Azul é uma cor ✅
- Ela é alta <span style="color:orange;">(não é proposição)</span>

## Operadores

### Conjunção ("e"  "^")

Para uma proposição composta por dois elementos relacionados por conjunção, como no caso abaixo de "João é professor e joga futebol", apenas teremos verdade como resposta quando ambas isoladamente forem verdadeiras.
<center><strong>A, B</strong>: elementos ou fatores</center>
![[Pasted image 20250828225213.png | center | 300]]
![[Pasted image 20250828225547.png | center | 100]]

### Disjunção ("ou"  "v")

Para uma proposição composta por dois elementos relacionados por disjunção, como no caso abaixo de "João é professor ou joga futebol", teremos verdade sempre que uma das duas (ou as duas) forem verdade.

![[Pasted image 20250828230141.png | center | 300]]

### Negação

Para uma proposição composta por dois elementos relacionados por disjunção, como no caso abaixo de "João é professor ou joga futebol", teremos o resultado negando o estado anterior do elemento.

![[Pasted image 20250828230331.png | center | 300]]

### Implicação

Na implicação verificamos a veracidade da implicação. Respeitamos que só podemos verificar a implicação como falsa se o primeiro elemento for verificado como verdadeiro e o consequente como falso, pois quando não o conseguimos verificar então assumimos que a implicação é verdadeira.

![[Pasted image 20250828230844.png | center | 400]]

### Bicondição

Na bicondição, fazemos a implicação de A->B e armazenamos o resultado. Depois de B->A e armazenamos o resultado.
Aplicamos "e" em ambos resultados no final.

`Dica`: Sempre que os valores verdade

![[Pasted image 20250828231335.png | center | 400]]

---

# Leis

## Tautologia, Lei de Morgan

~(A V B) é equivalente a (~A ^ ~B)

![[Pasted image 20250828232022.png]]

## Contradição

![[Pasted image 20250828232447.png]]