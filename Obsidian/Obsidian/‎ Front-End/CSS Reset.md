Alguns navegadores adotam *valores de estilização padrão* sem termos definido previamente. Estes valores variam de navegador para navegador, o que pode causar diferenças, comportamentos inesperados e problemas em nossos layouts.

Por conta disso é comum adotarmos a prática de `CSS Reset`, que nada mais é que inicialmente *colocar valores nulos em propriedades que costumam ser afetadas* por este comportamento.

```CSS
* {
  margin: 0;
  padding: 0;
  border: 0;
}

body {
	line-height: 1.6; /* Espaço entre as linhas */
}
```

## *Diferentes Formas*

Há inúmeras possibilidades e costumes de CSS reset. Inicialmente, fique com o que foi apresentado.