# DDL - A Arte de Definir Estruturas

O DDL (Data Definition Language) é a parte do SQL que se encarrega de criar, alterar e excluir os objetos do banco de dados. Se o SQL fosse um prédio, o DDL seria a equipe de arquitetura e construção – sem ele, nada de existir!

- **CREATE**: Cria novos objetos (tabelas, índices, views, etc).
- **ALTER**: Modifica a estrutura dos objetos existentes.
- **DROP**: Remove objetos do banco de dados de forma definitiva.
- **TRUNCATE**: Remove todos os registros de uma tabela, mantendo sua estrutura.

---

## CREATE: Construindo a Base

O comando CREATE é responsável por criar novas estruturas no banco. Geralmente, usamos para definir tabelas com suas colunas e restrições.

```SQL
CREATE TABLE clientes (
    id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    data_cadastro DATE DEFAULT SYSDATE
);
```


Nesse exemplo, criamos a tabela `clientes` com uma chave primária, uma coluna que não pode ser nula, uma restrição de unicidade para o e-mail e um valor padrão para a data de cadastro.

---

## ALTER: Remodelando a Estrutura

O ALTER permite que você modifique uma estrutura existente. Pode ser para adicionar, modificar ou remover colunas e restrições.

```SQL
ALTER TABLE clientes
ADD telefone VARCHAR(15);
```

Acima, adicionamos uma nova coluna `telefone` à tabela `clientes`.

Você também pode, por exemplo, alterar o tipo de uma coluna:

```SQL
ALTER TABLE clientes
MODIFY nome VARCHAR(150);
```

Aqui, aumentamos o tamanho máximo permitido para a coluna `nome`.

---

## DROP: Derrubando a Estrutura

Quando uma tabela ou outro objeto não é mais necessário, o comando DROP remove-o do banco de dados. Cuidado: essa operação é definitiva!

```SQL
DROP TABLE clientes;
```

Esse comando exclui completamente a tabela `clientes` e todos os dados contidos nela.

---

## TRUNCATE: Limpando a Casa

O TRUNCATE remove todos os registros de uma tabela, mas mantém sua estrutura intacta. É útil para "resetar" a tabela sem recriá-la.

```SQL
TRUNCATE TABLE clientes;
```

Diferente do DROP, o TRUNCATE apenas limpa a tabela, deixando a definição para futuros usos.

---

## Recapitulando

- **CREATE**: Constrói a estrutura do objeto.
- **ALTER**: Modifica a estrutura existente.
- **DROP**: Exclui o objeto permanentemente.
- **TRUNCATE**: Limpa todos os registros da tabela, mas mantém a estrutura.

Com essas ferramentas, você tem o poder de criar e remodelar seu banco de dados do jeito que precisar. Lembre-se: com grandes poderes vêm grandes responsabilidades – use o DDL com sabedoria e sempre faça backup dos dados importantes!
