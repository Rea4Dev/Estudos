Existem três formas de utilizar/linkar o css:

`Inline`
	Dentro de um elemento HTML através do atributo "style".

`Incorporado`
	Delimitado pela tag < style >.

`Externo`
	Arquivo CSS externo citado dentro do HTML 

![[Pasted image 20250324203415.png]]

Desta forma, CSS externo é o mais escalável (quanto mais escalável, melhor). Particularmente, utilizo apenas o CSS externo por boa prática.

---

## *Inline*

O CSS inline é aplicado diretamente dentro de uma tag HTML utilizando o atributo `style`
É útil para alterações rápidas ou estilos específicos, mas não é recomendado para grandes projetos, pois dificulta a manutenção.

```HTML
<p style="color: red; font-size: 20px;">Este texto está em vermelho e com tamanho 20px</p>
```
<p style="color: red; font-size: 20px;">Este texto está em vermelho e com tamanho 20px</p>

---

## *Incorporado*

O CSS incorporado é escrito dentro da própria página HTML, dentro da tag `<style>` no `<head>`.  
É indicado para estilos aplicados apenas a uma página específica, mas ainda assim não é a melhor prática para projetos maiores.

```HTML
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Exemplo CSS Incorporado</title>
  <style>
    p {
      color: blue;
      font-size: 18px;
    }
  </style>
</head>
<body>
  <p>Este texto está em azul e com tamanho 18px</p>
</body>
</html>
```

<p style="color: blue; font-size: 18px;">Este texto está em azul e com tamanho 18px</p>

---

## *Externo*

O CSS externo é feito em um arquivo `.css` separado e é referenciado no HTML com a tag `<link>`.  
É a forma mais organizada e recomendada, principalmente para projetos grandes ou reutilizáveis.

```HTML
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Exemplo CSS Externo</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <p>Este texto está em verde e com tamanho 16px</p>
</body>
</html>
```

```CSS
p {
  color: green;
  font-size: 16px;
}
```

<p style="color: green; font-size: 16px;">Este texto está em verde e com tamanho 16px</p>
