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
dados_BD = cursor_Oracle.fetchall() # arnazenagem intermediaria dos resultados

# Condicional 1 "Sim"
if (os.path.getsize("./historico.csv") == 0):
    with open ('historico.csv', 'w', newline='') as historico: # documento criado/sobrescrito
        csv.writer(historico).writerow(coluna[0] for coluna in cursor_Oracle.description) # escreve cabeçalho
        csv.writer(historico).writerows(dados_BD) # escreve as linhas com base na armazenagem intermediaria. Linha 14 garante quebra de linha entre infos.
        print("\n\n ele é zero, sobrescrito \n\n") # controle. Apagar

# Condicional 1 "Não"
else:
    with open ('historico.csv', 'r+', newline='', encoding='utf-8') as historico:
        lista_historico = list(csv.reader(historico))

        for linhaBD in dados_BD:
            i = 0
            action_id_bd = int(linhaBD[3])
            status_linha_bd = str(linhaBD[1])
            
            for n, linha in enumerate(lista_historico[1:]):
                i += 1
                status_linha_hist = str(linha[1]) 
                action_id_linha_hist = int(linha[3])
                print(f'Buscar {action_id_bd} na linha {linha}') # Teste
            
                if (action_id_bd == action_id_linha_hist): # Condicional 2     
                    if ((status_linha_bd == status_linha_hist) or (status_linha_hist == "" and status_linha_bd == "None")): # Condicional 2 "Sim" | # Condicional 3 | # compara STATUS 
                        print("São iguais. Ignorar.\n") # Condicional 3 "Sim"
                    else:
                        print("Não são iguais! Salvar\n") # Condicional 3 "Não"
                        csv.writer(historico).writerow(linhaBD) 
        
# Não presente. Apenas para fechar.
cursor_Oracle.close()
cx_Oracle.connect(user='its_man', password='maint#its06', dsn=cx_Oracle.makedsn('ora-qa37', 1521, service_name='qa37')).close()