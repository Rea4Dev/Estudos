[[Índice de Python|Voltar]]

## 📌 Type Hints

- Adicione **anotações de tipo** para funções e variáveis.
- Melhora a legibilidade e suporte a ferramentas de análise.
- Opcional, porém recomendado para código mais explícito (PEP 484).

```python
# Correto
def multiplicar(a: float, b: float) -> float:
    return a * b

# Errado (sem type hints)
def multiplicar(a, b):
    return a * b
```
