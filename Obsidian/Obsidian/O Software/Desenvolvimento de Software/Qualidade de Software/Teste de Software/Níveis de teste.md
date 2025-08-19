---
data_criacao: 18-08-2025
flashcards: Não feito
revisão: Não feita
---
# 📌 Níveis de Teste

## Teste vs Qualidade

Precisamos, antes de tudo, diferenciar Teste de Softwares de Qualidade de Software.

	Qualidade de Software
É uma das fatias da Engenharia de Software que trata principalmente de **técnicas estáticas** (ou seja, *que não executam nosso código*, como *inspeção*, *revisão*, *análise estática*).

	Teste de Software
A partir do momento que executa-se o código (ou seja, **técnicas dinâmicas**) para identificar/analisar comportamentos, então estamos tratando de teste.

Qualidade de Software é um subconjunto de Teste de Software.


## Conceito geral

``Definição`` (ISTQB): *test levels* são **agrupamentos organizados de atividades de teste relacionados a uma mesma parte ou objetivo do software**, tratados como um estágio dentro do ciclo de vida.

``Objetivo``: dividir para conquistar → **cada nível tem foco, riscos e responsabilidades diferentes**, *mas todos se complementam*.


## ⚖️ Importante: níveis ≠ tipos de teste.

- ``Níveis`` = onde/quando testamos no ciclo de vida.

- ``Tipos`` = o que ou qual atributo testamos (funcional, desempenho, segurança…).

## 🧩 Relação entre os níveis

``Unitário``: garante a saúde dos blocos de construção.

``Integração``: garante que blocos “conversem” corretamente.

``Sistema``: garante que o produto todo cumpre os requisitos.

``Aceitação``: garante que o produto resolve o problema do usuário.

📌 Pirâmide de testes:
*Base larga* (unitários) → maior quantidade, rápidos e automatizados.

*Meio* (integração e sistema) → menos numerosos, mais caros.

*Topo* (aceitação) → mais poucos, geralmente manuais/semiautomatizados.

# 📝 Dicas de estudo

- Sempre associe nível ↔ artefato:

- Unitário ↔ código-fonte.

- Integração ↔ design de componentes/interfaces.

- Sistema ↔ requisitos funcionais/não funcionais.

- Aceitação ↔ requisitos de usuário/contrato.

**Pergunte-se**: “Que risco é mais provável aqui?” → isso define prioridade dos testes.
