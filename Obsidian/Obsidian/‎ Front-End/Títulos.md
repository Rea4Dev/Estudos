A tag `<h1>` define o título principal de uma página ou seção. É a mais importante entre os seis níveis de cabeçalhos (`<h1>` a `<h6>`) e geralmente indica o tema principal do conteúdo.
```HTML
<h1>Título principal</h1>
```

> "h1" significa "Header 1", que é "Título 1".
## *Hierarquia de Títulos*

Como pode perceber, há uma hierarquia nos títulos, semântica, lógica e visual.
A hierarquia de títulos em HTML vai de `<h1>` a `<h6>`, onde `<h1>` é o mais importante e `<h6>` o menos. Ela ajuda na organização do conteúdo, acessibilidade e SEO (otimização para mecanismos de busca).

##### *Ordem correta de uso:*

1. `<h1>` – Título principal da página (deve haver apenas um por página).
2. `<h2>` – Subtítulos diretos do `<h1>`.
3. `<h3>` – Subtítulos dentro de um `<h2>`, e assim por diante até `<h6>`.

##### *Exemplo de estrutura correta:*

```html
<h1>Guia de HTML</h1>
  <h2>Introdução</h2>
    <h3>O que é HTML?</h3>
    <p>Texto...</p>
    
    <h3>História do HTML</h3>
	<p>Texto...</p>
	
  <h2>Elementos Básicos</h2>
    <h3>Tags Estruturais</h3>
	<p>Texto...</p>
	
    <h3>Tags de Formatação</h3>
	<p>Texto...</p>
```

![[Pasted image 20250317175504.png | center | 400]]

##### *Boas práticas:*

✅ Use títulos em ordem lógica (não pule do `<h1>` para `<h4>`).  
✅ Apenas um `<h1>` por página.  
✅ Mantenha os títulos curtos e descritivos.

Isso melhora a experiência do usuário e a indexação nos motores de busca. 🚀