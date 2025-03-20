# Do que se trata?
Desenvolvimento em Python (3.13.2/64bits) de um script Gerador de Log, analisando uma base de dados SQL (Oracle) em tempo de execução para uma ação em específico que deve ser monitorada e mapeada.

---
# 1. Como funciona atualmente?
## 1.1 SIT
O SIT - Sistema Integrado de Testes - do time de Automação Industrial (dentro da Engenharia de Manufatura) é um setor da industria aeronáutica que desenvolve automações de testes para, não unicamente, mas principalmente, a elétrica das aeronaves. 
## 1.2 Pessoal SIT envolvido
- Bruno Lima Zattoni
*Formação*: Engenheiro Eletricista com Especialização em Aeronáutica (pelo Programa de Especialização Aeronáutica - PEE, fornecido pela parceria Embraer | ITA).
*Cargo*: Engenheiro de Desenvolvimento de Processos - Equipe SIT - Engenharia de Automação e 4.0 - Engenharia de Manufatura.
*Posição*: P.O (principal) mas atuante em diversos outros processos. Neste projeto atuará como P.O.
*Experiência*: 6 anos de experiência no SIT.

- Wendel Silveira
*Formação*: Cientista da Computação com certificação em SCRUM Master.
*Cargo*: Analista de Processos, Desenvolvedor Sênior Full-Stack - Equipe SIT - Engenharia de Automação e 4.0 - Engenharia de Manufatura.
*Posição*: Desenvolvedor Sênior Full-Stack, neste projeto atuará como Tech Lead.
*Experiência*: Mais de duas décadas de experiência em desenvolvimento de software full-stack. No SIT possui mais de 4 anos de experiência.
## 1.3 Testes SIT
Os Testes (ou Roteiros de Teste, como também são chamados) são elaborados pela equipe de Engenharia de Manufatura.
Um operador da produção executa um teste (digamos, por enquanto, que em um "checklist") com auxílio de alguns equipamentos embarcados desenvolvidos pela equipe SIT.

## 1.4 WebSIT
Estes "checklists" encontram-se em um portal web, chamado WebSIT. No WebSIT, com base em algumas informações, o operador pode selecionar determinado teste e executá-lo. Logo após é enviado ao servidor do WebSIT o resultado deste teste.
![[Exemplo WebSIT.png]]

## 1.5 MMC e OP
Todo teste é um **MMC** (Meio de Medição e Controle). É como se fosse uma "receita" arquivada de como testar cada sistema. Quando determinado avião vai testar algo, ele replica essa "receita" em uma OP (Ordem de Produção), que gera a demanda para o operador executar de fato o teste.

## 1.6 Os testes (testes, operações e actions)
Chamamos de **teste** todo um teste específico de algo em uma aeronave (Com uma MMC e OP) e de **operação** uma seção específica dentro deste teste. Uma operação é organizada em checklists e validações, chamados de **actions**.
Por exemplo, um determinado teste possuim 4 operações, cada uma delas com uma série de fatores a serem analisados e validados (actions). 
Uma operação sempre possuirá um botão de play nela para iniciar. As operações são isoladas entre si.

## 1.7 Rastreabilidade de operações
Atualmente, ações não possuem nenhum tipo de rastreabilidade nativa (ou seja, não há uma geração de log para saber quantas vezes foram executadas, quando e nem qual o resultado). 
Buscaremos explorar como gerar isso com base nos dados presentes no servidor.

---
# 2. O que querem implementar?
Toda vez que uma ação for executada queremos saber em qual horário isso ocorreu e em qual status terminou esta action (se obteve sucesso ou não).
O nosso P.O (Bruno) deu um exemplo de use-case:

| Data-Hora                       | OP       | MMC  | Aeronave | Operação | Step | Tipo    | Resultado |
| ------------------------------- | -------- | ---- | -------- | -------- | ---- | ------- | --------- |
| 18-FEB-25 02.33.41.808000000 PM | 91005213 | 1597 | 10052    | 002.000  | B    | Leitura | FAIL      |
![[Exemplo WebSIT.png]]

---
# 3. Como querem implementar?
Deseja-se que haja um script em Python que estará monitorando a base de dados SQL (enquanto o teste é executado) para assim então gerar um log (em CSV) para cada operação clicada, armazenando também quando foi clicada e qual foi o status final dela.

## 3.1 Dados Técnicos
Já sabemos que há três tabelas SQL principais que estarão com as informações relacionadas necessárias:
- ITS_Test
- ITS_Operations
- ITS_Operations_Action
Há uma preferência grande do uso de consultas e relações SQL onde puder ser aplicado neste projeto (desenvolvedor Sênior atestou que isso otimiza a execução).

## 3.2 Sugestão de lógica
Foi sugerido que o script periodicamente comparasse o estado anterior da tabela com o atual, a fim de mapear determinado evento na base de dados SQL, para posteriormente relacionar com as outras tabelas e por fim gerar um log. 

---
# 4. Meu plano de Ação
Antes de começar o desenvolvimento de todo o código, é necessário e fundamental entender profundamente o comportamento e as relações das tabelas no banco de dados do SIT. 
Desta forma, por hora, elaborei o seguinte fluxo para explorar e documentar adequadamente (lembrando que os códigos abaixo não foram testados e muito provavelmente não estão de acordo com a real arquitetura - eu apenas rapidamente os desenvolvi enquanto pensava na lógica e, para não esquecer dessas possibilidades de consultas SQL, as anotei):

## 4.1 Realizar a análise das Tabelas
- Descrição das Tabelas:
```SQL
DESCRIBE ITS_Test;

DESCRIBE ITS_Operations;

DESCRIBE ITS_Operations_Actions;
```
Algo parecido com isso pode fornecer uma visão geral das colunas e tipos de dados de cada tabela.

- As Chaves Primárias e Estrangeiras:
```SQL
SELECT cols.table_name, cols.column_name, cols.position, cons.status, cons.owner

FROM all_constraints cons, all_cons_columns cols

WHERE cols.table_name IN ('ITS_Test', 'ITS_Operations', 'ITS__Operations_Actions')

  AND cons.constraint_type IN ('P', 'R')

  AND cons.constraint_name = cols.constraint_name

  AND cons.owner = cols.owner

ORDER BY cols.table_name, cols.position;
```
Algo parecido com isso pode ajudar a entender como as tabelas estão relacionadas.


## 4.2 Exploração dos Dados
- Realizar a contagem de registros:
```SQL
SELECT 'ITS_Test' AS table_name, COUNT(*) AS row_count FROM ITS_Test

UNION ALL

SELECT 'ITS_Operations', COUNT(*) FROM ITS_Operations

UNION ALL

SELECT 'ITS__Operations_Actions', COUNT(*) FROM ITS__Operations_Actions;
```
Algo parecido com isso pode dar uma ideia do volume de dados em cada tabela.

- Exemplos de Dados:
```SQL

SELECT * FROM ITS_Test WHERE ROWNUM <= 5;

SELECT * FROM ITS_Operations WHERE ROWNUM <= 5;

SELECT * FROM ITS__Operations_Actions WHERE ROWNUM <= 5;

```
Visualizar alguns registros pode ajudar a entender a estrutura e o conteúdo.


## 4.3 Relações entre Tabelas
- Junções Básicas:
```SQL
SELECT t.TEST_ID, t.MMC_CODE, t.OP_NUMBER, o.OPERATION_ID, o.START_TIME, o.END_TIME, o.STATUS

FROM ITS_Test t

JOIN ITS_Operations o ON t.TEST_ID = o.TEST_ID

WHERE ROWNUM <= 10;
```
Algo parecido com isso mostrará como os testes e operações estão relacionados.

- Relações com Actions:
```SQL
SELECT o.OPERATION_ID, o.STATUS, a.ACTION_ID, a.ACTION_TYPE, a.RESULT

FROM ITS_Operations o

JOIN ITS__Operations_Actions a ON o.OPERATION_ID = a.OPERATION_ID

WHERE ROWNUM <= 10;
```
Algo parecido com isso ajudará a entender como as ações estão vinculadas às operações.


## 4.4 Análise Temporal
- Distribuição Temporal:
```SQL
SELECT TRUNC(START_TIME, 'HH24') AS hour, COUNT(*) AS operations

FROM ITS_Operations

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

FROM ITS_Operations

WHERE END_TIME IS NOT NULL

  AND ROWNUM <= 10;
```
Algo parecido com isso ajudará a entender a duração típica das operações.


## 4.5 Documentação
- Diagrama ER: Posso criar um diagrama de entidade-relacionamento (ER) para visualizar as relações entre as tabelas.  DbVisualizer, Oracle (preferencial) ou MySQL Workbench podem ajudar.

- Glossário de Campos: Documentar cada campo importante, incluindo:
Nome do campo
Tipo de dados
Descrição
Exemplo de valor
Relacionamentos


## 4.6 Testes de Consultas
- Consultas de Exemplo: Escreverei consultas que simulem o que o script Python fará. Por exemplo:
```SQL
SELECT o.OPERATION_ID, o.START_TIME, o.END_TIME, o.STATUS, t.MMC_CODE, t.OP_NUMBER

FROM ITS_Operations o

JOIN ITS_Test t ON o.TEST_ID = t.TEST_ID

WHERE o.LAST_MODIFIED > SYSDATE - INTERVAL '5' MINUTE;
```
  

## 4.7 Performance
- Explain Plan: Usarei EXPLAIN PLAN para entender o custo das consultas:
```SQL
EXPLAIN PLAN FOR

SELECT o.OPERATION_ID, o.START_TIME, o.END_TIME, o.STATUS, t.MMC_CODE, t.OP_NUMBER

FROM ITS_Operations o

JOIN ITS_Test t ON o.TEST_ID = t.TEST_ID

WHERE o.LAST_MODIFIED > SYSDATE - INTERVAL '5' MINUTE;

  

SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY);
```
Algo parecido com isso ajudará a identificar possíveis gargalos de performance.


## 4.8 Documentação das Descobertas
- Registrar Tudo: Manterei um documento (Obsidian e provavelmente não precisarei compartilhar com ninguém) atualizado com:  
Estrutura das tabelas
Relacionamentos chave
Consultas úteis
Padrões observados nos dados
Problemas encontrados e soluções


## 4.9 Colaboração com a Equipe
- Revisão com Especialistas: Discutirei minhas descobertas com o desenvolvedor sênior (Wendel) para validar suas conclusões e obter insights adicionais.  


## 4.10 Próximos Passos
- Plano de Ação: Com base na análise, criarei um plano detalhado para a implementação do script, incluindo:  
Quais tabelas e campos serão monitorados
Com que frequência o banco será verificado
Como os logs serão estruturados
Quais consultas serão usadas

---
# 5. Estudos paralelos
Não possuo familiaridade o suficiente para sua imediata execução, desta forma, adquiro este plano de ação de estudos prévios antes de iniciar no projeto. Os estudos não estão estruturados de forma a englobar o todo, e sim, pontos mais críticos e principais.
Após estes estudos do plano de ação, irei iniciar imediatamente o projeto, entretanto, ainda consultando minhas fontes e aprendendo focais sempre que tiver uma necessidade.

<center><h1>Plano de Aprendizado SQL para o Projeto</h1></center>
## 5.1 Fundamentos Essenciais (Se ainda os domino, revisar rapidamente)

🔹 SELECT básico: WHERE, ORDER BY, LIMIT (ou ROWNUM no Oracle).
🔹 Funções de agregação: COUNT(), SUM(), AVG(), MIN(), MAX().
🔹 Filtros avançados: BETWEEN, IN, LIKE.
🔹 Conversões de tipo: TO_DATE(), TO_TIMESTAMP(), TO_CHAR().

⏳ Tempo estimado: 2 a 3 horas de prática e revisão, se necessário.


---

## 5.2 Trabalhando com múltiplas tabelas (Super relevante para meu caso!)

🔹 JOINs (Foco em INNER JOIN e LEFT JOIN): Para cruzar informações entre ITS_Test, ITS_Operation e ITS_Action.
🔹 Subqueries (SELECT dentro de SELECT): Para criar consultas mais organizadas e eficientes.
🔹 CTEs (WITH Queries): Para deixar consultas mais legíveis quando precisar de várias operações encadeadas.

⏳ Tempo estimado: 5 a 6 horas de prática ao longo dos primeiros dias do projeto.


---

## 5.3 Rastreabilidade e otimização das consultas

🔹 Uso do EXPLAIN PLAN: Para analisar o desempenho das queries e evitar consultas lentas.
🔹 Índices (INDEX): Saber quando e como eles melhoram a performance das buscas.
🔹 Particionamento de tabelas (se aplicável ao banco da empresa).

⏳ Tempo estimado: 4 a 6 horas de prática ao longo das semanas, conforme for necessário otimizar.


---

## 5.4 Manipulação segura de dados (Para quando precisar modificar a base)

🔹 UPDATE e DELETE seguros: Sempre testar primeiro com SELECT antes de modificar.
🔹 Transações (BEGIN TRANSACTION, COMMIT, ROLLBACK): Para evitar apagar dados acidentalmente.
🔹 Uso de FOREIGN KEYS e integridade referencial: Para entender por que certos DELETE falham (como no erro que você encontrou).

⏳ Tempo estimado: 3 a 5 horas de aprendizado prático, aplicando quando necessário.


---

## 5.5 Automação e Integração com Python

🔹 Usando bibliotecas como cx_Oracle ou SQLAlchemy para conectar ao Oracle e executar queries via Python.
🔹 Escrita de logs automáticos com Python: Para registrar execuções das queries e gerar os arquivos CSV.

⏳ Tempo estimado: 6 a 8 horas de aprendizado prático, conforme você avança no código do seu projeto.

## 5.6 Como irei estudar?

✅ Aplicando os conceitos direto no meu projeto → Sempre que surgir um problema, ver qual desses tópicos pode resolvê-lo.
✅ Usando o banco de desenvolvimento para testar → Assim, posso evita impactar dados reais.
✅ Consultando a documentação do Oracle SQL → Oracle SQL Docs tem detalhes úteis.
✅ Contando com o professor e Wendel para dúvidas e otimizações!

---
# Opinião do Professor 
Abaixo, segue a opinião do professor (estilizado):

> [!TIP] Geraldo Ponte Tavares
> Carvalho, o teu plano de ação está bem estruturado e faz bastante sentido. De forma resumida:
> 1. *Análise das tabelas e relacionamento*  
> - É essencial mapear todas as chaves primárias e estrangeiras (P e R) para entender como os dados se cruzam entre ITS_Test, ITS_Operations e ITS_Operations_Action.
> - Conferir se existem índices relevantes para as colunas que você usará nos JOINs e nos filtros (WHERE). Se não houver, vale conversar com o DBA para criar índices que facilitem o monitoramento.
> 2. *Monitoramento periódico*  
> - A ideia de comparar o “estado anterior” com o “estado atual” é prática e comum. Geralmente se faz isso usando uma coluna de data/hora de última modificação (LAST_MODIFIED ou algo similar).
> - Você pode armazenar a última data/hora consultada e, no próximo loop, buscar apenas os registros que foram alterados após esse timestamp.
> 3. *Geração de logs (CSV)*  
> - Em Python, usar a biblioteca csv ou mesmo pandas facilita a escrita do arquivo CSV.
> - Definir claramente quais colunas entram no log: Data/Hora, Operação, MMC, Aeronave, Step, Tipo, Resultado etc.
> 4. *Integração com Oracle*  
> - Para Python, o cx_Oracle é a biblioteca oficial. Se preferir algo mais alto nível, pode usar o SQLAlchemy.  
> - Sempre testar as queries primeiro no SQL Developer (ou ferramenta que usar) para confirmar se retornam os dados esperados antes de automatizar no Python.
> 5. *Performance e segurança*  
> - Se a base for muito grande, verifique se há índices adequados nas colunas que filtrarão os dados novos/alterados.
> - Se precisar modificar dados (UPDATE/DELETE), use transações (COMMIT/ROLLBACK) e sempre valide no ambiente de desenvolvimento antes de colocar em produção.
> - Caso haja necessidade de algo mais “tempo real” do que polling, vale estudar triggers ou streams do Oracle, mas isso já depende de quão crítico é ter o log imediatamente.
> 6. *Estudos de SQL*  
> - O roteiro de revisão do conteúdo do quarto semestre que você montou (JOINs, subqueries, CTE, EXPLAIN PLAN, índices etc.) cobre bem o essencial para lidar com a maior parte dos cenários de consulta e otimização.
> - Se for mexer em triggers, sequences ou PL/SQL, adicione isso ao seu plano de estudos. Mas só se realmente precisar para o projeto.
><br>No geral, está tudo no caminho certo. É importante documentar bem as descobertas e alinhar com o Tech Lead (Wendel) antes de prosseguir com alterações no ambiente de produção. 
><br>Ressalto, por fim, que é importante que volte a progredir seus conhecimentos em bancos de dados relacionais após este projeto. A grade ensinada em seu curso obteve sucesso em te dar os conhecimentos gerais necessários para poder abordar da forma que está abordando, entretanto, é interessante que você englobe em seu escopo de estudo pessoal a constante evolução de determinados tópicos, como este.
><br>Entendo que sua abordagem no passado tenha sido priorizar ramos do desenvolvimento embarcado, mas (como pode ver) evoluir progressivamente os conteúdos apresentados sempre terá utilidade prática.
><br>Qualquer dúvida extra, é só avisar! Desejo sorte em seu projeto. Lembre-se sempre de versionar os códigos e muito cuidado ao operar o banco de dados.
><br>Forte abraço!

