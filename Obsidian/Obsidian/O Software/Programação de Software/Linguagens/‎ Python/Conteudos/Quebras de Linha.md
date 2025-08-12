[[Python|Voltar]]

## 📌 Quebras de Linha

- Limite linhas a *79 caracteres para códigos* e *comentários/docstrings devem ter até 72 caracteres* (PEP 8).
- Use `()` ou `\` para quebrar linhas longas.

```python
# Correto
valor_total = (valor_longo 
               + ajuste 
               - desconto)

# Errado
valor_total = valor_longo + ajuste - desconto  # linha ultrapassa 79 caracteres
```