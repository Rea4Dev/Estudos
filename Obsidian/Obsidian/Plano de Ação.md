# WorkFlow

Antes de começar o desenvolvimento de todo o código, é necessário e fundamental entender profundamente o comportamento e as relações das tabelas no banco de dados do SIT. 
Desta forma, por hora, elaborei o seguinte fluxo para explorar e documentar adequadamente (lembrando que os códigos abaixo não foram testados e muito provavelmente não estão de acordo com a real arquitetura - eu apenas rapidamente os desenvolvi enquanto pensava na lógica e, para não esquecer dessas possibilidades de consultas SQL, as anotei):

## 1. Realizar a análise das Tabelas
- Descrição das Tabelas:
```SQL
DESCRIBE ITS_Test;

DESCRIBE ITS_Operation;

DESCRIBE ITS_Action;
```
Algo parecido com isso pode fornecer uma visão geral das colunas e tipos de dados de cada tabela.

- As Chaves Primárias e Estrangeiras:
```SQL
SELECT cols.table_name, cols.column_name, cols.position, cons.status, cons.owner

FROM all_constraints cons, all_cons_columns cols

WHERE cols.table_name IN ('ITS_Test', 'ITS_Operation', 'ITS_Action')

  AND cons.constraint_type IN ('P', 'R')

  AND cons.constraint_name = cols.constraint_name

  AND cons.owner = cols.owner

ORDER BY cols.table_name, cols.position;
```
Algo parecido com isso pode ajudar a entender como as tabelas estão relacionadas.


## 2. Exploração dos Dados
- Realizar a contagem de registros:
```SQL
SELECT 'ITS_Test' AS table_name, COUNT(*) AS row_count FROM ITS_Test

UNION ALL

SELECT 'ITS_Operation', COUNT(*) FROM ITS_Operation

UNION ALL

SELECT 'ITS_Action', COUNT(*) FROM ITS_Action;
```
Algo parecido com isso pode dar uma ideia do volume de dados em cada tabela.

- Exemplos de Dados:
```SQL

SELECT * FROM ITS_Test WHERE ROWNUM <= 5;

SELECT * FROM ITS_Operation WHERE ROWNUM <= 5;

SELECT * FROM ITS_Action WHERE ROWNUM <= 5;

```
Visualizar alguns registros pode ajudar a entender a estrutura e o conteúdo.


## 3. Relações entre Tabelas
- Junções Básicas:
```SQL
SELECT t.TEST_ID, t.MMC_CODE, t.OP_NUMBER, o.OPERATION_ID, o.START_TIME, o.END_TIME, o.STATUS

FROM ITS_Test t

JOIN ITS_Operation o ON t.TEST_ID = o.TEST_ID

WHERE ROWNUM <= 10;
```
Algo parecido com isso mostrará como os testes e operações estão relacionados.

- Relações com Actions:
```SQL
SELECT o.OPERATION_ID, o.STATUS, a.ACTION_ID, a.ACTION_TYPE, a.RESULT

FROM ITS_Operation o

JOIN ITS_Action a ON o.OPERATION_ID = a.OPERATION_ID

WHERE ROWNUM <= 10;
```
Algo parecido com isso ajudará a entender como as ações estão vinculadas às operações.


## 4. Análise Temporal
- Distribuição Temporal:
```SQL
SELECT TRUNC(START_TIME, 'HH24') AS hour, COUNT(*) AS operations

FROM ITS_Operation

GROUP BY TRUNC(START_TIME, 'HH24')

ORDER BY hour;
```
Algo parecido com isso mostrará como as operações estão distribuídas ao longo do tempo.

- Durações das Operações:
```SQL
SELECT OPERATION_ID,

       START_TIME,

       END_TIME,

       (END_TIME - START_TIME) * 24 * 60 AS duration_minutes

FROM ITS_Operation

WHERE END_TIME IS NOT NULL

  AND ROWNUM <= 10;
```
Algo parecido com isso ajudará a entender a duração típica das operações.


## 5. Documentação
- Diagrama ER: Posso criar um diagrama de entidade-relacionamento (ER) para visualizar as relações entre as tabelas.  DbVisualizer, Oracle (preferencial) ou MySQL Workbench podem ajudar.

- Glossário de Campos: Documentar cada campo importante, incluindo:
Nome do campo
Tipo de dados
Descrição
Exemplo de valor
Relacionamentos


## 6. Testes de Consultas
- Consultas de Exemplo: Escreverei consultas que simulem o que o script Python fará. Por exemplo:
```SQL
SELECT o.OPERATION_ID, o.START_TIME, o.END_TIME, o.STATUS, t.MMC_CODE, t.OP_NUMBER

FROM ITS_Operation o

JOIN ITS_Test t ON o.TEST_ID = t.TEST_ID

WHERE o.LAST_MODIFIED > SYSDATE - INTERVAL '5' MINUTE;
```
  

## 7. Performance
- Explain Plan: Usarei EXPLAIN PLAN para entender o custo das consultas:
```SQL
EXPLAIN PLAN FOR

SELECT o.OPERATION_ID, o.START_TIME, o.END_TIME, o.STATUS, t.MMC_CODE, t.OP_NUMBER

FROM ITS_Operation o

JOIN ITS_Test t ON o.TEST_ID = t.TEST_ID

WHERE o.LAST_MODIFIED > SYSDATE - INTERVAL '5' MINUTE;

  

SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY);
```
Algo parecido com isso ajudará a identificar possíveis gargalos de performance.


## 8. Documentação das Descobertas
- Registre Tudo: Manterei um documento (Obsidian e provavelmente não precisarei compartilhar com ninguém) atualizado com:  
Estrutura das tabelas
Relacionamentos chave
Consultas úteis
Padrões observados nos dados
Problemas encontrados e soluções


## 9. Colaboração com a Equipe
- Revisão com Especialistas: Discutirei minhas descobertas com o desenvolvedor sênior (Wendel) para validar suas conclusões e obter insights adicionais.  


## 10. Próximos Passos
- Plano de Ação: Com base na análise, criarei um plano detalhado para a implementação do script, incluindo:  
Quais tabelas e campos serão monitorados
Com que frequência o banco será verificado
Como os logs serão estruturados
Quais consultas serão usadas