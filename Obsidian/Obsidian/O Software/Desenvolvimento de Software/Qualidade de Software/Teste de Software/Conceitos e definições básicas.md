---
data_criacao: 18-08-2025
flashcards: Não feito
revisão: Não feita
pendente: sim
---
*pendente*: Após finalizar esta matéria, reveja todo esta página e garanta que saiba de tudo. Caso não, crie flashcards para o que não souber/esquecer.

Neste "Conceitos e definições básicas", nos preocupamos em introduzir corretamente estes conteúdos. Grande parte deste material tem como objetivo contextualizar, diversos tópicos aqui serão aprofundados posteriormente dentro da estrutura de tópicos anterior, em [[Testes e Manutenção de Software]].
# O que é “teste de software”

> [!Tip] Definição (síntese ISTQB) 
> Teste é o conjunto de *atividades* ao longo do ciclo de vida (*estáticas e dinâmicas*) para **planejar, preparar e avaliar** produtos de software (e artefatos relacionados) **a fim de verificar requisitos, demonstrar adequação ao propósito e revelar defeitos**, *reduzindo o risco de falhas em operação*. 
## Objetivos essenciais

1. Revelar defeitos e *reduzir risco* (**não provar ausência de defeitos**).
2. Fornecer *informação para decisão* (ex.: “pronto para liberar?”).
3. Aumentar a confiança na qualidade percebida.
4. Conformidade com requisitos, normas e contratos.
5. Prevenção (static testing identificando problemas antes de executar código). 


---

# Termos fundamentais (e como se relacionam)

``Erro`` (``mistake``) → ação **humana** que pode introduzir um problema (ex.: equívoco ao interpretar um requisito). 

``Defeito`` / ``bug`` / ``fault`` → **imperfeição** em um artefato (código, requisito, design) que pode causar uma falha quando executado/ativado. (IEEE 1044 trata fault como subtipo de defect.) 

``Falha`` (``failure``) → **comportamento** observável *diferente do esperado durante a execução* (**evidência** de que há um defeito). 


> *Linha do tempo mental*: Erro humano **→** insere um defeito **→** que, sob certas condições de execução, manifesta-se como falha. (NIST também relaciona com segurança: bug/fault/error/weakness/vulnerability.) 


## V&V (Verificação x Validação):

``Verificação``: “estamos construindo certo o produto?” (consistência com especificações/artefatos anteriores).

``Validação``: “estamos construindo o produto certo?” (atende às necessidades do usuário/negócio). (Definições consagradas em IEEE/SEI; excelente síntese em Paulk.) 


---

# Atividades estáticas x dinâmicas

``Estáticas``: inspecções, walkthroughs, revisões de requisitos/design/código, análise estática com ferramentas — sem executar o software.

``Dinâmicas``: execução do software ou partes dele (unitário, integração, sistema, etc.).
Objetivo prático: achar problemas o quanto antes (shift-left) para reduzir custo de correção. 


---

# Níveis, tipos e escopo (visão de alto nível)

``Níveis de teste`` (test levels): agrupamentos de atividades geridas em conjunto; clássicos: componente (unit), integração, sistema e aceitação. 

``Tipos de teste`` (test types): funcionais e não funcionais (p.ex. desempenho, segurança, usabilidade), além de confirmação e regressão em mudanças. (CTFL v4.0.1 consolida a taxonomia e relaciona a manutenção.) 

``Risco como guia`` (Risk-Based Testing): planejar, priorizar e dimensionar testes proporcionalmente ao risco do produto. 


---

# Artefatos e vocabulário que você vai usar sempre

``Caso de teste`` (test case): precondições, entradas, ações, resultados esperados e pós-condições, derivados de condições de teste. 

``Suíte de testes`` (test suite/set): coleção organizada de casos de teste para uma execução. 

``Oráculo de teste`` (test oracle): fonte do resultado esperado (manual, sistema legada, especificação, conhecimento especialista). 

``Base de testes`` (test basis): documentos que descrevem o que o sistema deve fazer (requisitos, épicos, modelos, normas), a partir dos quais derivamos testes. 

``Objetivo de teste`` (test objective): razão para desenhar/executar um teste (ex.: “validar cálculo de juros”). 

``Ambiente de teste``: hardware, ferramentas, dados e stubs/mocks para executar testes. 

``Testware``: tudo que produzimos/usar para testar (planos, casos, scripts, dados, procedimentos, configuradores). 

``Critérios de entrada/saída``: condições para começar e encerrar atividades/níveis de teste (evitam começar cedo demais ou “dar saída” sem cobertura mínima/risco aceitável). 


---

# Princípios clássicos de teste (pra levar para a vida)

1. Testes mostram *presença, não ausência* de defeitos.

2. Exaustividade é impossível (testar “tudo” não é viável).

3. Testar cedo economiza tempo e dinheiro.

4. Defeitos tendem a agrupar-se.

5. Paradoxo do pesticida (testes repetidos param de encontrar novos defeitos).

6. Teste depende do contexto.

7. “Sem defeitos” ≠ software útil (*ausência de defeitos não garante valor*).

(Fontes: ISTQB CTFL v4.0.1 e materiais oficiais da ASTQB.) 


---

# Qualidade de produto e características (ISO/IEC 25010)

Use o *modelo de qualidade* para ligar **tipos de teste** a **atributos de qualidade**. A edição 2023 alterou termos e acrescentou Safety como característica de topo;

> Usability → Interaction Capability e Portability → Flexibility

com ajustes de subcaracterísticas. (Ótimo para justificar testes não-funcionais em planos e risk-based testing.) 


---

# Independência e papéis

Quanto *mais independente for quem testa em relação a quem construiu*, **maior a chance de encontrar defeitos** diferentes e julgamentos mais objetivos, na prática, combina-se níveis: 

1. pessoa que codou
2. par do time
3. time de QA
4. auditor externo

Conforme contexto e custo/benefício.
(CTFL v4 traz “independence of testing”.) 


---

# Dicas operacionais

Ao definir um teste, sempre responda:
- *qual risco ataco*?
- *qual oráculo uso*?
- *qual qualidade/propriedade da ISO 25010 cubro*?

**Traceabilidade**: vincule caso de teste → condição → requisito/risco;
Isso ajuda em critério de saída e auditorias.

Mantenha termos consistentes (erro/defeito/falha, V&V, níveis/tipos, base/condição/objetivo), usando o glossário ISTQB como referência única. 
