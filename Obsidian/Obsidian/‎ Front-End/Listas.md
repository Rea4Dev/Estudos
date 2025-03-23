Em HTML, existem dois tipos principais de listas:

> "ul" é undernated list (lista desordenada), e "ol" é ordenated list (lista ordenada)
### 1️⃣ *Listas não ordenadas*

Usadas para itens sem uma sequência específica. Os itens são marcados com pontos (`•`).

**Exemplo:**

```html
<ul>
    <li>Maçã</li>
    <li>Banana</li>
    <li>Uva</li>
</ul>
```

🔹 Exibido como:

- Maçã
- Banana
- Uva

---

### 2️⃣ *Listas ordenadas*

Usadas para itens que seguem uma ordem lógica. Os itens são numerados.

**Exemplo:**

```html
<ol>
    <li>Pré-aquecer o forno</li>
    <li>Misturar os ingredientes</li>
    <li>Assar por 30 minutos</li>
</ol>
```

🔹 Exibido como:

1. Pré-aquecer o forno
2. Misturar os ingredientes
3. Assar por 30 minutos

---

### *Extras*

✅ **Listas podem ser aninhadas:**

```html
<ul>
    <li>Frutas
        <ul>
            <li>Maçã</li>
            <li>Banana</li>
        </ul>
    </li>
</ul>
```

🔹 Exibido como:  

- Frutas
	- Maça
	- Banana


✅ Atributo `type` pode mudar o estilo da numeração em `<ol>`:

```html
<ol type="A">
    <li>Item 1</li>
    <li>Item 2</li>
</ol>
```

🔹 Exibido como:  

A. Item 1  
B. Item 2