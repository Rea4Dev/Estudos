1. [[Introdução ao Banco de Dados e SQL]]
2. [[Banco de Dados Avançado]]
3. [[Introdução ao Back-End]]
4. [[Projetos para Fixação]]

---
<center><h1>Roadmap</h1></center>
### 🔹 1. Introdução ao Banco de Dados e SQL

Agora você começa a trabalhar com *bancos de dados relacionais (SQL).

✅ *O que é um Banco de Dados?

- Diferença entre **bancos relacionais** (SQL) e **NoSQL**.
- Modelagem de dados (tabelas, colunas, tipos de dados).

✅ *SQL Básico*

- `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`.
- Tipos de dados (`VARCHAR`, `INT`, `DATE`, `BOOLEAN`).
- Constraints (`PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`).

✅ *Consultas SQL Intermediárias*

- `JOIN` (INNER, LEFT, RIGHT, FULL).
- `GROUP BY` e `HAVING`.
- `ORDER BY`, `LIMIT`, `OFFSET`.
- Subqueries (`EXISTS`, `IN`, `NOT IN`).

🔧 *Ferramentas para praticar:*

- **MySQL, PostgreSQL ou SQLite** (PostgreSQL é o mais recomendado para iniciantes).
- **DBeaver ou MySQL Workbench** para visualizar os dados.
- **SQL Fiddle** ([https://sqlfiddle.com/](https://sqlfiddle.com/)) para testar consultas online.

---

### 🔹 2. Banco de Dados Avançado

✅ *Índices e Performance*

- Índices (`CREATE INDEX`, `UNIQUE`, `FULLTEXT`).
- EXPLAIN e otimização de consultas.
- Transações (`BEGIN`, `COMMIT`, `ROLLBACK`).

✅ *Stored Procedures, Triggers e Views*

- Criar funções armazenadas (`CREATE PROCEDURE`).
- Triggers para automação (`AFTER INSERT`, `BEFORE UPDATE`).
- Views para consultas otimizadas (`CREATE VIEW`).

✅ *ORMs (Object-Relational Mapping)*

- Como usar ORM para conectar código ao banco (Ex: SQLAlchemy no Python, Prisma no Node.js).

---

### 🔹 3. Introdução ao Back-End

Agora que você entende bancos de dados, precisa conectar o banco ao *Back-End.

✅ *Conceitos essenciais de API*

- O que são **APIs RESTful** e **GraphQL**.
- Métodos HTTP (`GET`, `POST`, `PUT`, `DELETE`).
- Códigos de resposta HTTP (`200 OK`, `404 Not Found`, `500 Internal Server Error`).

✅ *Criação de um Back-End Simples*
🔹 Escolha uma linguagem e framework:

- **Node.js + Express**
- **Python + FastAPI ou Flask**
- **Java + Spring Boot**
- **C# + ASP.NET**

✅ *Autenticação e Segurança*

- JWT (JSON Web Tokens).
- Criptografia de senhas com **bcrypt**.
- Proteção contra SQL Injection.

---

### 🔹 4. Projetos para Fixação

A melhor forma de aprender é *fazendo projetos.

✅ *Projeto 1: CRUD Simples*

- Criar uma API que gerencia usuários (`/users`).
- Banco de dados com tabela de usuários (`id, nome, email, senha`).
- Endpoints para `GET`, `POST`, `PUT`, `DELETE`.

✅ *Projeto 2: API com Autenticação*

- Criar um sistema de login com JWT.
- Criar um CRUD para gerenciar posts de um blog.

✅ *Projeto 3: Sistema Completo*

- Criar um **sistema de vendas** ou **gestão de tarefas**.
- Implementar relacionamento entre tabelas (Ex: Produtos e Pedidos).
- Criar um **painel administrativo** com React/Vue/Angular.