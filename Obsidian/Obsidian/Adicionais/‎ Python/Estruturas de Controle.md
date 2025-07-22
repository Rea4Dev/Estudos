[[Índice de Python|Voltar]]

## 📌 Estruturas de Controle

- Espaço após `if`, `for`, `while`.
- Use `elif` para cadeias condicionais.

```python
# Correto
if idade >= 18:
    print("Adulto")
elif idade > 12:
    print("Adolescente")
else:
    print("Criança")

# Errado
if idade>=18:  # sem espaço
    print("Adulto")
```
