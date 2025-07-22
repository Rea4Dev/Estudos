- Atributo ou grupo de atributos com o potencial para se tornarem uma chave primária.
- Uma chave candidata que *não for usada como primária* chamará-se ``Chave Alternativa``.

# Tabela: ITS_Test
| TEST_ID | *MMC_CODE* | *OP_NUMBER* | DESCRIPTION      |
| ------- | ---------- | ----------- | ---------------- |
| 1       | MMC123     | 101         | Teste de leitura |
| 2       | MMC456     | 102         | Teste de escrita |

Embora TEST_ID seja a chave primária, os atributos **MMC_CODE** e **OP_NUMBER** poderia ser considerada uma chave candidata, pois cada identifica de forma única um teste.

Como não são usados como chave primária no caso, então recebem o nome ``Chave Alternativa``