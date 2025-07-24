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
