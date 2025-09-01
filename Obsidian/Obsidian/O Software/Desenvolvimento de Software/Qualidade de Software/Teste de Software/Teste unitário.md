---
data_criacao: 19-08-2025
flashcards: Não feito
revisão: Não feita
---
# 🔹 Teste de Unidade (Unitário / Componente)

``Escopo``: menor unidade testável de software (função, método, classe, módulo).

``Responsável típico``: o próprio desenvolvedor.

``Foco``: validar se o código funciona de acordo com o design de baixo nível.

``Técnicas comuns``: caixa-branca, TDD, mocks/stubs para dependências externas.

``Ferramentas``: JUnit, pytest, NUnit, Google Test.

``Benefício``: defeitos são encontrados cedo, quando mais baratos de corrigir.

``Exemplo``: testar se a função calcular_imposto() retorna o valor esperado com diferentes entradas.

## Quando fazer

Não necessariamente devemos escrever testes unitários para todas funções ou features que desenvolvermos. O ideal é buscar **boa cobertura de testes**, mas sem exagerar, testes também custam tempo e manutenção.

Como regra prática, podemos seguir:

- ✅ **Funções críticas** (cálculo, regras de negócio, manipulação de dados sensíveis) → sempre teste.
- ✅ **Funções com lógica complexa** → teste para evitar regressões.
- ❌ **Funções triviais** (ex: getter/setter, prints, wrappers muito simples) → geralmente não vale o esforço.

**Resumindo**: escreva testes para o que pode **quebrar** e causar dor de cabeça no futuro.

---

# Em Python

Em **Python**, usamos a biblioteca `pytest` para escrever testes unitários.  
Normalmente, criamos uma pasta chamada `tests/` para armazenar os arquivos de teste.

A convenção é nomear os arquivos de teste de forma parecida com os módulos que queremos testar, adicionando o sufixo `_test.py`.

Exemplo:
- Módulo: `calc.py`
- Teste: `calc_test.py`
![[Pasted image 20250827140138.png | center]]
## Assert

A palavra-chave `assert` pode ser entendida como **“garantir”**.  
Por exemplo, o código:

```python
assert resp == 4
```

pode ser lido como: _“garantir que a resposta seja 4”_.

| Assert                           | Significado                                 |
| -------------------------------- | ------------------------------------------- |
| `assert item in lista`           | garante que `item` está presente em `lista` |
| `assert item not in lista`       | garante que `item` não está em `lista`      |
| `assert isinstance(resp, float)` | garante que `resp` é `float`                |
| `assert raises(Exception)`       | garante que uma exceção foi lançada         |
## Executando pytest

Podemos executar no terminal `pytest` para executar todos os testes que fizemos. Entretanto, se rodar-mos `pytest -s -v` teremos mais informações.
![[Pasted image 20250901122047.png | center]]
