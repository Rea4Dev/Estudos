São as características das entidades (ex: `nome`, `CPF`, `modelo`, `placa`). Representado por círculos.
![[Pasted image 20250223202854.png | center]]

🔻 **Equivalências nos Modelos:**
- **Modelo Conceitual** → Representado como um _Atributo_ (bolinha conectada à entidade no DER).
- **Modelo Lógico** → Representado como uma _Coluna (ou Campo)_ dentro da tabela.
- **Modelo Físico** → Implementado como um _Campo_ em uma tabela do banco de dados, com tipo de dado definido.

## Atributos Especiais - Chaves
Chaves são atributos especiais usados para **identificar** registros **de forma única** (ex: CPF como chave primária em uma tabela de pessoas).

>💡Ou seja, toda chave é um atributo, mas nem todo atributo é uma chave.

Pode ser única (identifica uma única linha) ou não-única (identifica um conjunto de linhas).