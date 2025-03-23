A tag `<a>` (âncora) cria links em uma página HTML. Ela pode ser usada para redirecionar para outras páginas, seções internas ou até para baixar arquivos.

>"a"  é de anchor, que significa 
### *Exemplo básico:*

```html
<a href="https://www.example.com">Visite o Example</a>
```

🔹 Exibido como: **[Visite o Example](https://www.example.com/)**

---

### *Principais atributos:*

- `href` → Define o destino do link.
- `target="_blank"` → Abre o link em uma nova aba.
- `title` → Exibe um texto ao passar o mouse.

**Exemplo:**

```html
<a href="https://www.example.com" target="_blank" title="Abrir Example">Clique aqui</a>
```

---

### *Link para uma seção da mesma página:*

```html
<a href="#secao1">Ir para a Seção 1</a>

<h2 id="secao1">Seção 1</h2>
<p>Conteúdo da Seção 1...</p>
```

---

### *Link para baixar um arquivo:*

```html
<a href="documento.pdf" download>Baixar PDF</a>
```

Essa tag é essencial para navegação na web! 🚀