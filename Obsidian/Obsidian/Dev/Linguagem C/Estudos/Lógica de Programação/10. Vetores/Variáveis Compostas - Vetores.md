Um vetor (também vulgarmente conhecido por Array) não é mais que um conjunto de elementos consecutivos, *todos do mesmo tipo*, que podem ser acessados individualmente a partir de um único nome.

---
# Usos Principais
## Declaração
1. A declaração de um vetor com uma única dimensão obedece à seguinte sintaxe:
```C
tipo nome[quantidade]

int g[20]; /* g é um vetor com 20 números inteiros */

float renda[100]; /* renda é um vetor com 100 números reais */
```
2. A declaração e a carga inicial de um vetor podem ser realizadas sem indicar qual o número de elementos do vetor.
```C
tipo var[ ] = { valor1, valor2, …, valorn };
```
Nesse caso, o compilador vai criar um vetor com tantos elementos quantas as cargas iniciais.
## Acesso
Cada uma das posições do nosso vetor pode ser acessada através do respectivo índice colocado entre Colchetes \[ ]. Lembrando que, *índices começam com 0*.
```C
vetor[0] = 123; /* Coloque o valor 123 na primeira posição do vetor */
vetor[5] = vetor[0]*2; /* Coloque na última posição do vetor o dobro do valor do primeiro elemento. */
vetor[2] = vetor[0] + vetor[5]; /* Coloque no terceiro elemento do vetor a soma do primeiro com o último elemento. */
```
## Carga Inicial Automática de Vetores
Tal como as variáveis, os vetores quando são criados contêm valores aleatórios (lixo de memória) em cada uma das suas posições.
É possível iniciar automaticamente todos os elementos de um vetor através da seguinte sintaxe:
```C
tipo var[n] = { valor1, valor2, ..., valorn };

char vogal[5] = {'a', 'e', 'i', 'o', 'u'};
```
> [!TIP] Se um vetor for declarado com n elementos e forem colocados apenas k valores (k<n) na carga inicial do vetor, então os primeiros k elementos do vetor serão iniciados com os respectivos valores e os restantes serão iniciados com o valor ZERO.

---

# Peculiaridades

1. O *compilador não verifica se os índices utilizados em um vetor estão ou não corretos*.

<small>Um exemplo comum de erro de manipulação de um vetor com n elementos é a utilização do índice n (v[n]), que não pertence ao vetor e pode originar problemas graves, pois estaríamos alterando memória que não nos pertence (vazamento de memória?).</small>

---

2. O compilador *não verifica se os índices utilizados num vetor estão ou não corretos com a declaração do vetor*.

<small>Isto é, podemos declarar um vetor v com dimensão 3 e referenciar (erradamente) posições superiores ou inferiores, sem que o compilador indique qualquer erro.</small>

---

3. Não se pode declarar vetores sem dimensão. 

<small>Se não sabemos qual a dimensão pretendida, como poderá o compilador saber qual o espaço necessário?</small>
