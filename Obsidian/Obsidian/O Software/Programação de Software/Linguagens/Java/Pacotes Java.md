---
data_criacao: 13-08-2025
flashcards: Não feito
revisão: Não feita
---
Pacotes agrupam objetos *semelhantes*.
Em Java, pacotes agrupam classes. Você pode pensar nesses pacotes como diretórios do computador mesmo.

# Nome completo Qualificado

## Situação Problema

Pense que uma **empresa A** crie uma classe User em seu pacote.

Entretanto, ela resolve um problema que a *empresa B* também tem, então a *empresa B* decide usar um pacote da **empresa A**.

Só que... e se a *empresa B* também possuir uma classe User?

É justamente isso que o Nome Completo Qualificado busca distinguir.

## Como funciona

A ideia prática seria semelhante a identificar um humano pelo seu nome completo ao invés de apenas primeiro nome.

João podem ser muitas pessoas. Seria um conflito em empresa A com empresa B.
Já João Pedro França 6/7/2001 é extremamente provável de corresponder a apenas uma pessoa. Evitando conflito.

Desta forma, para nomear pacotes com **Nome Completo Qualificado**, seguimos a convenção abaixo.

`use letras minúsculas para o nome do pacote`
```Java
package <sigla país>.com.<empresa>.<nome do projeto>;
```

![[Pasted image 20250813133845.png | center]]

> Classes dentro do mesmo pacote podem chamar metodos uma das outras!