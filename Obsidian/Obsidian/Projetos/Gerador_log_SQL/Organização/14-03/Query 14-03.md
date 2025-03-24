```SQL
SELECT 
    its_test.mmc,
    its_test.serial_number AS aeronave,
    its_test.op,
    its_test.name AS teste,
    its_operations.xml_name as operação,
    its_operations.name as nome_operação,
    its_actions.parameter_identifier as acao,
    its_actions.behavior as tipo_acao,
    its_actions.status as result_acao,
    its_test_data.value as valor_esperado,
    its_test_data.current_value as valor_obtido,
    its_test.last_update_time as data_ultimo_update,
    its_test.test_id as id_test,
--    its_operations.operation_id AS id_operação,
    its_actions.action_id as id_acao,
    its_test.user_id as id_usuario
    
FROM its_test INNER JOIN its_operations ON its_test.test_id = its_operations.test_id
-- Selecione o que foi pedido do its_test e operations, processando apenas a intersecção com its_operations (baseado no test_id).
INNER JOIN its_actions ON its_operations.operation_id = its_actions.operation_id
-- De tudo isso processe a intersecção com its_acitons.
INNER JOIN its_request ON its_actions.action_id = its_request.action_id
-- De tudo isso processe a intersecção com its_request.
INNER JOIN its_test_data ON its_request.request_id = its_test_data.request_id
-- De tudo isso processe a intersecção com its_test_data.

WHERE LAST_UPDATE_TIME IS NOT NULL
ORDER BY LAST_UPDATE_TIME DESC, its_operations.xml_name ASC, its_actions.parameter_identifier ASC
-- Sem estes dois não teríamos a devida ordenação
FETCH FIRST 12 ROWS ONLY
```