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