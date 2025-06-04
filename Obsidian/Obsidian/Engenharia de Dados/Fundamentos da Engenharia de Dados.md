---
Indice: Engenharia de Dados
---
# Dados

`Dados`: São potenciais informações que podem ser armazenadas e processadas por computador. 

- **Dados estruturados**: são dados organizados em uma estrutura definida, como tabelas em um banco de dados relacional.
    
- **Dados não estruturados**: são dados que não possuem uma estrutura definida, como texto livre, imagens e vídeos.
    
- **Dados semi-estruturados**: são dados que possuem uma estrutura parcialmente definida, como documentos XML e JSON.
    

**Exemplo**: Um engenheiro de dados trabalha com dados estruturados de vendas, dados não estruturados de feedback de clientes e dados semi-estruturados de logs de servidores.

---

# O que é a Engenharia de Dados

Campo da engenharia voltado ao *projeto*, *construção* e *manutenção de sistemas* responsáveis pela **coleta**, **armazenamento**, **processamento** e **distribuição de dados em larga escala**. 

Envolve o uso de técnicas e ferramentas para `garantir que os dados estejam disponíveis, íntegros, seguros` e prontos para análise, *apoiando aplicações analíticas, ciência de dados e inteligência artificial*.

## Areas de atuação

A Engenharia de Dados abrange diversas áreas essenciais para o ciclo de vida dos dados, tais como:

- **Coleta de dados**: Envolve a aquisição sistemática de dados a partir de múltiplas fontes, como bancos de dados transacionais, APIs, dispositivos IoT, arquivos de log e fluxos de dados em tempo real. Essa etapa busca garantir a qualidade e a integridade dos dados desde a origem.
    
- **Armazenamento de dados**: Refere-se ao projeto e implementação de arquiteturas de armazenamento escaláveis e resilientes, utilizando tecnologias como bancos de dados relacionais, bancos NoSQL, data warehouses e data lakes. O objetivo é organizar os dados de forma segura, eficiente e acessível.
    
- **Processamento de dados**: Compreende o uso de pipelines de dados para transformação, limpeza, enriquecimento e integração de dados, por meio de técnicas como ETL (Extract, Transform, Load), ELT e processamento distribuído (ex.: Apache Spark, Flink). Essa etapa prepara os dados para uso analítico e operacional.
    
- **Análise e disponibilização de dados**: Envolve a orquestração e exposição de dados prontos para consumo por analistas, cientistas de dados e aplicações analíticas. Embora a análise de dados em si seja foco da Ciência de Dados, o engenheiro de dados fornece as estruturas que possibilitam a aplicação de algoritmos estatísticos e modelos preditivos com eficiência.

---

# Conceitos

- **Data Warehouse**: É como um “grande repositório central” onde os dados da empresa são armazenados de forma organizada, com o objetivo de facilitar consultas, relatórios e análises. Ele reúne dados de diferentes sistemas em um só lugar.
    
- **Data Mart**: É uma parte específica do Data Warehouse, voltada para um setor da empresa — como vendas, finanças ou marketing. Ele contém apenas os dados relevantes para aquele departamento, o que torna as análises mais rápidas e focadas.
    
- **ETL (Extract, Transform, Load)**: É um processo que serve para preparar os dados antes de serem usados. Primeiro, os dados são extraídos de diferentes fontes (como bancos de dados ou APIs), depois são transformados (limpos, padronizados, ajustados) e, por fim, carregados no local onde serão armazenados, como o Data Warehouse ou o Data Mart.
    
- **Data Governance (Governança de Dados)**: Refere-se ao conjunto de regras, boas práticas e políticas que garantem que os dados da empresa sejam confiáveis, seguros, organizados e utilizados de forma correta e conforme leis e normas.
    

**Exemplo**: Imagine que um engenheiro de dados precisa ajudar o time de vendas a analisar seu desempenho. Para isso, ele cria um processo ETL que coleta dados de sistemas de pedidos e clientes, transforma esses dados para padronizá-los e depois carrega tudo em um Data Mart de vendas. Esse processo segue regras de governança para garantir que os dados estejam corretos e seguros.