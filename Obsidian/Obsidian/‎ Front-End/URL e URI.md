# URL

*Uniform Resource Locator* (URL) é o endereço que usamos para acessar recursos na internet.  
**Exemplo:** `https://www.google.com`  

# URI

A **URI (Uniform Resource Identifier)** é um identificador único para qualquer recurso na web, seja uma página, imagem, vídeo ou outro arquivo.  
Serve como uma forma padronizada de referenciar recursos.

> ![[Pasted image 20250317182855.png | 300]]  
> ![[Pasted image 20250317182808.png]]

## *Esquema (Protocolo de Comunicação)*

O esquema define como o navegador e o servidor se comunicam. Geralmente, temos dois:
- **HTTP:** Protocolo básico de transferência de dados.
- **HTTPS:** Versão segura do HTTP, que utiliza certificados e exibe o ícone de cadeado.

> ![[Pasted image 20250317183552.png | center]]

## *Domínio*

O domínio contém o endereço IP e a porta do servidor (geralmente 80 para http e 443 para https).  
*Exemplo:* No caso de um "live server", pode ser o seu próprio IP.

## *Caminho (Path)*

O **caminho** indica a localização do recurso na estrutura de pastas do servidor.  
*Exemplo:* Se você acessar `https://meusite.com/pasta/index.html`, o `/pasta/index.html` é o caminho.

---

# Como Funciona na Internet

1. **Digite a URL:** Ao digitar "google.com" no navegador, a solicitação é enviada ao seu provedor de internet.
2. **Consulta ao DNS:** O provedor consulta o **DNS** (um sistema que funciona como uma "planilha") para traduzir a URL em uma URI numérica.
3. **Solicitação ao Servidor:** Com a URI em mãos, o provedor direciona a requisição ao servidor web.
4. **Resposta do Servidor:** Se nenhum caminho específico for indicado, o servidor retorna a página padrão, geralmente o `index.html`. Acesse [[Parsing e Renderização]] para entender como é para o navegador quando recebe a página.

> ![[Pasted image 20250317192901.png | center]]

