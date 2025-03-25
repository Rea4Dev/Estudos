A propriedade *`font-family`* define a família de fontes utilizada no texto.

É uma boa prática utilizar um _fallback_, ou seja, declarar múltiplas famílias de fontes como alternativas. Caso o navegador do usuário não consiga carregar a primeira opção, ele usará a próxima disponível na lista.

Além disso, a última opção deve ser uma categoria genérica (_serif_, _sans-serif_, _monospace_, etc.), garantindo que o navegador sempre encontre uma fonte compatível.

### **Exemplo:**

```css
p {
  font-family: "Roboto", "Arial", sans-serif;
}
```

Neste caso:

1. O navegador tentará usar a fonte **Roboto**.
2. Se ela não estiver disponível, tentará **Arial**.
3. Se nenhuma das duas existir, usará qualquer fonte genérica **sans-serif** do sistema.

💡 **Dica:** Para garantir que a fonte personalizada seja carregada corretamente, é comum importá-la via Google Fonts ou usar a regra `@font-face`.

### **Importando fontes do Google Fonts:**

```css
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

p {
  font-family: "Roboto", Arial, sans-serif;
}
```

Isso garante que a fonte **Roboto** será baixada automaticamente, caso não esteja instalada no dispositivo do usuário. 🚀