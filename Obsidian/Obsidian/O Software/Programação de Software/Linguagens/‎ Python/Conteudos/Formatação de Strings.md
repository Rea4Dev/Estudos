[[Índice Python|Voltar]]

## 📌 Formatação de Strings

- Prefira **f-strings** para formatação (Python 3.6+).
- Use `.join()` para concatenar listas de strings.

```python
# Correto
nome = "Carlos"
saudacao = f"Bem-vindo, {nome}!"

# Errado
saudacao = "Bem-vindo, " + nome + "!"  # concatenação ineficiente
```
