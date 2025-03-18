Uma página HTML possui uma estrutura de organização e separação das tags visando principalmente organização semântica das tags.

Em outras palavras, todo código de uma página HTML seguirá um padrão de estruturação, onde será separado:
**Cabeça**
	Incluindo informações da página.
**Corpo**
	Onde há o conteúdo principal e todas as tags que adicionaremos para gerar a página.
	Visaremos sempre o bom costume de seguir a padronização para escolher, separar e estruturar nossas tags (não se preocupe, será ensinado).

Preste bastante atenção nas explicações abaixo para entender os elementos da estrutura.

---
## Estrutura
Antes do conteúdo da cabeça, é declarado o elemento que informa qual será o tipo deste documento (página HTML). Desta forma:
```C
<!DOCTYPE html>
```

Logo após, já declaramos a tag html para indicar que tudo entre a abertura e o fechamento da tag será conteúdo desta tag html.
Na tag html, declaramos um atributo que diz qual será o idioma desta página HTML (útil especialmente para ferramentas de tradução de navegadores, pois se identificarem que é uma língua diferente do usuário, irão sugerir tradução):
```c
<!DOCTYPE html>
<html lang="pt-BR>

</html>
```

Agora, como conteúdo da tag HTML, iremos deixar os espaços de conteúdos da cabeça e corpo declarados.
```C
<!DOCTYPE html>
<html lang="pt-BR>
	<head>
	
	</head>
	
	<body>
	
	</body>
</html>
```

## Cabeça
Na cabeça, podemos incluir tags que incluirão informações da página.
Por exemplo, a tag title, que informa o título da página (que aparece na aba do navegador).
```C
<!DOCTYPE html>
<html lang="pt-BR>
	<head>
		<title> Raccoon News </title>
	</head>
	
	<body>
	
	</body>
</html>
```

## Corpo
Onde incluiremos o conteúdo da página em tags. Em outras palavras, a secção que mais iremos trabalhar.

A exemplo, podemos incluir um título de texto (h1) e um parágrafo (p). Não se preocupe pois iremos ver as tags melhor com o tempo, entenda por hora a estrutura.
```C
<!DOCTYPE html>
<html lang="pt-BR>
	<head>
		<title> Raccoon News </title>
	</head>
	
	<body>
		<h1> Título da Notícia </h1>
		<p> Parágrafo da Notícia </p>
	</body>
</html>
```