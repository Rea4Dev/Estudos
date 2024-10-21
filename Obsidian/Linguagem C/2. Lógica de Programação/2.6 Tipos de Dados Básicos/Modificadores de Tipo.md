O fato de o tamanho de um inteiro poder variar é algo preocupante, pois os limites das variáveis que armazenam inteiros podem variar de maneira drástica, reduzindo fortemente a portabilidade dos programas entre máquinas diferentes. Repare bem na diferença entre os valores que uma variável pode conter:

![[Pasted image 20241020140256.png]]

Como podemos então garantir que um programa escrito por nós usa sempre dois ou quatro bytes para armazenar um inteiro, se o tamanho de um inteiro varia de máquina para máquina?

Na declaração de um inteiro podem ser utilizados quatro prefixos distintos para melhor definição das características da variável.

- **short** - Inteiro pequeno (2 bytes)
- **long** - Inteiro grande (4 bytes)
- **signed** - Inteiro com sinal (negativos e positivos)
- **unsigned** - Inteiro sem sinal (apenas positivos)

## Short e Long
Para garantirmos que o inteiro n usa **apenas 2 bytes de memória, independentemente da arquitetura** utilizada, devemos declarar a variável como:
```
short int n;
```

Para garantirmos que o inteiro n usa sempre 4 bytes de memória, independente da arquitetura utilizada, devemos declarar a variável como:
```
long int n;
```

> -"_O formato de leitura e escrita de variáveis inteiras short e long nas funções scanf e printf devem ser precedido dos prefixos h (short) e l (long)._"

```
scanf(“%hd”,&idade);

printf(“Tenho %ld na minha conta do banco.”)
```