A propriedade *`text-align`* define o **alinhamento horizontal** do texto dentro de um elemento.

### **Valores mais comuns:**

- `left` → Alinha o texto à esquerda (padrão para idiomas LTR, como o português).
- `right` → Alinha o texto à direita (útil para idiomas RTL, como árabe).
- `center` → Centraliza o texto.
- `justify` → Distribui o texto uniformemente para ocupar toda a largura do elemento.

### **Exemplo prático:**

```css
p {
  text-align: left;   /* Alinhado à esquerda */
}

h1 {
  text-align: center; /* Centralizado */
}

div {
  text-align: justify; /* Justificado */
}
```

💡 **Dicas:**

- O `justify` pode melhorar a leitura em blocos de texto longos, mas pode criar espaçamentos irregulares entre palavras.
- O alinhamento afeta **apenas elementos inline ou inline-block** dentro do elemento selecionado.

🔹 **Exemplo visual:**

```html
<div style="width: 300px; text-align: justify;">
  Este é um exemplo de texto justificado. O navegador ajusta os espaços entre as palavras para ocupar toda a largura do elemento.
</div>
```

🚀 **Use text-align junto com direction: rtl; para alinhar textos em idiomas da direita para a esquerda!**