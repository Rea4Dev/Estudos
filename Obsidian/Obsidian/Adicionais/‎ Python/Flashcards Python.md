# Como utilizar?

Sempre após estudarmos e anotarmos algo, iremos criar Flashcards das coisas que acharmos importante e pertinente a ser lembrado em longo prazo. Devemos ter cuidado, pois é uma linha tênue entre a negligência e o exagero.

Com o Flashcard feito, iremos diariamente resolver as questões. Sem muita culpa, esforço ou tempo, o intuito não é acertar, e sim gravar!

Toda vez que reparar que errou muito um série de cards específicos a um assunto, após responder os flashcards, passe lá e de uma lida!

## Sugestão pessoal

Não crie manualmente Flashcards, isso é muito trabalhoso e custoso em tempo. Ao invés disso, pegue toda a página e mande para o GPT, peça a ele que faça os Flashcards no modelo que você utiliza.

Geralmente o GPT irá fazer um ótimo trabalho. E caso uma coisa ou outra escape... bem, não há problemas, até porque *flashcards não são apenas inicialmente criados, é um processo eterno a cada vez que algo se prova ser digno de estar nele*!

Então é isso, jogar para o GPT e ter a maturidade de futuramente sempre que algo deste tema falhar a memória, virar Flashcard.

---

# Python
## Experienciados
#Python/Experienciados

P1) Você se lembra como declarar funções com *parâmetros opcionais*?
^
```Python
def devolver_frases(saudacao, humilhacao=" "):
	if saudacao == "sim":
		print("\n oi ", end="")
	if humilhacao == "sim":
	    print("bobão")

devolver_frases("sim")
devolver_frases("sim", "sim")
```
<!--SR:!2025-07-10,3,261-->
%

P2) Você se lembra como escrevemos em arquivos?
^
```Python
import os

pasta_atual = os.path.dirname(__file__)
arquivo = os.path.join(pasta_atual, 'exemplo.md')

with open(arquivo, "w") as file:
    file.write("Olá")
```
<!--SR:!2025-07-12,5,241-->
%

P3) Você se lembra da melhor maneira de trabalhar com *pasta atual*, *pasta pai* e *arquivo*?
^
```Python
import os

PASTA_ATUAL = os.path.dirname(__file__)
PASTA_PAI = os.path.dirname(PASTA_ATUAL)
ARQV = os.path.join(PASTA_DATA, 'arquivo.txt')
```
<!--SR:!2025-07-08,1,202-->
%

---
