[[Índice de Python|Voltar]]

## 📌 Tratamento de Exceções

- Seja **específico** ao capturar exceções.
- Capture exceções específicas, nunca `except:` vazio.
- Documente exceções em docstrings quando relevantes.

```python
# Correto
try:
    arquivo = open("dados.txt")
except FileNotFoundError:
    print("Arquivo não encontrado!")

# Errado
try:
    arquivo = open("dados.txt")
except:  # captura qualquer erro
    pass  # ignora a exceção
```
