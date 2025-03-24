import cx_Oracle
import csv
import os
import sys
TABULACAO = 140
TABULACAO_MENOR = 30
equivalentes_validos = {}

query_sql = """
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
""" # nao pode possuir ponto e vírgula no final, framework não compreende

def consultar_bd(query_sql):
    try:
        comandos_sql = cx_Oracle.connect(
            user='its_man', 
            password='maint#its06', 
            dsn=cx_Oracle.makedsn('ora-qa37', 1521, service_name='qa37')
        ).cursor() 
        
    except cx_Oracle.DatabaseError as falha_conexao:
        error, = falha_conexao.args
        print(f"\n\033[1;31m"
        "Banco de Dados não conectado.")

        if error.code == 1017:
            print("\033[0;37m"
            "- Login não autorizado, verifique o nome de usuário e senha informados. Erro: cx_Oracle.DatabaseError 1017\n")
        sys.exit()

    else:
        print(f"{"-"*TABULACAO}"
        "\n\033[1;32m"
        "Banco de Dados conectado com sucesso.")

        print(f"\n\033[0;30m"
        "Consulta sendo feita. Aguarde...\n")
        comandos_sql.execute(query_sql)

        print("\033[0;37m"
        "- Consulta feita.")

        lista_dados_bd = comandos_sql.fetchall()
        print("- Consulta do Banco de Dados armazenados na variável dados_bd.")
        
        return lista_dados_bd, comandos_sql

def verificar_historico(lista_dados_bd, comandos_sql):
        with open ('historico.csv', 'r+', newline='') as historico: 
            if (os.path.getsize("./historico.csv") == 0):
                print(f"\n\033[1;33m"
                "Histórico está vazio."
                "\033[0;30m\n"
                "\nArmazenando tudo de dados_bd em histórico\033[0;37m\n")

                csv.writer(historico).writerow(coluna[0] for coluna in comandos_sql.description) 
                csv.writer(historico).writerows(lista_dados_bd)
        
            else:
                print(f"{"-"*TABULACAO}"
                "\n\033[1;34m"
                "Histórico não está vazio."
                "\033[0;30m\n"
                "\nIniciando processo de percorrer Banco de Dados e Histórico\033[0;37m\n")

def comparar_lista_com_csv(lista_dados_bd):
    with open('historico.csv', 'r+', newline='', encoding='latin1') as historico:
        lista_historico = list(csv.reader(historico, delimiter=','))
        ids_historico = [linha_historico[13] for linha_historico in lista_historico[1:] if len(linha_historico) > 13]

        for linha in lista_dados_bd:
            id_lista_bd = str(linha[13])  
            
            if id_lista_bd in ids_historico:
                status_lista_bd = linha[8]  
                status_historico = lista_historico[ids_historico.index(id_lista_bd) + 1][8] 

                if status_lista_bd == status_historico:
                    print(f'\033[0;30mID: {id_lista_bd} encontrado no arquivo historico.csv com status correspondente: {status_lista_bd}\033[0;37m')
                else:
                    print(f'\033[1;30mID: {id_lista_bd} encontrado no arquivo historico.csv, mas com status diferente (BD: {status_lista_bd}, Histórico: {status_historico}\033[0;37m)')
                    csv.writer(historico).writerow(linha) 
            else:
                print(f'ID: {id_lista_bd} não encontrado no arquivo historico.csv')

def main():
    os.system('cls')
    lista_dados_bd, comandos_sql = consultar_bd(query_sql)
    verificar_historico(lista_dados_bd, comandos_sql)
    comparar_lista_com_csv(lista_dados_bd)

if __name__ == "__main__":
    main()