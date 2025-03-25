MINUTOS_FILTRAGEM_QUERY1 = 5
query_1 = """
SELECT its_test.last_update_time,
       its_actions.action_id
FROM its_test

LEFT JOIN its_operations ON its_operations.test_id = its_test.test_id
LEFT JOIN its_actions ON its_actions.operation_id = its_operations.operation_id 

WHERE its_test.last_update_time >= SYSTIMESTAMP - interval '""" + str(MINUTOS_FILTRAGEM_QUERY1) + """' minute AND its_actions.status <> 'PASSED' AND its_actions.status IS NOT NULL -- Apenas STATUS FAILED
"""

print(query_1)