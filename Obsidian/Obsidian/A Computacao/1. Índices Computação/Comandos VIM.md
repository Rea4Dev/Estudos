---
data_criacao: 28-08-2025
flashcards: Não feito
revisão: Não feita
---

---

# Comandos e Navegação no VIM

## Modos do VIM

- **Normal**: Navegação e comandos (padrão ao abrir).
- **Inserção**: Digitação de texto (`i`, `a`, `o`).
- **Visual**: Seleção de texto (`v`, `V`, `Ctrl+v`).
- **Linha de Comando**: Comandos iniciados com `:`.

---

## Navegação Básica

- `h` → Esquerda
- `l` → Direita
- `j` → Linha abaixo
- `k` → Linha acima
- `0` → Início da linha
- `^` → Primeiro caractere não vazio
- `$` → Fim da linha
- `w` → Próxima palavra
- `e` → Fim da palavra
- `b` → Início da palavra
- `gg` → Início do arquivo
- `G` → Fim do arquivo
- `:n` → Ir para linha n

---

## Inserção de Texto

- `i` → Inserir antes do cursor
- `a` → Inserir após o cursor
- `o` → Nova linha abaixo
- `O` → Nova linha acima

---

## Edição

- `x` → Apagar caractere
- `dd` → Apagar linha
- `yy` → Copiar linha
- `p` → Colar após
- `P` → Colar antes
- `u` → Desfazer
- `Ctrl+r` → Refazer
- `r<char>` → Substituir caractere
- `cw` → Alterar palavra
- `cc` → Alterar linha

---

## Busca e Substituição

- `/texto` → Buscar para frente
- `?texto` → Buscar para trás
- `n` → Próxima ocorrência
- `N` → Ocorrência anterior
- `:%s/antigo/novo/g` → Substituir em todo arquivo
- `:s/antigo/novo/g` → Substituir na linha atual

---

## Trabalhando com Arquivos

- `:w` → Salvar
- `:q` → Sair
- `:wq` ou `:x` → Salvar e sair
- `:q!` → Sair sem salvar
- `:e arquivo` → Abrir arquivo
- `:w arquivo` → Salvar como

---

## Janelas e Abas

- `:split` ou `:sp` → Dividir horizontal
- `:vsplit` ou `:vsp` → Dividir vertical
- `Ctrl+w w` → Alternar janelas
- `:tabnew` → Nova aba
- `gt` → Próxima aba
- `gT` → Aba anterior

---

## Dicas Úteis

- `.` → Repete último comando
- `:help comando` → Ajuda sobre comando
- `Ctrl+g` → Mostra posição no arquivo
- `:%y+` → Copiar todo arquivo para área de transferência

---
