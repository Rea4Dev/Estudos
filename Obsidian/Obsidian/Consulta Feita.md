```SQL
SELECT its_actions.behavior,
       its_actions.status,
       its_actions.parameter_identifier,
       its_actions.action_id,
       AB.test_id,
       AB.user_id,
       AB.last_update_time,
       AB.op,
       AB.mmc,
       AB.operation_id,
       AB.xml_name
FROM its_actions
FULL OUTER JOIN (
    SELECT its_test.*,
           its_operations.operation_id,
           its_operations.xml_name
    FROM its_test
    FULL OUTER JOIN its_operations ON its_test.test_id = its_operations.test_id
    WHERE its_test.last_update_time IS NOT NULL
) AB ON its_actions.operation_id = AB.operation_id
WHERE TEST_ID is not null
ORDER BY LAST_UPDATE_TIME DESC, AB.xml_name ASC, its_actions.parameter_identifier ASC;
```
