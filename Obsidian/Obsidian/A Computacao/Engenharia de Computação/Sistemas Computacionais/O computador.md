---
data_criacao: 29-07-2025
flashcards: Não feito
revisão: Não feita
---
# O computador

## Definição

A **ACM (Association for Computing Machinery)** define “computador” no contexto técnico, especialmente ao abordar a história da computação.

A definição mais relevante e respeitada vem do *"IEEE/ACM Software Engineering Body of Knowledge (SWEBOK)"* e também de obras publicadas sob a curadoria da ACM e IEEE, como no *IEEE Annals of the History of Computing*.

Apesar de a ACM _não ter uma única_ definição canônica de "computador", ela frequentemente adota a visão clássica formalizada por **Alan Turing** e materializada pelo modelo **von Neumann**.

> [!Definição técnica aceita pela ACM (e comunidade científica)]
> Um computador é uma *máquina* capaz de executar *algoritmos* de forma *automática e controlada* por meio de *instruções programáveis*, geralmente **por armazenar e manipular dados segundo um modelo formal de computação**.
>  
> <small>Fonte: ACM/IEEE Curriculum Guidelines for Undergraduate Degree Programs in Computer Science (CS2013)</small>

Esse conceito está associado ao que chamamos de `máquina de propósito geral`, geralmente implementando a arquitetura de **von Neumann**, cujos componentes são:

- Unidade de controle
- Unidade lógica e aritmética
- Memória
- Dispositivos de entrada e saída

## Estrutura Hierárquica dos Computadores

O computador é projetado seguindo uma estrutura hierárquica, em que seus componentes são organizados em **sistemas e subsistemas** distribuídos em **diferentes níveis de abstração**. Cada nível executa funções específicas e se comunica com os níveis adjacentes por meio de **interfaces bem definidas**.

Essa organização permite isolar a complexidade de cada camada e facilita o estudo, o projeto e a manutenção de sistemas computacionais. Do ponto de vista didático, essa hierarquia possibilita uma abordagem progressiva, **do mais abstrato ao mais concreto**, favorecendo a compreensão fase a fase.

### Exemplo clássico de níveis hierárquicos:

1. Nível do usuário/programador (linguagens de alto nível)
2. Nível de sistema (sistema operacional e compiladores)
3. Nível da linguagem de máquina (instruções do processador)
4. Nível do microprograma (controle das instruções via firmware)
5. Nível digital lógico (circuitos digitais, portas lógicas)
6. Nível eletrônico (componentes físicos como transistores)

> Essa estrutura foi sistematizada por autores como Andrew Tanenbaum e Carl Hamacher, e reflete a abordagem aceita em currículos orientados pela **ACM/IEEE**.
