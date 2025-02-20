>[!TODO] A possuir nesta página
>- [ ] *CREATE TABLE*, *INSERT*, *SELECT*, *UPDATE*, *DELETE*.
>- [ ] Tipos de dados (*VARCHAR*, *INT*, *DATE*, *BOOLEAN*)
>- [ ] Constraints (*PRIMARY KEY*, *FOREIGN KEY*, *NOT NULL*)
###### Apresentando e História
Existente há mais de 50 anos e padronizada pela ANSCI em 1986 (entretanto, continua a receber atualizações), SQL - *Linguagem Estruturada de Consulta* - foi criada inicialmente pela IBM e usada para manipulação e processamento de estrutura de dados e um banco de dados relacional. 

>Apesar do nome, SQL faz mais que apenas consultas.

> Utilizada em todos SGBD de Banco de Dados Relacionais

###### SGBD
Apesar de ser possível operar um Banco de Dados Relacional sem um intermédio, um SGBD - *Sistema Gerenciador de Banco de Dados* - é um software utilizado para facilitar o uso de Banco de Dados Relacionais. 

Há diversos SGBD no mercado, forcenido por diversas empresas. Aqui, usaremos o Oracle.

###### Como SQL é estruturado
Formamos uma consulta (chamada também de query) através das cláusulas:

- *DDL*: Data Defenition Language - Linguagem de Definição de Dados
Comandos que interagem com os objetos do banco, como as tabelas.

- *DML*: Data Manipulation Language - Linguagem de Manipulação de Dados
Comandos que manipulam os dados.

- DCL: Data Control Language - Linguagem de Controle de Dados
Responsáveis por controlar a parte de segurança, gerindo acessos e permissões de usuários.

- DTL ou TCL: Data Transcrition Language - Linguagem de Transação de Dados
É possível agrupar comandos em uma transação e pode executar essa transação como se fosse um só processo. Chamada "forma atômica". É possível reverter tudo em segurança se necessário.
Usado para garantir a consistência dos dados.

- *DQL*: Data Query Language - Linguagem de Consulta de Dados
Cláusulas que utilizamos para realizar consultas nas tabelas.
![[Pasted image 20250219211540.png | center]]
