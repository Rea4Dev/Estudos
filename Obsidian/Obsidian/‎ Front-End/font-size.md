A propriedade *`font-size`* define o tamanho da fonte do texto.

Existem várias unidades para especificar o tamanho da fonte, cada uma com características diferentes.

### **Principais unidades de medida:**

1. **Pixels (px)** – Tamanho fixo, independente do elemento pai.
    
    ```css
    p {
      font-size: 16px;
    }
    ```
    
    🔹 Útil para elementos com tamanho controlado, mas pode dificultar a acessibilidade.
    
2. **Ems (em)** – Relativo ao tamanho da fonte do elemento pai.
    
    ```css
    p {
      font-size: 1.2em; /* 1.2x o tamanho da fonte do elemento pai */
    }
    ```
    
    🔹 Útil para layouts responsivos, mas pode acumular tamanhos inesperados em elementos aninhados.
    
3. **Rems (rem)** – Relativo ao tamanho da fonte do `html`.
    
    ```css
    p {
      font-size: 1.2rem; /* 1.2x o tamanho da fonte do <html> */
    }
    ```
    
    🔹 Melhor para acessibilidade e responsividade, pois evita efeitos de escalonamento em cascata.
    
4. **Porcentagem (%)** – Relativo ao tamanho da fonte do elemento pai.
    
    ```css
    p {
      font-size: 120%;
    }
    ```
    
    🔹 Funciona de forma similar ao `em`, mas pode ser menos intuitivo em alguns casos.
    

💡 **Dica:**

- Para **sites responsivos**, prefira `rem` ou `em` em vez de `px`, pois facilitam a escalabilidade do texto em diferentes dispositivos.
- Para **textos acessíveis**, defina o tamanho base no `html` e use `rem` para manter uma escala consistente.

### **Exemplo prático de responsividade:**

```css
html {
  font-size: 16px;
}

h1 {
  font-size: 2rem; /* 32px */
}

p {
  font-size: 1rem; /* 16px */
}
```

🔹 Se o usuário aumentar o tamanho da fonte no navegador, os textos crescerão proporcionalmente. 🚀