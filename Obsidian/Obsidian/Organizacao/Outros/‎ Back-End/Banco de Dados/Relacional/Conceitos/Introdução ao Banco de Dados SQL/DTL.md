# DTL - Gerenciando Transações com Segurança

O DTL (Data Transaction Language) – também conhecido como TCL (Transaction Control Language) – é a parte do SQL que garante a integridade dos dados durante operações que envolvem múltiplas etapas. Imagine-o como o "botão de salvar" (ou "desfazer") do seu banco de dados: ele confirma ou reverte um conjunto de ações, para que você nunca perca o controle.

- **COMMIT**: Confirma as mudanças feitas durante a transação, tornando-as permanentes.
- **ROLLBACK**: Desfaz as operações realizadas na transação, retornando o banco ao estado anterior.
- **SAVEPOINT**: Cria pontos intermediários dentro de uma transação, permitindo reverter apenas parte das alterações.

---

## COMMIT: Salvando Suas Operações

Após executar uma série de comandos que modificam dados, você usa o COMMIT para confirmar que tudo está correto. É como apertar o botão de "salvar" no seu trabalho.

```SQL
INSERT INTO vendas (produto, quantidade, valor)
VALUES ('Notebook', 2, 3500);

COMMIT;
```

Neste exemplo, os dados da venda são definitivamente gravados no banco após o COMMIT.

---

## ROLLBACK: Desfazendo a Bagunça

Se algo der errado ou se você mudar de ideia, o ROLLBACK desfaz todas as operações realizadas na transação atual. É como apertar o botão de "desfazer" no editor de texto.

```SQL
INSERT INTO vendas (produto, quantidade, valor)
VALUES ('Notebook', 2, 3500);

-- Algo não saiu como esperado:
ROLLBACK;
```

Após o ROLLBACK, nenhuma alteração feita na transação é salva.

---

## SAVEPOINT: Pontos de Salvamento no Meio do Caminho

Quando sua transação é longa e você quer ter a opção de reverter apenas parte dela, use SAVEPOINT para marcar pontos de verificação.

```SQL
-- Inicia a transação
BEGIN;

INSERT INTO vendas (produto, quantidade, valor)
VALUES ('Notebook', 2, 3500);

SAVEPOINT ponto_intermediario;

INSERT INTO vendas (produto, quantidade, valor)
VALUES ('Mouse', 5, 150);

-- Se algo der errado após o SAVEPOINT, você pode reverter até aqui:
ROLLBACK TO ponto_intermediario;

-- Confirma o que ficou certo
COMMIT;
```

Neste exemplo, se a inserção do mouse der errado, você pode reverter apenas essa parte, mantendo a venda do notebook.

---

## Recapitulando

- **COMMIT**: Torna permanentes todas as operações realizadas na transação.
- **ROLLBACK**: Reverte todas as operações realizadas na transação (ou até um SAVEPOINT específico).
- **SAVEPOINT**: Marca um ponto de verificação dentro da transação para um rollback parcial.

Com o DTL, você tem o controle total sobre suas transações, garantindo que suas operações sejam seguras e consistentes. Use essas ferramentas com sabedoria e mantenha seu banco de dados sempre em ordem!