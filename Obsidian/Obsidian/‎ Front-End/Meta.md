Contém metadados do documento, como `charset` e `viewport`, que são importantes para a compatibilidade e responsividade.
```HTML
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
(...)
```
### Meta Charset

A tag `<meta charset="UTF-8">` define a **codificação de caracteres** que o navegador deve usar para renderizar o conteúdo da página. No Brasil usamos UTF-8.

- **Por que isso importa?**  
    Ela garante que todos os caracteres (como acentos, símbolos especiais e letras de diversos alfabetos) sejam exibidos corretamente.
- **Exemplo prático:**  
    Se você usar uma codificação inadequada, pode acabar vendo caracteres estranhos ou “mojibake” (texto corrompido).
- **Resumo:**  
    Ela atua como um “tradutor” que informa ao navegador como interpretar os bytes do arquivo HTML como texto legível.

### Meta Viewport

A tag `<meta name="viewport" content="width=device-width, initial-scale=1.0">` é essencial para a **responsividade** das páginas, principalmente em dispositivos móveis.

- **width=device-width:**  
    Faz com que a largura da página se ajuste à largura da tela do dispositivo. Isso evita que a página seja renderizada em uma escala inadequada ou com barras de rolagem desnecessárias.
- **initial-scale=1.0:**  
    Define o nível de zoom inicial quando a página é carregada, garantindo que o conteúdo apareça no tamanho adequado sem zoom automático.
- **Por que isso importa?**  
    Sem essa tag, a página pode parecer “esticada” ou muito pequena em telas de celulares, comprometendo a experiência do usuário.

Em resumo, essas meta tags fornecem **metadados** que ajudam os navegadores a entenderem como processar e exibir o conteúdo de maneira correta e adaptada a diferentes dispositivos.