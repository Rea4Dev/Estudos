[[Índice Python|Voltar]]

O método _ _ init _ _ () em Python é um ``método construtor`` usado para *inicializar objetos quando eles são criados* a partir de uma classe.

É chamado automaticamente assim que um novo objeto é instanciado, ou seja, quando você cria uma instância da classe.

```Python
class Carro:
	def __init__(self, marca, modelo, ano):
		self.marca = marca
		self.modelo = modelo
		self.ano = ano
```