A propriedade *`font-style`* define o **estilo da fonte**, ou seja, se o texto será normal, itálico ou oblíquo.

### **Valores possíveis:**

- `normal` → Texto sem alterações (padrão).
- `italic` → Texto em **itálico** (se a fonte suportar).
- `oblique` → Texto **inclinado** (similar ao itálico, mas gerado artificialmente).

### **Exemplo prático:**

```css
p {
  font-style: normal; /* Padrão */
}

em {
  font-style: italic; /* Itálico */
}

.special {
  font-style: oblique; /* Inclinada */
}
```

💡 **Diferença entre italic e oblique**

- `italic` usa uma versão real da fonte desenhada para ser itálica.
- `oblique` apenas inclina o texto artificialmente, útil quando a versão itálica não está disponível.

🔹 **Exemplo visual:**

```html
<p style="font-style: italic;">Este texto está em itálico.</p>
<p style="font-style: oblique;">Este texto está em oblíquo.</p>
```

🚀 **Dica:** Use `font-style: italic;` em elementos `<em>` e `<i>` para garantir acessibilidade e semântica correta!