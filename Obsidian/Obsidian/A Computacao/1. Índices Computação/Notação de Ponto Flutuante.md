---
data_criacao: 28-08-2025
flashcards: Não feito
revisão: Não feita
---

---

# Notação de Ponto Flutuante
A notação de ponto flutuante é muito usada na computação, como por exemplo em cálculos matemáticos de precisão, em processos de renderização de imagem em jogos 3D (que demandam bastante deste tipo de representação e de aritimética de ponto flutuante).

**Mantissa**:
	Quantidade de dígitos na parte significativa do número.

**Base**:
	Conjunto de símbolos (ou algarismo)

**Expoente**:
	Valor inteiro dentro de uma intervalo \[min, max]

## Exemplo
Pense em um dispositivo embarcado, com memória e processamento limitados, que opera na *base 10* com *4 dígitos na mantissa* e expoente assumindo valores {-3, -2, -1, 0, 1, 2, 3}. 

### -17,945
Digamos que queremos representar o número -17,945 nele.

![[Pasted image 20250828193928.png | center | 400]]

Ocorre um truncamento! O dígito "5", por exceder a quantidade de quatro especificada, é descartado e desconsiderado.

### Maior e menor número
![[Pasted image 20250828192230.png | center | 400]]

---
# Ponto Flutuante Binário

![[Pasted image 20250828193554.png]]