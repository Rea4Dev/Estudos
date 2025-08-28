---
data_criacao: 28-08-2025
flashcards: Não feito
revisão: Não feita
---
# Operadores Lógicos e Aritméticos em Java

Um guia prático e direto para consulta no dia a dia, com exemplos curtos e dicas para evitar armadilhas.

## Visão geral rápida

- Aritméticos: `+`, `-`, `*`, `/`, `%`, `++`, `--`
- Atribuição composta: `+=`, `-=`, `*=`, `/=`, `%=`
- Relacionais e igualdade: ` ==`, `!=`, `<`, `>`, `<=`, `>=`
- Lógicos (booleanos): `&&`, `||`, `!`, `^`
- Condicional (ternário): `?:`
- Complemento útil: bit a bit `&`, `|`, `^`, `~`, `<<`, `>>`, `>>>`

---

# Operadores aritméticos

- `+` soma
- `-` subtração
- `*` multiplicação
- `/` divisão
- `%` resto (módulo)

```java
int a = 7, b = 3;
System.out.println(a + b); // 10
System.out.println(a - b); // 4
System.out.println(a * b); // 21
System.out.println(a / b); // 2  (divisão inteira trunca)
System.out.println(a % b); // 1
```

## Regras importantes

- Divisão inteira trunca em direção a zero:

```java
System.out.println(7 / 3);   // 2
System.out.println(-7 / 3);  // -2
```

- Resto com negativos segue o sinal do dividendo:

```java
System.out.println(-7 % 3);  // -1
System.out.println(7 % -3);  // 1
```

- Divisão por zero:

```java
System.out.println(5 / 0);    // ArithmeticException
System.out.println(5.0 / 0);  // Infinity
System.out.println(0.0 / 0.0);// NaN
```

- Promoção numérica: operações entre tipos inteiros menores promovem a `int`; presença de `double` leva o resultado a `double`.

```java
byte x = 10, y = 20;
int r = x + y;       // promove a int
double d = 1 + 2.5;  // 3.5 (promove a double)
```

- Overflow em inteiros é silencioso:

```java
int m = Integer.MAX_VALUE;
System.out.println(m + 1); // -2147483648 (overflow)
```

> [!warning] Dinheiro não é `double` Para valores monetários, prefira `BigDecimal` para evitar erros de ponto flutuante.

---

## Incremento e decremento

- `++x` pré-incremento
- `x++` pós-incremento
- `--x`, `x--` análogo

```java
int n = 5;
System.out.println(n++); // 5 (usa, depois incrementa)  n = 6
System.out.println(++n); // 7 (incrementa, depois usa)
```

> [!tip] Evite efeitos colaterais Não misture muitos `++`/`--` na mesma expressão. Prefira linhas separadas para legibilidade.

---

## Atribuição composta

- `+=`, `-=`, `*=`, `/=`, `%=` aplicam a operação e atribuem.
- Fazem conversão implícita para o tipo da variável à esquerda.

```java
byte b1 = 1;
b1 += 1;      // ok (conversão implícita)
/// b1 = b1 + 1; // erro: resultado é int
```

---

## Relacionais e igualdade

- ` ==`, `!=`, `<`, `>`, `<=`, `>=` retornam `boolean`.

```java
int a = 3, b = 5;
System.out.println(a < b);  // true
System.out.println(a == b); // false
```

Objetos: ` ==` compara referências; `.equals()` compara conteúdo (quando implementado).

```java
String s1 = new String("java");
String s2 = new String("java");
System.out.println(s1 == s2);      // false (refs diferentes)
System.out.println(s1.equals(s2)); // true  (conteúdo igual)
```

---

# Lógicos (booleanos)

- `&&` e curto-circuito
- `||` ou curto-circuito
- `!` negação
- `^` ou exclusivo (XOR) booleano

```java
boolean ok = true, fail = false;
System.out.println(ok && fail); // false
System.out.println(ok || fail); // true
System.out.println(!ok);        // false
System.out.println(ok ^ fail);  // true
```

## Curto-circuito e ordem de avaliação

- Em `A && B`, se `A` for `false`, `B` não é avaliado.
- Em `A || B`, se `A` for `true`, `B` não é avaliado.
- Avaliação é da esquerda para a direita.

```java
String s = null;
if (s != null && s.length() > 0) {
    // seguro
}

if (s != null & s.length() > 0) {
    // perigoso: & avalia ambos os lados -> pode lançar NullPointerException
}

int i = 0;
boolean r = (i++ == 0) && (i++ == 1);
System.out.println(r); // true
System.out.println(i); // 2
```

> [!tip] De Morgan `!(A && B)` é equivalente a `(!A || !B)` e `!(A || B)` equivale a `(!A && !B)`.

---

## Condicional ternário

Forma compacta de `if-else`. Estrutura: `condicao ? valorSeVerdadeiro : valorSeFalso`.

```java
int x = -8;
int abs = x >= 0 ? x : -x;
String status = abs > 10 ? "alto" : "ok";
```

---

## Complemento: bit a bit e deslocamento

Úteis para flags e operações de baixo nível (com tipos inteiros).

- Bit a bit: `&` (AND), `|` (OR), `^` (XOR), `~` (NOT)
- Deslocamentos: `<<` (esquerda), `>>` (direita aritmético), `>>>` (direita lógico)

```java
int mask  = 0b0101;
int flags = 0b0011;

int and = flags & mask; // 0001
int or  = flags | mask; // 0111
int xor = flags ^ mask; // 0110
int not = ~flags;       // complemento de 2

int v = -8;
System.out.println(v >> 1);   // -4 (preserva sinal)
System.out.println(v >>> 1);  // grande positivo (preenche com zero)
```

---

## Precedência e associatividade essenciais

Da mais alta para a mais baixa (resumo do que mais importa no dia a dia):

1. Unários: `+`, `-`, `!`, `~`, `++`, `--`, cast
2. Multiplicativos: `*`, `/`, `%`
3. Aditivos: `+`, `-`
4. Deslocamentos: `<<`, `>>`, `>>>`
5. Relacionais: `<`, `<=`, `>`, `>=`, `instanceof`
6. Igualdade: ` ==`, `!=`
7. Bit a bit: `&`, `^`, `|`
8. Lógicos: `&&`, `||`
9. Ternário: `?:`
10. Atribuições: ` =`, `+=`, `-=`, `*=`, `/=`, `%=`, `&=`, `^=`, `|=`, `<<=`, `>>=`, `>>>=`

> [!tip] Quando em dúvida, use parênteses Parênteses tornam a intenção explícita e evitam bugs sutis.

---

## Pitfalls comuns e boas práticas

- Evite comparar `double` com ` ==`; use tolerância (`epsilon`) ou `BigDecimal` para finanças.
- Prefira parênteses a confiar só na precedência.
- Cuidado com overflow em `int` e `long`; para checagem, use `Math.addExact`, `Math.multiplyExact` (lançam exceção em overflow).
- Evite múltiplos `++`/`--` na mesma expressão.
- Use `&&`/`||` no lugar de `&`/`|` para booleanos na maioria dos casos, por causa do curto-circuito.

```java
double a = 0.1 * 3;       // 0.30000000000000004
double b = 0.3;
System.out.println(Math.abs(a - b) < 1e-9); // true (comparação com tolerância)
```
