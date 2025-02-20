Um banco de dados é um sistema organizado para armazenar, gerenciar e recuperar informações de forma estruturada e eficiente.
<center><h1>Tipos Comuns</h1></center>

- *Banco de Dados Relacional:* Armazena dados em tabelas com relacionamentos definidos (SQL).
- *Banco de Dados não Relacional*: Flexível para dados não estruturados (NoSQL).

---
<center><h1>Banco de Dados Relacional vs Banco de Dados não Relacional</h1></center>

A principal diferença entre bancos de dados relacionais e não relacionais está na forma como os dados são estruturados, armazenados e gerenciados. 
Vamos explorar as características de cada um e suas distinções:

- Estrutura:  
	- *SQL*: Os dados são organizados em **tabelas**, com relacionamentos definidos entre elas (via chaves primárias e estrangeiras).  
	- *NoSQL*: Flexível! Dados podem ser armazenados em formatos **não tabulares** (JSON | Chave-valor | Grafos | Wide-Column)

- Esquema: 
	- *SQL*: Fixo. Requer um **esquema pré-definido** (estrutura rígida). As colunas e tipos de dados (ex: `INT`, `VARCHAR`) devem ser definidos antes de inserir dados.
	- *NoSQL*: Dinâmico. Não exige um esquema rígido. Os dados podem variar em estrutura (ex: um documento pode ter campos diferentes de outro).

- Linguagem de Consulta:
	- *SQL*: Usa **SQL** para consultas complexas, joins e operações transacionais.
	- *NoSQL*: Não usa SQL. Consultas são adaptadas ao modelo de dados (ex: APIs específicas ou linguagens como MongoDB Query Language).

- Consistência:  
	- *SQL*: Segue o **ACID** (Atomicidade, Consistência, Isolamento, Durabilidade), garantindo transações confiáveis e integridade dos dados.
	- *NoSQL*:  Prioriza **disponibilidade e escalabilidade** (BASE: *Basically Available, Soft state, Eventually consistent*). Menos rígido que ACID.

- Escalabilidade:
	- *SQL*: Geralmente escalona **verticalmente** (aumentando capacidade do servidor), o que pode ser limitado e custoso.
	- *NoSQL*: Escalona **horizontalmente** (adicionando servidores/distribuindo dados), ideal para grandes volumes e alta demanda.

- Casos de Uso:
	- *SQL*: Ideal para aplicações com dados estruturados e relacionamentos complexos (ex: sistemas financeiros, ERP, CRM). Use se você precisa de transações seguras, integridade de dados e relacionamentos bem definidos (ex: sistema bancário).
	- *NoSQL*: Aplicações com dados semi ou não estruturados, alta velocidade de escrita/leitura ou escalabilidade massiva (ex: redes sociais, IoT, análise em tempo real). Use se seus dados são heterogêneos, a escala é crítica, ou você precisa de flexibilidade (ex: aplicações em tempo real, big data).

Ambos têm vantagens e desvantagens, e a escolha depende do contexto do projeto. Hoje, **muitos sistemas usam ambos** (arquitetura híbrida) para aproveitar os benefícios de cada modelo. 