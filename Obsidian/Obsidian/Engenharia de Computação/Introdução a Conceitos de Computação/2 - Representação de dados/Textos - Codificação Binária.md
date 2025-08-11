---
data_criacao: 05-08-2025
flashcards: Não feito
revisão: Não feita
---
> [!Definição]  
> A **codificação binária de texto** é o processo de representar caracteres (letras, números, símbolos) em formato binário, permitindo que sejam **armazenados, processados e transmitidos por sistemas digitais**.

Essa codificação estabelece um **mapeamento entre caracteres e sequências de bits**, sendo essencial para a comunicação entre software, hardware e redes.

# Principais Formatos de Codificação

## `UTF-8` — Unicode Transformation Format 8-bit

- Codificação variável: **de 8 a 32 bits por caractere**
- Compatível com ASCII nos primeiros 128 caracteres
- **Padrão dominante na web** e em sistemas modernos
- Otimiza espaço ao usar menos bits para caracteres comuns

## `EBCDIC` — Extended Binary Coded Decimal Interchange Code

- Codificação desenvolvida pela **IBM**
- Usa **8 bits por caractere**
- Ainda encontrada em sistemas mainframe
- Pouco utilizada em ambientes modernos

## `ASCII` — American Standard Code for Information Interchange

- Codifica **128 caracteres** em **7 bits**
- Caractere adicional de **paridade** pode ser adicionado para verificação de erro
- Suporta letras, números, sinais de pontuação e caracteres de controle (ex: `\n`, `\t`)
- Base das codificações modernas

## `Unicode`

- Criado para representar **caracteres de todos os idiomas**
- Cada caractere ocupa, na versão básica (UTF-16), **16 bits**
- Resolve a limitação de abrangência do ASCII

## Comparativo

| Codificação | Tamanho   | Características principais                   |
| ----------- | --------- | -------------------------------------------- |
| `EBCDIC`    | 8 bits    | Legado, IBM mainframes                       |
| `ASCII`     | 7+1 bits  | Simples, eficiente, limitado a inglês        |
| `Unicode`   | 16 bits   | Universal, abrange múltiplos alfabetos       |
| `UTF-8`     | 8–32 bits | Compacto, escalável, padrão atual de mercado |
