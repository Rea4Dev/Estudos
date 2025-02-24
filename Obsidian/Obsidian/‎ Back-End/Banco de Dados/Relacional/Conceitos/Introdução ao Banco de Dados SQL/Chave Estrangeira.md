- Uma chave estrangeira é um atributo que **referencia a chave primária** de outra tabela, garantindo a **integridade referencial** entre os dados. Ela estabelece relações entre tabelas e impede valores inválidos ou órfãos.

- Atributo de uma tabela que estabelece um *relacionamento com a chave primária de outra tabela*.

- É através da chave estrangeira que *sabemos com qual registro em outra tabela um registro está relacionado*.

# Tabela: ITS_Test
| *TEST_ID* | MMC_CODE | OP_NUMBER | DESCRIPTION      |
| --------- | -------- | --------- | ---------------- |
| 1         | MMC123   | 101       | Teste de leitura |
| 2         | MMC456   | 102       | Teste de escrita |

# Tabela: ITS_Operations
| OPERATION_ID | *TEST_ID (FK)* | START_TIME          | END_TIME            | STATUS  |
| ------------ | -------------- | ------------------- | ------------------- | ------- |
| 1001         | 1              | 2025-02-19 10:00:00 | 2025-02-19 10:15:00 | SUCCESS |
| 1002         | 1              | 2025-02-19 11:00:00 | 2025-02-19 11:20:00 | FAIL    |
| 1003         | 2              | 2025-02-19 12:00:00 | 2025-02-19 12:25:00 | SUCCESS |
- Na tabela **ITS_Operations**, a coluna **TEST_ID** funciona como chave estrangeira, garantindo que cada operação esteja associada a um teste válido cadastrado em **ITS_Test**.
- Essa relação assegura a integridade referencial: não é possível registrar uma operação com um **TEST_ID** que não exista na tabela de testes.