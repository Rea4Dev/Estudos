# Do mundo real ao Banco de Dados

Antes de criar um banco de dados, é preciso **entender o problema** e **observar o mundo real**. 

Essa fase envolve:
- ✅ *Identificar os principais elementos* – Ocorre a abstração; selecionar do todo apenas aquilo que me interessa armazenar a partir do contexto pretendido.
- ✅ *Analisar relacionamentos* – Como os elementos interagem? (ex: um **cliente** pode fazer vários **pedidos**).  
- ✅ *Coletar requisitos* – Quais são as necessidades dos usuários e da aplicação?

![[Pasted image 20250222174524.png | center]]

## Exemplo prático  

Imagine que você precisa criar um banco de dados para uma locadora de veículos. Alguns elementos que podem ser observados no mundo real:

- **Clientes** alugam **carros**.
- Cada **carro** pertence a uma **categoria** (econômico, SUV, luxo).
- Um **contrato de aluguel** é gerado para cada locação.

	📌 Essa observação do mundo real nos ajuda a extrair entidades e relações que serão modeladas no banco de dados.