[[Python|Voltar]]

Com **dois underscores** (`__dado`) ativam _name mangling_ (diferente de "privado").

`Exemplo`
```Python
class Exemplo:
    def __init__(self):
        self.__dado = "segredo"
```