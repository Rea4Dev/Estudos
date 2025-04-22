Listas possuem diversos métodos que auxiliam no gerenciamento dos dados. Alguns dos mais usados são:

``append():`` 
	adiciona um item ao final da lista.

``insert():`` 
	insere um item em uma posição específica.

``remove():`` 
	remove o primeiro item com o valor especificado.

``pop():`` 
	remove e retorna o item de uma posição (ou o último item, se nenhum índice for especificado).

``sort():`` 
	ordena a lista.

``reverse():`` 
	inverte a ordem da lista.

``count():`` 
	retorna o número de ocorrências de um item.

``index():`` 
	retorna o índice do primeiro item encontrado com o valor especificado.


```Python
frutas = ["maçã", "banana", "laranja"]

# Adicionando um elemento
frutas.append("kiwi")
print(frutas)

# Inserindo um elemento na posição 1
frutas.insert(1, "abacaxi")
print(frutas)

# Removendo um elemento
frutas.remove("laranja")
print(frutas)

# Removendo e retornando o último elemento
ultimo = frutas.pop()
print(f"Item removido: {ultimo}")
print(frutas)
```