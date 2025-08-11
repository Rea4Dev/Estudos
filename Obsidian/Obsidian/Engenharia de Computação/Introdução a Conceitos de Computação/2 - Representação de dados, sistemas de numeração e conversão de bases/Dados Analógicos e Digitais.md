---
data_criacao: 05-08-2025
flashcards: Não feito
revisão: Não feita
---
# Dados Analógicos

## Definição

> [!Definição]  
> **Dados analógicos** são representações *contínuas* de *grandezas físicas*, *variando de forma suave e sem interrupções* dentro de um intervalo.  
> São usados *para descrever fenômenos naturais ou grandezas que mudam continuamente* ao longo do tempo.

## Características dos dados analógicos

- Representação **contínua**
- Medição de **grandezas naturais variáveis**
- Valores **intermediários infinitos** entre dois extremos
- **Susceptíveis a ruídos e distorções** do ambiente
- Dependem de dispositivos físicos para leitura e registro
## Dispositivos analógicos

Dispositivos analógicos *utilizam essa representação contínua para medir quantitativamente fenômenos da natureza*. Eles capturam variações _não discretas_, sendo capazes de representar qualquer valor dentro de um intervalo, com _precisão limitada apenas pela sensibilidade do dispositivo_.

### Exemplos de grandezas medidas por dispositivos analógicos:

- Temperatura
- Pressão
- Distância
- Som

> Um exemplo clássico de dispositivo analógico é o **voltímetro de ponteiro**, cuja agulha se move de forma contínua conforme a variação da tensão.

---

# Dados Digitais
## Definição

> [!Definição]  
> Dados digitais são representações _discretas_ de informações, normalmente codificadas em **dígitos binários** (0 e 1), adequadas ao processamento eletrônico e computacional.

## Dispositivos digitais

Dispositivos digitais operam com **valores discretos**, ou seja, *trabalham com unidades de informação bem definidas e separadas* — chamadas **dígitos**.

## Unidades de Informação
### Bit

A menor unidade de informação digital é o **bit** (_Binary digIT_), capaz de representar apenas dois estados possíveis:

- `0` — ausência de sinal, desligado, falso
- `1` — presença de sinal, ligado, verdadeiro

Essa representação binária é a base de todo o funcionamento dos computadores modernos.

### Byte

Byte (_BinarY TErm_) é a _unidade básica de armazenamento_ em memória e disco usada pelos computadores, e é formada por **8 bits**.

A *escolha* do byte como unidade padrão vem de sua *capacidade de representar 256 combinações distintas* (`2⁸`), o que o torna suficiente para codificar:

- Caracteres (como na tabela ASCII)
- Instruções básicas de máquina
- Pequenos blocos de dados

### Palavra

> [!Definição]  
> **Palavra** é uma _sequência de bytes tratada como uma unidade pelo processador_, utilizada para armazenar instruções ou dados.

O tamanho de uma palavra varia conforme a arquitetura do computador:
- Pode conter **2, 4, 6 ou 8 bytes**
- Uma palavra de 8 bytes equivale a **64 bits**
- Está diretamente ligada à **largura dos registradores e do barramento de dados** do processador

<div style="display:flex; justify-content:center;">
  <table>
    <tr>
      <th style="text-align:center;">Arquitetura</th>
      <th style="text-align:center;">Tamanho da palavra</th>
    </tr>
    <tr>
      <td style="text-align:center;">32 bits</td>
      <td style="text-align:center;">4 bytes</td>
    </tr>
    <tr>
      <td style="text-align:center;">64 bits</td>
      <td style="text-align:center;">8 bytes</td>
    </tr>
  </table>
</div>

## Características dos dados digitais

- Representação **discreta e quantizada**
- Baseado em **valores finitos e bem definidos**
- Mais **resistente a ruídos** do que sistemas analógicos
- Facilitam **armazenamento, processamento e transmissão precisa** de informações
- Fundamentados no sistema binário (bits)