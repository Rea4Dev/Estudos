1. Conversa inicial com Wendel e Bruno

2. Análise Geral inicial para gerar familiaridade (1 dia)

3. Elaboração de Cenário e Plano de Ação (1 dia)

4. Garantia da Maturidade Conceitual Crítica

5. Realizar a análise das Tabelas (1 dia)
5.1 Descrever as colunas (DESCRIBE)
5.2 Mapear chaves primárias e estrangeiras
5.3 Validar índices relevantes

6. Exploração dos Dados (0,5 dia)
6.1 Verificar volume (COUNT)
6.2 Visualizar amostras (SELECT * / ROWNUM)
6.3 Identificar possíveis inconsistências

7. Mapeamento das Relações entre Tabelas (0,5 dia)
7.1 Entender JOINs entre ITS_Test, ITS_Operations e ITS_Operations_Action
7.2 Confirmar chaves de ligação e colunas principais
7.3 Verificar se há necessidade de ajustes ou criação de índices adicionais

8. Análise Temporal (0,5 dia)
8.1 Avaliar distribuição de START_TIME e END_TIME
8.2 Calcular duração média das operações
8.3 Verificar possíveis picos ou gargalos de execução

9. Documentação (Diagrama ER, Glossário de Campos) (1 dia)
9.1 Criar ou atualizar diagrama de entidade-relacionamento
9.2 Descrever cada campo e seu propósito (glossário)
9.3 Organizar em local acessível (ex.: Obsidian, wiki interna)

10. Testes de Consultas (1 dia)
10.1 Elaborar queries simulando extração de dados
10.2 Validar resultados em ambiente de desenvolvimento
10.3 Ajustar consultas conforme necessidades do script futuro

11. Performance (EXPLAIN PLAN, Índices) (1 dia)
11.1 Utilizar EXPLAIN PLAN nas principais consultas
11.2 Verificar possíveis gargalos e otimizações
11.3 Discutir com o DBA, se necessário, criação ou ajuste de índices

12. Documentação das Descobertas (0,5 dia)
12.1 Registrar problemas e soluções encontradas
12.2 Atualizar logs de aprendizado e decisões tomadas
12.3 Compartilhar com a equipe (Wendel e Bruno)

13. Colaboração com a Equipe (Wendel/Bruno) (0,5 dia)
13.1 Revisar achados e alinhar próximos passos
13.2 Verificar aderência aos requisitos do projeto
13.3 Ajustar prioridades, se necessário

14. Desenvolvimento do Script em Python (3 dias)
14.1 Conectar ao Oracle (cx_Oracle ou SQLAlchemy)
14.2 Implementar lógica de comparação (“estado anterior” vs. “estado atual”)
14.3 Geração de logs em CSV

15. Testes de Integração (1 dia)
15.1 Simular eventos reais no banco de dados
15.2 Validar geração correta dos logs
15.3 Ajustar quaisquer inconsistências identificadas

16. Entrega e Revisão Final (1 dia)
16.1 Revisar todo o projeto e checar requisitos
16.2 Refinar documentações e código, se necessário
16.3 Encerrar a POC e apresentar resultados