[[Python|Voltar]]

## 📌 Docstring

DocStrings são strings de documentação em Python usadas para descrever o propósito e funcionamento de *módulos*, *classes* e *funções*. Elas são definidas entre três aspas duplas ou simples e podem ser acessadas via `__doc__`. Boas práticas recomendam que sejam claras, concisas e sigam o estilo PEP 257.

```Python
def somar_dois(num1: float, num2: float) -> float:
    """Calcula e retorna a soma entre dois números reais.
    
    Args:
        a: float: Primeiro valor real
        b: float: Segundo valor real
    
    Returns:
        float: A soma dos dois números
    
    Raises:
        TypeError: Se os argumentos não forem números reais.
    """
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)): # isinstance verifica se o valor é do tipo especificado, primeiro argumento é o valor, segundo argumento é o tipo
        raise TypeError("Os argumentos devem ser números reais.")
    return num1 + num2

#help(somar_dois)  # Forma 01 de acessar para que serve

#print(somar_dois.__doc__)  # Forma 02 de acessar para que serve

print(somar_dois(1, 2))  # Teste da função
print(somar_dois(1.0, 2.0))  # Teste da função
#print(somar_dois("A", 2.0))  # Teste da função
```

- Use o formato convencional (Google Style, NumPy, ou reST).
- Inclua propósito, parâmetros, retorno e exceções.
- Usar `"""` seguindo o estilo **[PEP 257](https://peps.python.org/pep-0257/)**
- Devem ser o **primeiro elemento** após declarações de funções/classes/módulos
- Devem explicar:
     - Propósito da função/classe
     - Parâmetros (tipos e descrição)
     - Valor de retorno
     - Exceções relevantes

### Exemplos Práticos

```python
# ✔️ CORRETO - Docstring completa e formatação adequada
def calcular_media(valores: list[float]) -> float:
    """Calcula a média aritmética de uma lista numérica.
    
    Args:
        valores (list[float]): Lista de valores numéricos (não vazia)
    
    Returns:
        float: Média calculada
        
    Raises:
        ZeroDivisionError: Se a lista estiver vazia
    """
    if not valores:
        raise ValueError("Lista não pode ser vazia")
    return sum(valores) / len(valores)


# ❌ ERRADO - Abreviações, falta de docstring e formatação ruim
def calc_media(v):  # Calcula média dos valores
    return sum(v)/len(v)  # Divisão sem tratamento de erro
```

### ✨ Dicas de Uso

- **Docstrings VS Comentários**:
  - Docstrings são para **documentação técnica** (usuários da função)
  - Comentários explicam **decisões complexas** (desenvolvedores)

- **Boas práticas**:
  ```python
  # ✔️ Use para documentação pública
  def converter_para_fahrenheit(celsius: float) -> float:
      """Converte temperatura de Celsius para Fahrenheit.
      
      Args:
          celsius (float): Temperatura em graus Celsius
          
      Returns:
          float: Temperatura equivalente em Fahrenheit
      """
      return (celsius * 9/5) + 32

  # ✔️ Comentário útil para lógica complexa
  def fatorial(n: int) -> int:
      # Usa recursão de cauda para otimização de memória
      def auxiliar(acc: int, m: int) -> int:
          return acc if m == 0 else auxiliar(acc * m, m - 1)
      return auxiliar(1, n)
  ```

- **Ferramentas**:
  - Use `help()` no interpretador para visualizar docstrings
  - IDEs modernas (VS Code, PyCharm) exibem docstrings em tooltips
  - Ferramentas como Sphinx geram documentação automática a partir de docstrings

---

### Principais Erros a Evitar

1. **Docstrings deslocadas**:
   ```python
   def funcao_errada():
       print("Executando...")
       """Docstring posicionada erroneamente"""  # ❌ Não funciona como documentação
   ```

2. **Comentários óbvios**:
   ```python
   x = x + 1  # Incrementa x  # ❌ Redundante
   ```

3. **Docstrings genéricas**:
   ```python
   def processar():
       """Processa os dados."""  # ❌ Não explica o que faz
   ```

4. **Misturar idiomas**:
   ```python
   # ❌ Evite misturar inglês e português
   def get_idade():  # Retorna idade do usuário
       """Returns user age."""
       ...
   ```

Esta versão inclui exemplos mais completos, destaca erros comuns e traz orientações práticas para diferentes cenários. Mantive o português como idioma principal, mas adapte para inglês se for o padrão do seu projeto!