---
data_criacao: 22-08-2025
flashcards: Não feito
revisão: Não feita
---
Possui um _tipo_ e pode ter **restrições**:
# Tipos
- ``INT``: números inteiros. Ex.: -2, 0, 42.
- ``DECIMAL(p,s) / NUMERIC(p,s)``: números _exatos_ com precisão fixa. Ex.: 10.50.
- ``FLOAT / REAL / DOUBLE``: números de ponto flutuante (_aproximados_).
- ``VARCHAR(n)``: texto de tamanho _variável_ até n. Ex.: "Ana".
- ``TEXT``: texto sem limite prático (_depende do SGBD_).
- ``CHAR(n)``: texto de tamanho _fixo_; completa com espaços.
- ``DATE``: data. Ex.: 2025-08-22.
- ``TIMESTAMP``: data e hora; alguns SGBDs têm opção _with time zone_.
- ``BOOLEAN``: verdadeiro/falso (às vezes 1/0).
- ``BLOB / BYTEA``: dados _binários_ (imagens, PDFs).
- ``UUID``: identificador único universal.
- ``JSON / JSONB``: documentos JSON (_validação/indexação variam por SGBD_).

# Restrições
- ``NULL``: ausência de valor; use como _IS NULL_ / _IS NOT NULL_ (não use = NULL).
- ``NOT NULL``: impede _NULL_; exige preenchimento. Ex.: nome VARCHAR(80) NOT NULL.
- ``UNIQUE``: todos os valores da coluna devem ser distintos _(em geral, múltiplos NULL são permitidos)_.
- ``CHECK``: condição booleana por linha. Ex.: idade INT CHECK (idade >= 0).

**Exemplo para visualizar:**
![[Pasted image 20250822141750.png | center]]