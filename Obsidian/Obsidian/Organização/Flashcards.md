---
Principal: Sim
---
---
# Python
#flashcards/Python

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
%

P3) Você se lembra da melhor maneira de trabalhar com *pasta atual*, *pasta pai* e *arquivo*?
^
```Python
import os

PASTA_ATUAL = os.path.dirname(__file__)
PASTA_PAI = os.path.dirname(PASTA_ATUAL)
ARQV = os.path.join(PASTA_DATA, 'arquivo.txt')
```
%