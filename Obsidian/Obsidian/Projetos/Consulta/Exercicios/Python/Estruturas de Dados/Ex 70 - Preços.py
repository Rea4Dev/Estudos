produtos = ('Lápis', 2.75, 
            'Caneta', 10.3, 
            'Caderno', 20.99,    
            'Estojo', 25, 
            'Apontador', 5)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')   #forma 1
print('LISTAGEM DE PREÇOS'.center(40)) #forma 2
print('-' * 40)

for i in range(0, len(produtos)):
    if i % 2 == 0:
        print(f"{produtos[i]:.<30}", end="") #elementos par são os produtos
    else:
        print(f"R${produtos[i]:>7.2f}") #elementos ímpares os preços

print('-' * 40)