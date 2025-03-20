tupla = (input("Digite uma palavra: "),
         input("Digite outra palavra: "),
         input("Digite outra palavra: "),
         input("Digite outra palavra: "),)

for i in range(0, len(tupla)):
    print(f"\nNa palavra {tupla[i]} temos as vogais -> ", end="")
    for c in range(0, len(tupla[i])):        
        if tupla[i][c].lower() in "aeiou":
            print(tupla[i][c].lower(), end="")