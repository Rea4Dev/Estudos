Em CSS, chamamos esta caixa de **"box"**, que representa o espaço ocupado por um elemento (se tiver dificuldades para compreender experimente ver um vídeo explicando Box Model ou testar paralelamente no Codepen abaixo).
https://codepen.io/pen/

![[Box Model.png]]

Cada elemento HTML é uma **caixa retangular** composta por quatro camadas principais:

1. **Margin** – Espaço externo ao redor do elemento.
2. **Border** – A borda ao redor do conteúdo e do padding.
3. **Padding** – Espaço interno entre a borda e o conteúdo.
4. **Content** – O próprio conteúdo do elemento (texto, imagem, etc.).

---

## **1. Margin**

A **margin** define o espaçamento externo entre elementos.

```css
p {
  margin-top: 20px;
  margin-right: 30px;
  margin-bottom: 5px;
  margin-left: 10px;
}
```

Ou de forma simplificada, usando os quatro valores na ordem **top, right, bottom, left**:

```css
p {
  margin: 20px 30px 5px 10px;
}
```

💡 **Dica:** Se os valores forem iguais para os lados opostos, é possível encurtar ainda mais:

```css
p {
  margin: 20px 30px; /* 20px para top e bottom, 30px para left e right */
}
```
---

## **2. Border**

A **border** define a borda do elemento, podendo ter **espessura**, **cor** e **estilo**.

```css
p {
  border-top: 1px solid green;
  border-right: 2px ridge red;
  border-bottom: 4px double yellow;
  border-left: 6px inset blue;
}
```

📝 **Estilos de borda comuns:**

- `solid` → linha contínua
- `dashed` → tracejada
- `dotted` → pontilhada
- `double` → dupla
- `ridge` → efeito 3D elevado
- `inset` → efeito de "afundado"

![[Pasted image 20250323104055.png | center]]

---

## **3. Padding**

O **padding** é o espaçamento interno entre o conteúdo e a borda do elemento.

```css
p {
  padding-top: 10px;
  padding-right: 15px;
  padding-bottom: 5px;
  padding-left: 20px;
}
```

Ou de forma abreviada:

```css
p {
  padding: 10px 15px 5px 20px;
}
```

💡 **Dica:** Se todos os lados tiverem o mesmo valor, basta um número:

```css
p {
  padding: 10px;
}
```

🔎 **Importante:** O `padding` afeta **o tamanho total do elemento**. Para evitar que ele aumente o tamanho definido, podemos usar `box-sizing: border-box;`, conforme veremos adiante.

---

## **4. Width & Height**

As propriedades **width** e **height** controlam a largura e altura do conteúdo da caixa. Ou seja, alteramos diretamente a largura e altura da caixa do conteúdo.

```css
div {
  width: 200px;
  height: 150px;
}
```

Valores podem ser definidos em:

- **Pixels (px)** → Tamanho fixo (ex: `width: 300px;`).
- **Porcentagem (%)** → Relativo ao elemento pai (ex: `width: 50%;`).
- **auto** → O navegador ajusta automaticamente.
- **vw e vh** → Relativo à largura e altura da viewport (ex: `width: 50vw;`).
