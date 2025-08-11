---
data_criacao: 05-08-2025
flashcards: Não feito
revisão: Não feita
---
# 💬 Caso do Nome em “Negrito” no LinkedIn — Análise Técnica

- Certa vez, utilizei o site [Piliapp Cool Text](https://pt.piliapp.com/cool-text/bold-italic) para converter meu nome para **“negrito”**.
- No LinkedIn, alterei o campo “Nome” para essa versão negrito e funcionou: meu nome aparecia em negrito para todos.  
- Após cerca de uma semana, fui permanentemente banido. 

Ao tentar criar outra conta com o mesmo truque, o sistema já havia sido atualizado para impedir.

## 1️⃣ O que realmente aconteceu
O site **não** aplicou formatação no texto (como HTML, Markdown ou CSS).  
Ele converteu cada letra para **outro caractere Unicode visualmente equivalente** — o chamado **homoglyph** (*caractere homógrafo*) — técnica muitas vezes explorada em ataques conhecidos como *homoglyph attack*.

Exemplo:
- Letra `R` normal → `U+0052`
- Letra `R` em *Mathematical Bold* → `U+1D413` (𝗥)

O resultado parece “negrito” porque o navegador **renderiza** o caractere usando um glifo estilizado presente na fonte, mas na realidade são apenas outros pontos de código Unicode (que podem ser desejáveis ou não no contexto).

---

## 2️⃣ UTF-8

- A maioria dos sistemas modernos de internet — incluindo LinkedIn — usa **UTF‑8** como codificação padrão para textos, porque é compatível com todos os idiomas e permite qualquer ponto de código Unicode (inclusive blocos estendidos como _Mathematical Alphanumeric Symbols_)

- Caracteres “negrito” de blocos como **Mathematical Alphanumeric Symbols** estão acima de `U+FFFF`, ocupando **4 bytes**.

- Se o sistema suporta `utf8mb4` (MySQL) ou UTF-8 completo, qualquer caractere Unicode pode ser armazenado.

Exemplo em bytes:
- `𝗥` (U+1D413) → `F0 9D 90 93` em UTF-8.

---
## 3️⃣ Aceitação

Na época, o campo “Nome” provavelmente tinha apenas:
- Validação de **não vazio** e caracteres imprimíveis;
- Sem filtro por **intervalo Unicode permitido**.
Resultado: qualquer letra visual passava, mesmo fora do alfabeto básico.

1. Mesmo campos como o **Nome ou título do perfil** aceitam texto UTF‑8 completo inicialmente. Mas isso não significa que aceitam qualquer ponto de código Unicode: há filtros de validação interna, especialmente em manchetes e nomes

2. Em agosto de 2024, o LinkedIn passou a **bloquear Unicode estilizado** (`fancy text`) em manchetes. O motivo: esses caracteres **não são indexáveis**, **podem quebrar acessibilidade** e **não são consistentes entre dispositivos**
---
## 4️⃣ A validação

1. **Armazenamento (backend)**: colunas suportam `utf8mb4` (MySQL) ou codificações equivalentes que lidam com qualquer ponto Unicode, até 4 bytes por caractere. Se um caractere estiver fora disso, causa erro técnico [Wikipedia](https://en.wikipedia.org/wiki/UTF-8?utm_source=chatgpt.com).

2. **Validação de entrada**:
	- Aplicam **normalização Unicode** (NFKC/NFKD) para transformar variantes estilizadas em caracteres básicos.
	- Usam **regex restritiva** para permitir apenas letras latinas, acentos comuns, espaço e traço.    
	- Isso impede que versões “negrito”, “itálico” ou “script” passem pelo sistema.

3. **Renderização (frontend)**:
	- Se um caractere passa na validação, o frontend o exibe com a fonte padrão. Se for algum ponto estilizado suportado na fonte do dispositivo, parecerá bold, italic etc. Caso contrário, aparece como “�” ou caracteres quadriculados.

4. **Por que bloquearam depois**
	Após detectar abuso, o LinkedIn pode ter adotado:
	
	*a) Normalização Unicode*
	- Aplicar `NFKC` ou `NFKD` antes de salvar/verificar:
	  - 𝗥 → R  
	  - Ｒ → R  
	- Isso reduz variações visuais ao caractere “base”.
	
	*b) Whitelist de caracteres*
	- Aceitar apenas letras `A-Z`, `a-z`, acentos comuns e poucos símbolos.
	
	*c) Regex restritiva*
	- Ex.: `^[\p{L}\p{M}\s\-]+$` com bloqueio de blocos incomuns.

---

## 5️⃣ Riscos e impactos
Apesar de não “quebrar” o banco de dados em grandes redes (desde que preparado para Unicode completo), o uso desses caracteres traz problemas:

- **Busca e indexação**: nomes em Unicode “exótico” não aparecem em buscas padrão.
- **Ordenação**: caracteres fora do alfabeto básico quebram ordenações alfabéticas.
- **Segurança**: homoglyph attacks são usados em phishing (`раураl.com` usando cirílico).
- **Normalização inconsistente**: sistemas diferentes podem tratar 𝗥 e R como letras distintas.

---

## 6️⃣ Relação com bancos de dados
- Em **bancos relacionais** (MySQL, PostgreSQL) e **não relacionais** (MongoDB), o risco só existe se o **charset** for limitado (ex.: `latin1` ou `utf8` antigo).
- Plataformas grandes usam **utf8mb4** ou equivalente, então armazenar 𝗥 é só guardar bytes.
- O problema não é técnico de “queda”, mas **funcional e de política interna**.

---

> **Nota:** Esse caso é um exemplo prático de como detalhes de codificação de caracteres, Unicode e políticas de entrada podem afetar sistemas reais — e por que validações robustas são essenciais.
