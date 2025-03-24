
#! Crie um script que conte a quantidade de letras da frase, entretanto, contornando o fato de que digitaram com espaços inadequados.

frase = "   Codar em Casal com carinho.     "
print(len(frase.strip()))

#funcionaria fazer a linha abaixo
frase = len(frase.strip())
print(frase)