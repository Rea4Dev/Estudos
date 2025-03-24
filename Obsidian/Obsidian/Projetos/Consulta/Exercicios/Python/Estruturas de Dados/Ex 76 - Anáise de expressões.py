# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expressao = input('Digite a expressão: ')
abre = 0
fecha = 0
for i in expressao:
    if i == "(":
        abre += 1
    elif i == ")":
        fecha += 1
if abre==fecha:
    print("Certo")
else:
    print("Errado")

#---------------------------------------------------------------------------------------------------------------------------------------------#
#Soluão professor
expr = input("Digite a expressão: ")
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')