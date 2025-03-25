A propriedade *`font-weight`* define a **espessura da fonte**.

### **Valores possíveis:**

1. **Palavras-chave:**
    
    - `normal` (padrão, equivalente a 400)
    - `bold` (negrito, equivalente a 700)
    - `lighter` (mais fino que o peso herdado)
    - `bolder` (mais grosso que o peso herdado)
    
    ```css
    p {
      font-weight: bold;
    }
    ```
    
2. **Valores numéricos:**
    
    - Varia de `100` (extremamente fino) a `900` (super grosso)
    - Nem todas as fontes suportam todos os valores
    
    ```css
    h1 {
      font-weight: 900; /* Extra black */
    }
    p {
      font-weight: 300; /* Light */
    }
    ```
    

💡 **Dicas:**

- Nem todas as fontes têm variações de peso entre `100` e `900`. Algumas só suportam `normal` e `bold`.
- Usar pesos intermediários (`300`, `500`, `700`) pode melhorar a **legibilidade** e o **design**.
- `bolder` e `lighter` funcionam de forma relativa ao peso herdado pelo elemento.

🔹 **Exemplo prático:**

```css
body {
  font-family: "Arial", sans-serif;
}

h1 {
  font-weight: 800; /* Bem grosso */
}

p {
  font-weight: 400; /* Normal */
}

span {
  font-weight: 200; /* Mais fino */
}
```

🚀 **Para melhor controle, prefira valores numéricos em vez de palavras-chave.**