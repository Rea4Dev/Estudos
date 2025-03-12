## Dimensões
Comecemos pela primeira máxima interessante:

> Não existe qualquer limite para o número de dimensões que um vetor pode conter.

A declaração de um vetor com n *dimensões* é realizada através da seguinte sintaxe:
```C
tipo vetor[dim1][dim2][…][dimn]
```

### Bidimensional
Vulgarmente chamado de Matriz (o que ele na verdade não é), o vetor bidimensional pode ser visualizado como um "jogo da velha".

| X   |     | O   |
| --- | --- | --- |
|     | X   |     |
|     |     | O   |
>Em C, um vetor declarado com duas dimensões não é, na realidade, uma Matriz, mas sim um vetor de vetores. O mesmo se aplica a vetores com dimensão superior a 2.

No caso anterior aquilo que declaramos não foi uma matriz, mas sim um vetor de três posições Velha\[3], em que cada uma dessas posições é formada por um vetor de três caracteres.
![[Pasted image 20250210134020.png | center | 180]]
![[Pasted image 20250210134152.png]]

Se declararmos um vetor:
```C
int v[3][4];
```
![[Pasted image 20250210134246.png | center]]
