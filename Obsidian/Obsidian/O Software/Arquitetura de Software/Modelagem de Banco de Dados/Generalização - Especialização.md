- *Generalização/Especialização* – Representa uma hierarquia entre entidades.
	- **Generalização** ocorre quando entidades diferentes compartilham características em comum, então elas são agrupadas em uma entidade mais genérica.
	- **Especialização** é o oposto: uma entidade genérica pode ser dividida em subtipos mais específicos, que possuem atributos ou comportamentos próprios.
![[Pasted image 20250222170955.png | center ]]

No modelo de [[Engenharia de Informaçao]] representamos:
![[Pasted image 20250223172831.png]]

🔻 **Equivalências nos Modelos:**
- **Modelo Conceitual** → Representada como um triângulo indicando hierarquia, com a entidade geral no topo e as especializações abaixo.
- **Modelo Lógico** → Representada como uma _Tabela Pai_ para a entidade geral e _Tabelas Filhas_ para as especializações, conectadas por chaves estrangeiras.
- **Modelo Físico** → Implementada como tabelas relacionadas usando FK ou, em SGBDs que suportam herança (ex: PostgreSQL), diretamente como herança.