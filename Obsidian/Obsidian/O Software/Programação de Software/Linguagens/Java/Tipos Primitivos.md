---
data_criacao: 14-08-2025
flashcards: Não feito
revisão: Não feita
---
# Tipos Primitivos
Muita atenção ao utilizar os modificadores de tipos, os tipos primitivos, quando têm uma forma padrão (como double para decimal | int para inteiro) é necessário colocar o indicador de tipo após o valor (27.4f (float) | 100000L (long int)).

## Char
Tipo primitivo designado a caracteres.
- `Tamanho`: 16 bits.
- `Descrição`: ASCII de 0 à 255.
```Java
char nota = 'A';
char simbolo = '%';
```

## Inteiros
Modificáveis com modificadores de tipo:
- `byte`: 8 bits <small>[-128 ; 127]</small>
- `short`: 16 bits <small>[-32K ; 32K]</small>
- `int`: 32 bits <small>(numeros grandes)</small>
- `long`: 64 bits <small>(para numeros muito grandes)</small>

```Java
byte nota = 10;
short distancia = 20143;
long numero = 10000000L;
```
## Decimais
Modificável com modificadores do tipo:
- `float`: 32 bits <small>(para decimais grandes)</small>
- `double`: 64 bits <small>(para decimais muito grandes)</small>

```Java
float aliquota = 27.4f;
double preco = 99.53;
```

## Booleano
```Java
vivo = true;
```