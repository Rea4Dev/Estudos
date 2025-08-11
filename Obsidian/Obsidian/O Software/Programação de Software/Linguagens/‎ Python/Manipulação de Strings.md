---
data_criacao: 04-08-2025
flashcards: Não feito
revisão: Não feita
---
# Manipulação de Strings

Diretamente, strings são **imutáveis**.
```Python
nome = 'Maria'

nome[0] = 'm'

# Não funcionará!
```
Entretanto, podemos utilizar métodos para manipulá-las.

## Métodos

Python oferece alguns métodos úteis para manipulação de strings:

- string *.find(p)* -> retorna o índice em que a substring p aparece 
- string *.count(p)* -> retorna a frequência em que a substring p aparece 
- string *.replace(p, q)* -> substitui a substring p pela substring q 
- string *.capitalize()* -> primeiro caractere fica maiúsculo
- string *.upper()* -> todos caracteres maiúsculos
- string *.lower()* -> todos caracteres minúsculos
- string *.strip()* -> remove espaços em branco em excesso