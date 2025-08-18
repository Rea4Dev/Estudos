---
data_criacao: 18-08-2025
flashcards: Não feito
revisão: Não feita
---
# 📌 Níveis de Teste

## Conceito geral

``Definição`` (ISTQB): *test levels* são **agrupamentos organizados de atividades de teste relacionados a uma mesma parte ou objetivo do software**, tratados como um estágio dentro do ciclo de vida.

``Objetivo``: dividir para conquistar → **cada nível tem foco, riscos e responsabilidades diferentes**, *mas todos se complementam*.


## ⚖️ Importante: níveis ≠ tipos de teste.

- ``Níveis`` = onde/quando testamos no ciclo de vida.

- ``Tipos`` = o que ou qual atributo testamos (funcional, desempenho, segurança…).


---

# 🔹 Teste de Unidade (Unitário / Componente)

``Escopo``: menor unidade testável de software (função, método, classe, módulo).

``Responsável típico``: o próprio desenvolvedor.

``Foco``: validar se o código funciona de acordo com o design de baixo nível.

``Técnicas comuns``: caixa-branca, TDD, mocks/stubs para dependências externas.

``Ferramentas``: JUnit, pytest, NUnit, Google Test.

``Benefício``: defeitos são encontrados cedo, quando mais baratos de corrigir.

``Exemplo``: testar se a função calcular_imposto() retorna o valor esperado com diferentes entradas.


---

🔹 Teste de Integração

Escopo: interações entre unidades, módulos ou componentes.

Foco: defeitos em interfaces, protocolos de comunicação, troca de dados.

Abordagens:

Top-down (do mais alto nível para baixo, usando stubs).

Bottom-up (dos módulos básicos para cima, usando drivers).

Sanduíche (mistura dos dois).

Big Bang (tudo junto de uma vez → pouco recomendado em projetos grandes).


Responsável típico: desenvolvedores + suporte de testers.

Exemplo: verificar se o módulo de login integra corretamente com o banco de dados e o sistema de autenticação externo.



---

🔹 1.2.3 Teste de Sistema

Escopo: o sistema completo como um todo.

Foco: validar o software contra requisitos funcionais e não-funcionais.

Tipos de teste envolvidos: funcionalidade, desempenho, segurança, usabilidade, compatibilidade etc.

Responsável típico: equipe de QA/testes (independente da dev).

Exemplo: testar se o aplicativo de e-commerce permite cadastrar, comprar e pagar um produto corretamente.



---

🔹 1.2.4 Teste de Aceitação

Escopo: verificação final antes da entrega.

Foco: garantir que o sistema atende às necessidades do usuário/negócio.

Responsável típico: cliente/usuário final, com suporte do time de QA.

Subtipos comuns:

UAT (User Acceptance Test): usuários avaliam se atende aos fluxos de negócio.

Teste de Aceitação Operacional: checar se o sistema roda bem no ambiente real (backup, recuperação, monitoramento).

Teste de Contrato/Regulatório: verificação contra normas ou leis (ex.: PCI-DSS, LGPD).

Teste Alfa/Beta: conduzido por usuários internos (alfa) ou externos (beta) em ambientes controlados.


Exemplo: cliente simula a compra completa no sistema e valida se o processo reflete as regras de negócio acordadas.



---

🧩 Relação entre os níveis

Unitário: garante a saúde dos blocos de construção.

Integração: garante que blocos “conversem” corretamente.

Sistema: garante que o produto todo cumpre os requisitos.

Aceitação: garante que o produto resolve o problema do usuário.


📌 Pirâmide de testes:

Base larga (unitários) → maior quantidade, rápidos e automatizados.

Meio (integração e sistema) → menos numerosos, mais caros.

Topo (aceitação) → mais poucos, geralmente manuais/semiautomatizados.



---

📝 Dicas de estudo

Sempre associe nível ↔ artefato:

Unitário ↔ código-fonte.

Integração ↔ design de componentes/interfaces.

Sistema ↔ requisitos funcionais/não funcionais.

Aceitação ↔ requisitos de usuário/contrato.


Pergunte-se: “Que risco é mais provável aqui?” → isso define prioridade dos testes.



---

👉 Pronto! Esse é o panorama teórico.
Na sua proposta, você vai “fazer os quatro níveis manualmente”.
Quer que eu já prepare um mini-exemplo prático (mesmo que abstrato, tipo uma função simples) mostrando como ficaria cada nível aplicado?