# Query SQL
Foi solicitado que, até sexta, eu fizesse uma Query SQL utilizando de chaves primárias, relacionamentos e Join para filtrar os dados relevantes e da forma como desejamos operar. 
Quando pronta a Query, uma simulação será feita e irei manualmente anotar sempre que houver diferença no Status da action.

Atualizações: Terminei a Query
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

---
# Análise Ação-Reação 
Com a Query feita, realizarei uma análise de ação-reação para garantir que as instâncias de fato sofrem um update quando refeito a mesma action.

- Hipotese 1:
O ID da action se mantém em execuções diferentes?
	- Caso sim:
	De fato a tabela apenas sofre um update no registro em questão (o que faz sentido ao pensar em volume de dados)
	- Caso não:
	A tabela insere de fato novos valores a cada re-execução. Volume de dados não otimizado.

- Resultado observado:
	Atualmente apenas as etapas A e B de 1.0 foram efetuadas e PASSED. O TEST_ID apontado é 37179.
	Após a re-execução, o TEST_ID apontado se manteve 37179.

De fato a tabela apenas sofre um update no registro em questão (o que faz sentido ao pensar em volume de dados)

---
# Relacionamentos
Aqui mostra como é estruturado o relacionamento das entidades.
Acessee clicando [[Relacionamentos|Aqui]]

---
# Elaboração Trigger

Criando Tabela de Histórico
```SQL
CREATE TABLE its_actions_history (
    history_id        NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    action_id         NUMBER,
    old_behavior      VARCHAR2(100),
    new_behavior      VARCHAR2(100),
    old_status        VARCHAR2(50),
    new_status        VARCHAR2(50),
    old_parameter     VARCHAR2(100),
    new_parameter     VARCHAR2(100),
    operation_id      NUMBER,
    changed_at        TIMESTAMP DEFAULT SYSTIMESTAMP,
    changed_by        VARCHAR2(100)
);
```

Criando o Trigger
```SQL
CREATE OR REPLACE TRIGGER trg_its_actions_history
BEFORE UPDATE ON its_actions
FOR EACH ROW
WHEN (OLD.status != NEW.status OR OLD.parameter_identifier != NEW.parameter_identifier OR OLD.behavior != NEW.behavior)
BEGIN
    INSERT INTO its_actions_history (
        action_id,
        old_behavior,
        new_behavior,
        old_status,
        new_status,
        old_parameter,
        new_parameter,
        operation_id,
        changed_at,
        changed_by
    ) VALUES (
        :OLD.action_id,
        :OLD.behavior,
        :NEW.behavior,
        :OLD.status,
        :NEW.status,
        :OLD.parameter_identifier,
        :NEW.parameter_identifier,
        :OLD.operation_id,
        SYSTIMESTAMP,
        SYS_CONTEXT('USERENV','SESSION_USER')
    );
END;
/
```

Após pedir permissão ao Wendel para criar tabelas, foi-me informado que não temos acesso DDL ao servidor WebSIT.
> Além disso, *uso de triggers é desencorajado* devido a potenciais problemas com segurança, performance, migração e versionamento de servidores. 

Desta forma, abandono esta possibilidade.

---
# Floxograma Algoritmo
Elaboro e seguirei este fluxograma no desenvolvimento do código em Python.
Acesse clicando [[Algoritmo.canvas|aqui]]

---
# Desenvolvimento Script Python

# Old
## Estruturação 01 - Abandonada
```Python
import time
import cx_Oracle
import csv

dsn_tns = cx_Oracle.makedsn('ora-qa37', 1521, service_name='qa37')
connection = cx_Oracle.connect(user='its_man', password='maint#its06', dsn=dsn_tns)
cursor = connection.cursor()
  
query = """SELECT * FROM (
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
    WHERE AB.test_id IS NOT NULL
    ORDER BY AB.last_update_time DESC, AB.xml_name ASC, its_actions.parameter_identifier ASC
)
WHERE ROWNUM <= 10"""

last_status = {}


with open('alteracoes.csv', mode='w', newline='', encoding='utf-8') as csv_file:

    cursor.execute(query)
    results = cursor.fetchall()
    column_names = [col[0] for col in cursor.description]
    writer = csv.writer(csv_file)
    writer.writerow(column_names)

print("Monitorando alterações...")


while True:
    cursor.execute(query)
    results = cursor.fetchall()

    changes = []
    for row in results:

        action_id = row[3]
        status = row[1]  
        if action_id in last_status:
            if last_status[action_id] != status:
                changes.append(row)
                last_status[action_id] = status  
        else:
            last_status[action_id] = status
    if changes:
    
        with open('alteracoes.csv', mode='a', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(changes)
        print(f"{len(changes)} alteração(ões) registrada(s).")

    time.sleep(3)

cursor.close()
connection.close()
```
Problemas observados:
- Sobrescreve a cada execução
- Por sobrescrever, não está comparando 

Possíveis solulçoes:
- Criar um script ou função secundária que iria filtrar apenas os não repetidos do arquivo (mais fácil porém mais informal).
- Mudar o core do código (mais difícil porém mais formal)

Ação escolhida:
- Mudar o core do código.

## Estruturação 02 - Não adotada
Irie, ao invés de fazer o script todo, fazer ele em parte e validá-lo sempre antes da próxima alteração.
Algumas versões deste 02 podem não estar de acordo com a versão final, entretanto, aqui viso a robustez antes da compatibilidade com o esperado.

- Objetivo 1: Desenvolver código capaz de fazer query sql
```SQL
import cx_Oracle

dsn_tns = cx_Oracle.makedsn('ora-qa37', 1521, service_name='qa37')
connection = cx_Oracle.connect(user='its_man', password='maint#its06', dsn=dsn_tns)

query = """SELECT * FROM (
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
    ORDER BY LAST_UPDATE_TIME DESC, AB.xml_name ASC, its_actions.parameter_identifier ASC
) WHERE ROWNUM <= 10"""

cursor = connection.cursor()
cursor.execute(query)
results = cursor.fetchall()

for row in results:
    print(row)
  
cursor.close()
connection.close()
```


# Atual
## 01 - Consulta Básica
De acordo com o Fluxograma do Algoritmo, esta é a primeira parte do desenvolvimento, uma mera aplicação da consulta SQL já feita.
```Python
# O código está baseado no meu algoritmo, no Obsidian. Os comentários acima dos blocos descrevem uma etapa do fluxo e os comentários após códigos são para auxiliar no entendimento.

# Início
import cx_Oracle
import csv
import os

# Retângulo 01
consulta = """
SELECT * FROM (
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
    ORDER BY LAST_UPDATE_TIME DESC, AB.xml_name ASC, its_actions.parameter_identifier ASC
) WHERE ROWNUM <= 10
""" # nao pode possuir ponto e vírgula no final, framework não compreende
cursor_Oracle = cx_Oracle.connect(user='its_man', password='maint#its06', dsn=cx_Oracle.makedsn('ora-qa37', 1521, service_name='qa37')).cursor() # .cursor cria um objeto que permite executar comandos SQL e gerenciar os resultados de consultas

# Retângulo 02
cursor_Oracle.execute(consulta) # consulta é feita
armazenagem_intermediaria = cursor_Oracle.fetchall() # arnazenagem intermediaria dos resultados

# Não presente. Apenas para fechar.
cursor_Oracle.close()
cx_Oracle.connect(user='its_man', password='maint#its06', dsn=cx_Oracle.makedsn('ora-qa37', 1521, service_name='qa37')).close()
```

## 02 - Consulta Complementar
```Python
# O código está baseado no meu algoritmo, no Obsidian. Os comentários acima dos blocos descrevem uma etapa do fluxo e os comentários após códigos são para auxiliar no entendimento.

# Início
import cx_Oracle
import csv
import os

# Retângulo 01
consulta = """
SELECT * FROM (
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
    ORDER BY LAST_UPDATE_TIME DESC, AB.xml_name ASC, its_actions.parameter_identifier ASC
) WHERE ROWNUM <= 10
""" # nao pode possuir ponto e vírgula no final, framework não compreende
cursor_Oracle = cx_Oracle.connect(user='its_man', password='maint#its06', dsn=cx_Oracle.makedsn('ora-qa37', 1521, service_name='qa37')).cursor() # .cursor cria um objeto que permite executar comandos SQL e gerenciar os resultados de consultas

# Retângulo 02
cursor_Oracle.execute(consulta) # consulta é feita
armazenagem_intermediaria = cursor_Oracle.fetchall() # arnazenagem intermediaria dos resultados

# Condicional 1
if (os.path.getsize("./historico.csv") == 0):
    # C1 "Sim" | Condicional 2
    with open ('historico.csv', 'w', newline='') as documento: # documento criado/sobrescrito
        csv.writer(documento).writerow(coluna[0] for coluna in cursor_Oracle.description) # escreve cabeçalho
        csv.writer(documento).writerows(armazenagem_intermediaria) # escreve as linhas com base na armazenagem intermediaria. Linah 14 garante quebra de linha entre infos.
        print("\n\n ele é zero, sobrescrito \n\n") # controle. Apagar
else:
    # C1 "Não"
    with open ('historico.csv', 'r+', newline='', encoding='utf-8') as documento:
        i = 0
        lista_documento = list(csv.reader(documento))
        for linha in armazenagem_intermediaria:
            i += 1
            print(f'{linha[1]} é igual a {lista_documento[i][1]}') # BESEADO EM POSIÇÃO, NÃO EM CHAVE PRIMÁRIA
            if (linha[1] == lista_documento[i][1]):
                #C2 "Sim"
                print("É igual")
            else:
                #C2 "Não"
                print("Não é igual")
                csv.writer(documento).writerow(linha) # Parei aqui. Está funcionando
        

    #print(f'\n\n ele n é zero n\n\n {armazenagem_intermediaria}') # controle. Apagar

# Não presente. Apenas para fechar.
cursor_Oracle.close()
cx_Oracle.connect(user='its_man', password='maint#its06', dsn=cx_Oracle.makedsn('ora-qa37', 1521, service_name='qa37')).close()

            #PA_status_documento = 2 + (i-1)*11
            #print(f'\n{linha}')
            #print(f'{linha[1]}\n')
```