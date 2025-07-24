# 📜 Manifesto de Fixação de Conteúdos — v1.0

Sistema pessoal de consolidação do conhecimento, aplicado no Obsidian.md + extensão de Flashcards.

---

## 🧠 Princípio Fundamental

> "A memória falha, o sistema corrige."

Sempre que terminar de estudar algo, **fica a seu critério** criar flashcards ou não.

O que se torna **regra inegociável** é:

> **Sempre que falhar em lembrar de algo estudado, investigue a origem dessa falha.**

---

## 🔍 Processo em caso de falha

1. **Verifique se o assunto estava registrado no Obsidian.**

   - ❌ **Não estava?**
     - Você não tinha como lembrar.
     - ➤ Registre o conteúdo agora no Obsidian.

   - ✅ **Estava?**
     - Sua memória falhou.
     - ➤ Crie um flashcard **específico** sobre a informação que falhou.

---

## 🔄 Revisão e Manutenção

A extensão de Flashcards cuidará da lógica de repetição (revisão espaçada) com base no seu desempenho. Confie nela.

---

## ⚠️ Pontos de Atenção

- Nem sempre você errará o que está esquecendo.
  - ➤ Considere revisões periódicas do conteúdo já estudado mesmo sem falhas detectadas.

- Revisão não é punição. É refinamento.
  - ➤ Relembrar é consolidar.

---

## ✍️ Atualizações Futuras

Este manifesto é um organismo vivo.
Sempre que uma melhoria for percebida, **registre e versione.**

---

> _"O conhecimento que não é revisado se apaga como traço na areia."_

# Engenharia de Software
## Modelagem de Dados
#EngSoft/Modelagem_de_Dados

ES1) O que é um SGBD?::Software para gerenciar, organizar, acessar, controlar e proteger informações de um banco de dados.



ES2) Qual o principal objetivo de um SGBD?
^
Facilitar a vida do programador/analista, abstraindo os detalhes técnicos de armazenamento de dados.
<!--SR:!2025-07-15,8,250-->
%

ES3) O que é abstração de dados em um SGBD?
^
Esconder os detalhes físicos de armazenamento e transações, apresentando uma visão conceitual dos dados.
<!--SR:!2025-07-09,2,230-->
%

ES4) No contexto de SGBDs, o que significa o termo "aplicação"?
^
Softwares que consomem os dados armazenados em um banco de dados.
<!--SR:!2025-07-18,11,270-->
%

ES5) O que são nós em um SGBD distribuído?
^
Locais físicos diferentes onde o banco de dados está distribuído.
<!--SR:!2025-07-09,2,230-->
%

ES6) Por que o SGBD utiliza protocolos de comunicação?
^
Para permitir a comunicação entre os nós distribuídos do banco de dados.
<!--SR:!2025-07-08,1,210-->
%

ES7) Quais os principais objetivos de segurança de um SGBD?
^
Garantir integridade e proteção dos dados contra falhas e acessos indevidos.
<!--SR:!2025-07-08,1,210-->
%

ES8) O que é uma transação em um SGBD?
^
Processo/programa que realiza consultas, alterações ou exclusões no banco de dados.
<!--SR:!2025-07-08,1,210-->
%

ES9) O que significa a sigla ACID em SGBDs?
^
Atomicidade, Consistência, Isolamento e Durabilidade.
<!--SR:!2025-07-08,1,210-->
%

ES10) O que é Atomicidade?
^
Ou todas as operações da transação são concluídas, ou nenhuma é (tudo ou nada).
<!--SR:!2025-07-09,2,250-->
%

ES11) O que é Consistência?
^
Garante que o banco permaneça em um estado válido após uma transação.
<!--SR:!2025-07-08,1,210-->
%

ES12) O que é Isolamento?
^
Assegura que transações concorrentes não interfiram umas nas outras.
<!--SR:!2025-07-22,15,290-->
%

ES13) O que é Durabilidade?
^
Garante que os efeitos de uma transação concluída permaneçam no banco, mesmo após falhas de sistema.
<!--SR:!2025-07-10,3,250-->
%

ES14) Para que serve o Log de Transação?
^
Registrar todas as operações realizadas para permitir recuperação em caso de falha.
<!--SR:!2025-07-09,2,250-->
%

ES15) Quais as principais características de um SGBD segundo Navathe e Ramez (2005)?
^
- Natureza autodescritiva
- Isolamento entre programas e dados
- Suporte a múltiplas visões
- Suporte a transações simultâneas e compartilhamento de dados
<!--SR:!2025-07-08,1,210-->
%

ES16) O que é uma Visão (View)?
^
Uma forma de exibir uma parte específica dos dados de forma controlada.
<!--SR:!2025-07-08,1,210-->
%

ES17) Por que usar Visões (Views) em um SGBD?
^
- Controle de segurança
- Simplificação de consultas
- Controle de acesso a colunas sensíveis
<!--SR:!2025-07-09,2,230-->
%

ES18) O que significa "Manipulação de Estrutura" em SGBDs?
^
Capacidade de definir, alterar e aplicar restrições na estrutura do banco de dados, de forma independente das aplicações.
<!--SR:!2025-07-08,1,210-->
%
