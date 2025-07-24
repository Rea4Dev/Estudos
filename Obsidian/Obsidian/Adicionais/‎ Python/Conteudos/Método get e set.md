Em Python, os métodos get e set são comumente usados *para acessar e modificar os atributos de um objeto* de forma controlada, garantindo que as operações de leitura e escrita sejam feitas de maneira segura.

---

## *Método get* 🔎

Métodos get são usados para acessar valor de um atributo de um objeto.

Eles geralmente começam com o atributo get, e permitem que você obtenha o valor de um atributo, mas não o modifique diretamente.

```Python
class Carro:
	def __init__(self, marca, modelo, ano):
		self._marca = marca
		self._modelo = modelo
		self._ano = ano

	def get_marca(self):
		return self._marca
```

---

## *Método set* ⚙️

Métodos set são usados para modificar o valor de um atributo de um objeto.

Eles geralmente começam com o prefixo set. Eles permitem que você defina um novo valor para um atributo, *garantindo que qualquer lógica de validação necessária seja aplicada antes de fazer a modificação*.

```Python
class Carro:
	def __init__(self, marca, modelo, ano):
		self._marca = marca
		self._modelo = modelo
		self._ano = ano

	def set_marca(self, marca):
		self._marca = marca
```

---
# Exemplo Prático

```Python
class Carro:
	def __init__(self, marca, modelo, ano):
		self._marca = marca
		self._modelo = modelo
		self._ano = ano

	def get_marca(self):
		return self._marca

	def set_marca(self, marca):
		self._marca = marca

# Instanciando
meu_carro = Carro(marca = "Toyota", modelo = "Corolla", ano = 2020)

# get
print("Marca do carro: ", meu_carro.get_marca())

# set
meu_carro.set_marca("Honda")

# get
print("Marca do carro: ", meu_carro.get_marca())
```
