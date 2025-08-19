---
data_criacao: 19-08-2025
flashcards: Não feito
revisão: Não feita
---
# 🔹 Teste de Integração

``Escopo``: interações entre unidades, módulos ou componentes.

``Foco``: defeitos em interfaces, protocolos de comunicação, troca de dados.

``Abordagens``:
- Top-down (do mais alto nível para baixo, usando stubs).
- Bottom-up (dos módulos básicos para cima, usando drivers).
- Sanduíche (mistura dos dois).
- Big Bang (tudo junto de uma vez → pouco recomendado em projetos grandes).

``Responsável típico``: desenvolvedores + suporte de testers.

``Exemplo``: verificar se o módulo de login integra corretamente com o banco de dados e o sistema de autenticação externo.