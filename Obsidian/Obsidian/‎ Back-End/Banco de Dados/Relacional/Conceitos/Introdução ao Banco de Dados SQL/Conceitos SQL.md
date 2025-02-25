# Divisões do SQL

SQL não é apenas uma ferramenta de consultas que você usa para consultar os dados; ele é dividido em partes que cuidam de diferentes funções no seu banco de dados:

### DDL - Data Definition Language
- Trata da criação e modificação da estrutura do banco.
- Comandos principais: *CREATE*, *ALTER*, *DROP*.
- Pense nele como o arquiteto e decorador do seu banco de dados. É ele quem decide como a casa vai ficar.

### DML - Data Manipulation Language
- Responsável por manipular os dados (inserir, atualizar, excluir e consultar).
- Comandos principais: *SELECT*, *INSERT*, *UPDATE*, *DELETE*.
- Aqui é onde a ação acontece. Toda vez que você roda um SELECT para buscar informações – com filtros, alias ou funções de agregação – você está operando no DML. É o dia a dia da movimentação de dados.

### DCL - Data Control Language
- Cuida dos acessos e permissões.
- Comandos principais: *GRANT*, *REVOKE*.
- Imagine um segurança de balada: ele garante que só as pessoas autorizadas entrem e aproveitem a festa dos dados.

### TCL - Transaction Control Language
- Gerencia as transações, ou seja, garante que um grupo de operações seja completado ou revertido por completo.
- Comandos principais: *COMMIT*, *ROLLBACK*, *SAVEPOINT*.
- Se algo der errado, ele é o botão de “desfazer” que salva o dia.

![[Pasted image 20250219211540.png]]
