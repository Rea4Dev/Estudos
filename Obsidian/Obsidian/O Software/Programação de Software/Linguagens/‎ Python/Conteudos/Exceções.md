[[Python|Voltar]]

Nomes de exceções devem usar `CamelCase` e terminar com "Error".

`Exemplo`
```Python
class MeuError(Exception):
    pass

raise MeuError("Algo deu errado!")
```