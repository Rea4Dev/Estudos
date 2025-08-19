---
data_criacao: 18-08-2025
flashcards: Não feito
revisão: Não feita
---
Permite criar Bancos de Dados, Tabelas ou Exibições (views).

# Criando um novo Banco de Dados

De forma prática, um Banco de Dados Relacional "é um lugar onde conseguimos guardar informações/dados dentro de tabelas".

Para criar um Banco de Dados, usamos o seguinte comando:
```SQL
CREATE DATABASE WebSIT;
```

# Criando uma nova Tabela

Uma tabela tem como objetivo armazenar informações dispostas em diferentes colunas. Cada uma das colunas dessa tabela será um tipo específico.
```SQL
CREATE TABLE tabela (Coluna1 TIPO1, Coluna2 TIPO2);
```

Os tipos são:
- ``Int``
- ``Decimal(M, D)``
- ``VARCHAR(N)``
- ``DATE``
