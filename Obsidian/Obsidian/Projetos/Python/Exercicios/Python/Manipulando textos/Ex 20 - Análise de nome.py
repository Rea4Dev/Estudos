""" 
- O nome com todas as letras maiúsculas.
- O nome com todas as letras minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
"""

nomeOriginal = "    Rea      Dev        "
print(f"\nNome original com espaços: {nomeOriginal}")


SplitJoin = (" ".join(nomeOriginal.split()))
print(f"\nOriginal transformado em lista e depois juntado com 1 espaço: {SplitJoin}")


print(f"Transforma em maiúscula: {SplitJoin.upper()}")


print(f"Transforma em minúscula: {SplitJoin.lower()}")


fullJoined = ("".join(nomeOriginal.split()))


print(f"\nTudo junto: {fullJoined}")
print(f"Tamanho: {len(fullJoined)}")
# outra forma de fazer a conta das letras sem espaços é: 
# print(len(nomeOriginal) - nomeOriginal.count(" "))


print(f"\nPrimeiro nome: {nomeOriginal.split()[0]}")
print(f"Tamanho: {len(nomeOriginal.split()[0])}")
# outra forma de fazer a conta da quantidade de letras do primeiro nome é
# print(f"Tamanho: {nomeOriginal.strip().find(" ")}")