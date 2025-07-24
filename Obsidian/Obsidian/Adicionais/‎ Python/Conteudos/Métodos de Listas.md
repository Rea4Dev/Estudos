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

---

```Python
lista=['calailo', 'burgir', 'chulo', 'locket']

#print(familia[3]) - retorna um indice
#print(familia[-3]) - retorna um indice d tras para frente
#print(familia[2:]) - retorna a partir do indice 2
#print(familia[2:4]) - retorna a partir do índice 2 ate o 4, excluindo o 4

lista[3]='Raco' #modifica o elemento escolhido   
lista.extend(['Shine','Lobisteu']) #add uma lista na outra
lista.append('Megalodon') #add um valor 
lista.insert(2,'Megalodon') #substitui o indice colocado, mas nao o elemento
lista.pop() #remove o ultimo indice
lista.remove('chulo') #remove o elemento específico
lista.clear() #apaga todos os indices, ficando uma lista vazia
lista2 = lista.copy() #copia a lista

idade_lista=[8,4,5,8]
idade_lista.sort() #ordem crescente

#lista.sort() - ordem alfabética do A ao Z
#idade_lista.reverse() - ordem decrescente
#lista.reverse() - ordem alfabetica do Z ao A
```