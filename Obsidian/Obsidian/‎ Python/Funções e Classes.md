[[Índice de Python|Voltar]]

## 📌 *Funções e Classes*

- **2 linhas em branco** antes de funções/classes de nível superior.
- Métodos em classes separados por **1 linha em branco**.

```python
# Correto
def processar_dados():
    pass


class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        pass

# Errado
def funcao1(): pass
def funcao2(): pass  # sem espaços entre funções
```
