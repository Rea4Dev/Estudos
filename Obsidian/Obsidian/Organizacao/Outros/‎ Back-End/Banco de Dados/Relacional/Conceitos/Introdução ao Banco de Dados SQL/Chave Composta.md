- *Chave Composta*: Dois ou mais atributos combinados identificam a entidade. 
# Tabela: ITS_Operations_Action
| *OPERATION_ID* | *ACTION_SEQUENCE* | ACTION_TYPE | RESULT  |
| -------------- | ----------------- | ----------- | ------- |
| 1001           | 1                 | Leitura     | SUCCESS |
| 1001           | 2                 | Verificação | FAIL    |
| 1002           | 1                 | Leitura     | SUCCESS |

*Observação:*  
A combinação de **OPERATION_ID** e **ACTION_SEQUENCE** forma uma chave composta, garantindo que cada ação dentro de uma operação seja única.
