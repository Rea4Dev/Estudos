O HTML semântico é uma *forma de estruturar* o código que utiliza *tags que descrevem claramente* o papel de cada parte do conteúdo. 

Isso **facilita a leitura e manutenção** do código, melhora a **acessibilidade** e ainda ajuda no **SEO** (otimização para mecanismos de busca).

## O que é HTML Semântico?

Em vez de usar apenas `<div>` ou `<span>` para tudo (que é possível), o HTML semântico emprega tags específicas que indicam o tipo de conteúdo que elas contêm. Assim, tanto navegadores quanto ferramentas de acessibilidade conseguem interpretar melhor a estrutura da página.

## Por que usar HTML Semântico?

- **Melhora a acessibilidade:** Leitores de tela para deficientes e outros dispositivos podem entender melhor a hierarquia e a função dos elementos.
- **Facilita a manutenção:** Um código organizado com tags semânticas é mais fácil de ler e modificar.
- **Auxilia no SEO:** Mecanismos de busca conseguem interpretar o conteúdo de maneira mais precisa, potencialmente melhorando o ranqueamento.

## Principais Tags Semânticas
Lembre, todas as tags abaixo são pertencentes ao body.

- `<header>`: Representa a seção de cabeçalho da página ou de uma seção.
- `<nav>`: Indica uma área de navegação, com links para outras partes do site.
- `<main>`: Delimita o conteúdo principal do documento.
- `<section>`: Agrupa conteúdo relacionado, geralmente com um tema em comum.
- `<article>`: Utilizada para conteúdos independentes e autônomos, como posts de blog ou notícias.
- `<aside>`: Representa conteúdo tangencial ao conteúdo principal, como barras laterais ou citações.
- `<footer>`: Define o rodapé da página ou seção, com informações complementares ou de autoria.

Não se preocupe, sabendo da existência e buscando ser semântico é o caminho certo para cada vez mais melhorar sua semântica. Não quero que isso seja um impeditivo para codificar.

## Exemplo de Código
Fique calmo, por hora você idealmente não conhece nenhuma das tags abaixo, mas a título de ilustração e visita futura, fica abaixo um exemplo:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Exemplo de HTML Semântico</title>
</head>
<body>
  <header>
    <h1>Bem-vindo ao Meu Site</h1>
  </header>

  <nav>
    <ul>
      <li><a href="#inicio">Início</a></li>
      <li><a href="#sobre">Sobre</a></li>
      <li><a href="#contato">Contato</a></li>
    </ul>
  </nav>

  <main>
    <article>
      <h2>Artigo Principal</h2>
      <p>Este é um exemplo de como utilizar HTML semântico para estruturar um artigo.</p>
    </article>

    <aside>
      <h3>Informações Adicionais</h3>
      <p>Aqui você pode colocar dados complementares ou links relacionados.</p>
    </aside>
  </main>

  <footer>
    <p>&copy; 2025 - Todos os direitos reservados.</p>
  </footer>
</body>
</html>
```

