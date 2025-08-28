---
data_criacao: 14-08-2025
flashcards: Não feito
revisão: Não feita
---

---
# Tipos de Referência (Objetos)

Tipos mais complexos, que possuem estados e comportamentos. São definidos por Classes.

```Java
Pessoa pessoa1 = ...
```

## Diferença entre Primitivo e Referência

O tipo primitivo armazena diretamente o valor (ex.: int idade = 25;).

Já o tipo de referência, diferente do primitivo, não guarda o valor em si. Ele armazena uma referência (uma espécie de endereço), que aponta para onde os valores, estados e comportamentos estão efetivamente armazenados na memória da JVM.

![[Pasted image 20250814102505.png | center]]

As Classes são as responsáveis por definir esses tipos de referência.
O programador manipula os objetos através dessa referência.

## Instâncias

O que acontece com uma variável de tipo de objeto que não foi instanciada?
Ela fica com valor null (ou seja, sem referência para nenhum objeto na memória).

![[Pasted image 20250814105327.png | center]]

Ao utilizar o construtor para instanciar, a variável passa a armazenar uma referência válida.
Assim, o objeto existe na memória e pode ser manipulado.

![[Pasted image 20250814105522.png | center]]
