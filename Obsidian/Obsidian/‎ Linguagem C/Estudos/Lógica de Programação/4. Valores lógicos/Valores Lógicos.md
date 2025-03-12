---

---
Em C *não existe* nenhum tipo específico de dados para armazenar valores lógicos.

---
## Falso e Verdadeiro

> Em C o valor lógico **FALSO** é representado por **0**.
> Tudo aquilo que **seja diferente de 0** representa o valor lógico **VERDADEIRO**.

Observe o caso abaixo:
```c
	if (x!=0)
		printf("%d não é zero\n",x);
	else
		printf("%d é igual a zero",x);
```

<small>Quando <strong>x != 0</strong>, o resultado da avaliação da expressão x!=0 devolve o valor <strong>Verdade</strong>.<br>Ora, como x != 0  e tudo o que é diferente de zero representa Verdade, <strong>x representa por si só o valor lógico Verdade</strong>.</small>
 - Se verdade (x, que é qualquer valor), será feito tal
 - Se falso (0), será feito tal.
<small>Por isso, escrever <strong>(x!=0)</strong> ou <strong>(x)</strong> é exatamente a mesma coisa.</small>

```c
	if (x)
		printf("%d não é zero\n",x);
	else
		printf("%d é igual a zero",x);
```

Sabendo disso, o valor de uma variável ou de uma constante pode ser aproveitado pelo programador como valor lógico, utilizando-o como FALSO (caso 0) ou VERDADE (caso seja diferente de 0).

Entretanto, *não é recomendado usar apenas o x neste caso*, pois isso impactaria na legibilidade e compreensão alheia do <span class="red-neon">código</span>.

---
## Operadores Relacionais

Como já conhecemos bem os operadores relacionais, nos preocuparemos em pontuar os seguintes principais tópicos:

> **1.** Uma expressão que contenha um operador relacional *devolve sempre como resultado o valor lógico* VERDADE ou FALSO.

> **2.** Devemos sempre lembrar da diferença de igualdade a atribuição:
<center><big>== é igualdade<br>= é atribuição</big></center>

---
- Esteja sempre atento à [[Precedência dos Operadores Lógicos e Relacionais]].