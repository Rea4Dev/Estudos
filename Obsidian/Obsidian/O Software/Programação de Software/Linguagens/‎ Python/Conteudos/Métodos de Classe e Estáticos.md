[[Python|Voltar]]

Métodos de classe usam `cls` como primeiro parâmetro.
`Exemplo`
```Python
class Exemplo:
    @classmethod
    def criar(cls, valor):
        return cls(valor)
```


- Métodos estáticos não usam `self` ou `cls` .
`Exemplo`
```Python
class Exemplo:
    @staticmethod
    def utilidade(x, y):
        return x + y
```