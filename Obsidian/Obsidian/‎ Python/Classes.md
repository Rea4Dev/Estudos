[[Índice de Python|Voltar]]
# O que são Objetos?
São ==entidades que representam conceitos, com propriedades e ações==. São formados por dados (variáveis) e métodos (funções).

# O que são Classes?
Classes são basicamente ==moldes== para que seja feita a criação de objetos a partir deles.

## Conceitos Importantes
Abaixo estão conceitos que serão úteis para o entendimento:

`Atributos`
	São as informações armazenadas de uma classe.
```Python
class Carro:
	def __init__(self, marca, modelo, ano):
		self._marca = marca    # Atributo
		self._modelo = modelo  # Atributo
		self._ano = ano        # Atributo
```

`Instanciar`
	É o ato de atribuir uma instância de classe a uma variável
```Python
#variável    [                  instância                            ]
meu_carro  =  Carro(marca = "Toyota", modelo = "Corolla", ano = 2020)
```

`Acessando`
	A partir do momento que uma variável recebe uma instância de classe, ele se torna um objeto. Para acessar objetos de um objeto, usa-se um ponto após seu nome, e então, qual objeto queremos acessar.
```Python
meu_carro.nome # Sairia "Toyota"
```

---
# Métodos
Os métodos de uma classe são as ações que os objetos criados a partir daquela classe podem realizar.

Usamos "def" para criar os métodos. Colocamos como primeiro argumento o "self", que utilizamos para acessar os atributos de toda a classe. 
Após (se existir), inserimos os argumentos que esta classe utilizará.

```Python
def get_marca(self):
		return self._marca
```

## Método Init
O método _ _ init _ _ () em Python é um ``método construtor`` usado para *inicializar objetos quando eles são criados* a partir de uma classe.

É chamado automaticamente assim que um novo objeto é instanciado, ou seja, quando você cria uma instância da classe.

```Python
class Carro:
	def __init__(self, marca, modelo, ano):
		self.marca = marca
		self.modelo = modelo
		self.ano = ano
```

## Método get 🔎
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

## Método set ⚙️
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

## Exemplo Geral

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

# Alternativa: DataClasses

Uma alternativa é o uso de DataClasses! 
Grande parte dos conceitos acima ainda são aplicáveis, com a diferença que agora a usuabilidade e leitura ficam facilitadas. Também informa qual o tipo do atributo. 

Outra vatagem é na impressão, pois caso você não forneça o objeto (atributo) que quer acessar, ele imprimirá tudo! 

```Python
from dataclasses import dataclass

@dataclass
class Cliente:
	nome: str
	email: str
	idade: int
	
	def apresentar(self):
		print(f"Meu nome é {self.nome}")

Rea = Cliente(nome="Rea", email="Rea4dev@dev.com", idade=20)

Rea.apresentar()

print(Rea) # Da forma clássica, isso aqui daria erro
```

Uma curiosidade é que o DataClasses apresenta as classes de uma forma visualmente mais próxima a como fazemos em Banco de Dados Relacionais, informando a classe, os atributos com seus tipos e abaixo os métodos:

![[Pasted image 20250330142255.png | center | 300]]

---
# Testes
```Python
class Action:
	def __init__(self, id, datetime, valor):
		self._id = id
		self._datetime = datetime
		self._valor = valor

	def get_id(self):
		return self._id

	def get_datetime(self):
		return self._datetime

	def get_valor(self):
		return self._valor

# Instanciando
action1 = Action(id = 32550138, datetime = "02-APR-25 10.01.16.674000000 AM", valor = 134)

for i in range(1, 6):
	Action

# get
print("Action ID: ", action1.get_id())

```