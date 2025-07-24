## Introdução
- PEP8 é o guia de estilo oficial para código Python, focado em legibilidade e consistência.
- Objetivo principal: facilitar a leitura e manutenção de código por humanos.
- Aderir ao PEP8 melhora a colaboração em projetos e integração com ferramentas de análise estática.
## Principais Regras e Recomendações

### 1. *Indentação*
- Use 4 espaços por nível de indentação.
- Evite tabs; configure o editor para converter tabs em espaços.
- Exemplo correto:
  ```python
  if condição:
      print("Indentação com 4 espaços")
  ```

### 2. *Tamanho de Linha*
- Limite máximo: 79 caracteres para código, 72 para comentários/docstrings.
- Quebre linhas usando `\` ou parênteses/colchetes/chaves para continuação implícita.

### 3. *Espaçamento*
- Uma linha em branco entre funções e classes.
- Dois espaços em branco entre seções lógicas em arquivos.
- Evite espaços:
  - Imediatamente dentro de parênteses, colchetes ou chaves.
  - Antes de `(`, `[`, ou após `]`, `)`, `}`.
- Use um espaço após vírgulas e dois pontos.

### 4. *Imports*
- Agrupe imports na seguinte ordem, separados por linhas em branco:
  1. Bibliotecas padrão
  2. Dependências de terceiros
  3. Módulos locais/aplicação
- Evite imports relativos (ex: `from .modulo import x`).
- Exemplo:
  ```python
  import os
  import sys

  from flask import Flask
  import pandas as pd

  from meuprojeto import utils
  ```

### 5. *Nomes*
- **Funções/Variáveis:** `snake_case` (ex: `calcular_total`)
- **Classes:** `CamelCase` (ex: `ClienteAtivo`)
- **Constantes:** `UPPER_CASE` (ex: `TAXA_JUROS`)
- **Métodos:** Use `self` como primeiro parâmetro em métodos de instância.
- **Variáveis privadas:** Prefixo `_` (ex: `_dado_interno`).

### 6. *Comentários*
- Comentários de bloco: frases completas, iniciando com maiúscula.
- Comentários em linha: raros e focados em explicações não óbvias.
- Atualize comentários junto com alterações no código.

### 7. **Docstrings**
- Use o formato convencional (Google Style, NumPy, ou reST).
- Inclua propósito, parâmetros, retorno e exceções.
- Exemplo:
  ```python
  def calcular_media(valores):
      """Calcula a média aritmética de uma lista de números.

      Args:
          valores (list): Lista de valores numéricos.

      Returns:
          float: Média dos valores. Retorna 0 se a lista estiver vazia.
      """
      if not valores:
          return 0.0
      return sum(valores) / len(valores)
  ```

### 8. **Comparações e Booleanos**
- Use `is`/`is not` para comparações com `None` ou booleanos.
- Evite comparar booleanos explicitamente (ex: `if ativo:` em vez de `if ativo == True`).

### 9. **Tratamento de Exceções**
- Capture exceções específicas, nunca `except:` vazio.
- Documente exceções em docstrings quando relevantes.
- Exemplo:
  ```python
  try:
      arquivo = open("dados.txt")
  except FileNotFoundError:
      print("Arquivo não encontrado")
  ```

### 10. **Formatação de Strings**
- Prefira f-strings (Python 3.6+) para formatação:
  ```python
  nome = "Maria"
  print(f"Olá, {nome}!")
  ```

---

## Ferramentas para Verificação
- **Linters:** `flake8`, `pylint`, `pycodestyle`
- **Autoformatadores:** `black`, `autopep8`, `yapf`
- **Configuração em IDEs:** VS Code (Python extension), PyCharm (habilitar inspeção PEP8)

---

## Exceções ao PEP8
- Quebre regras apenas quando:
  - Melhorar a legibilidade em casos específicos.
  - Necessário para compatibilidade com código legado.
  - Diretrizes de projeto exigirem estilo diferente.

---

## Citações Relevantes
- "A legibilidade conta." — Princípio Zen do Python.
- "Consistência é mais importante que perfeição." — Guia PEP8.

---

## Referências
- [Documentação Oficial PEP8](https://www.python.org/dev/peps/pep-0008/)
- [Guia de Docstrings](https://google.github.io/styleguide/pyguide.html)
- [Ferramenta Black (Autoformatador)](https://github.com/psf/black)

```python
# Zen do Python (import this)
"""
Bonito é melhor que feio.
Explícito é melhor que implícito.
Simples é melhor que complexo.
...
"""
```