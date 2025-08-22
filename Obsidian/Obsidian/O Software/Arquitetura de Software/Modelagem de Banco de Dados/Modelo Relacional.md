# O Modelo Relacional

O Modelo Relacional foi introduzido por Edgar F. Codd em 1970.
Fundamentado em lógica e _teoria dos conjuntos_, ele representa os dados como **tabelas** com *linhas* (*registros*) e **colunas** (**campos**).

- **Na prática (SQL):**  
    **tabela** = conjunto de *linhas* (*registros*) estruturadas por **colunas** (**campos**) e seus tipos.

- **Nomenclatura Edgar (não usada na prática):**  
    `relação` → tabela ·
    `tupla` → linha ·
    `atributo` → coluna ·
    ``domínio`` → tipo de dado.    

## Termos básicos

### [[Coluna (campo)]]

### Linha (registro): 
conjunto de valores que preenche as colunas.

### Esquema:
definição da tabela (nomes de colunas, tipos e restrições).

### Grau (aridade)
nº de **colunas**. **Cardinalidade**: nº de **linhas**.    

## Chaves e integridade

- **Chave candidata**: conjunto **mínimo** de colunas que identifica unicamente uma **linha**.

- **Chave primária (PRIMARY KEY)**: a candidata escolhida como identificador principal (**única** e **não nula**).
    
- **Chave estrangeira (FOREIGN KEY)**: coluna(s) que referenciam a `PRIMARY KEY` de outra tabela → assegura _integridade referencial_ (regras: `RESTRICT/NO ACTION`, `CASCADE`, `SET NULL`, `SET DEFAULT`).
    

## Observações importantes

- **Ordem**: tabelas **não têm ordem** por definição; só existe ordem com `ORDER BY`.
    
- **Duplicatas**: na teoria, **não** há; em SQL **podem existir** se você não usar `PRIMARY KEY`/`UNIQUE`.
    
- **`NULL`**: está no SQL (lógica de três valores). Use `IS NULL`/`IS NOT NULL` nas comparações.
    

---

- **Tabela**: coleção (na teoria, `relação`) de **linhas** coerentes com um **esquema**.
    
- **Composta de**:
    
    - **Linhas** (registros);
        
    - **Colunas** (campos) e seus **tipos**;
        
    - **Restrições** (`PRIMARY KEY`, `UNIQUE`, `CHECK`, `NOT NULL`).
        
- **Relacionamentos** entre tabelas via **chaves estrangeiras**, garantindo _integridade referencial_.
    

---

_Nota gramatical rápida:_ o correto é **“em vez de”** (substituição). **“Ao invés de”** só quando há oposição.