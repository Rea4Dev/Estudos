### 🔹 **Relacionamento N:N (Muitos para Muitos)**

O relacionamento **N:N (Muitos para Muitos)** ocorre quando **uma instância** da entidade A pode estar associada a **várias instâncias** da entidade B, e **vice-versa**.
![[Pasted image 20250223152400.png]]

---

## 🔺 **Características**

1. **Multiplicidade**
    - Uma instância de A pode se relacionar com **múltiplas** instâncias de B.
    - Uma instância de B pode se relacionar com **múltiplas** instâncias de A.

2. **Intermediário** (Tabela Associativa)
    - No modelo relacional, não podemos representar **N:N** diretamente.
    - Criamos uma **tabela intermediária** que transforma um relacionamento **N:N** em **dois relacionamentos 1:N**.

---

## 🔺 **Implementação no Banco de Dados**

- Criamos uma **tabela intermediária** contendo **chaves estrangeiras** das entidades envolvidas.
- Essas chaves estrangeiras juntas formam uma **chave primária composta** para evitar repetições.

🔹 **Exemplo: Relacionamento "Aluno" e "Disciplina"**

### 🗂 **Entidade Aluno**

|ID_Aluno|Nome|
|---|---|
|1|João|
|2|Maria|
|3|Pedro|

### 🗂 **Entidade Disciplina**

|ID_Disciplina|Nome|
|---|---|
|101|Matemática|
|102|Física|
|103|Programação|

### 🗂 **Tabela Intermediária "Aluno_Disciplina"**

|ID_Aluno|ID_Disciplina|
|---|---|
|1|101|
|1|103|
|2|101|
|2|102|
|3|103|

- O aluno **João** está matriculado em **Matemática (101)** e **Programação (103)**.
- O aluno **Maria** está matriculado em **Matemática (101)** e **Física (102)**.
- O aluno **Pedro** está matriculado apenas em **Programação (103)**.

---

## 🔺 **Leitura do Relacionamento**

Sempre seguimos a lógica de fixar uma **entidade A** e ver quantas instâncias da **entidade B** ela pode ter, e vice-versa.

> 🔎 **Para (N:N) (N:N)** lê-se, então:
> 
> - Todo _Aluno_ pode estar associado a **múltiplas** _Disciplinas_.
> - Toda _Disciplina_ pode estar associada a **múltiplos** _Alunos_.

---

## **Conclusão**

O relacionamento **N:N** é um dos mais comuns em bancos de dados relacionais, mas requer uma **tabela intermediária** para ser corretamente modelado. Ele é fundamental para representar cenários onde várias entidades precisam se relacionar com múltiplas instâncias umas das outras. 🚀