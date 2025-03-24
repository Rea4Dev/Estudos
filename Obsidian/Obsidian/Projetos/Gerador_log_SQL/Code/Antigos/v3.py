import cx_Oracle
import csv
import os
import sys
import time
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
FETCH FIRST 2 ROWS ONLY
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
        #time.sleep(3)

        print(f"\n\033[0;30m"
        "Consulta sendo feita. Aguarde...\n")
        comandos_sql.execute(query_sql)

        print("\033[0;37m"
        "- Consulta feita.")
        #time.sleep(1)

        dados_bd = comandos_sql.fetchall()
        print("- Consulta do Banco de Dados armazenados na variável dados_bd.")
        time.sleep(4)
        
        return dados_bd, comandos_sql

def tratar_hist(dados_bd, comandos_sql):
    with open ('historico.csv', 'r+', newline='') as historico: 
        if (os.path.getsize("./historico.csv") == 0):
            #time.sleep(1)
            print(f"\n\033[1;33m"
            "Histórico está vazio."
            "\033[0;30m\n"
            "\nArmazenando tudo de dados_bd em histórico\033[0;37m\n")
            #time.sleep(1)

            csv.writer(historico).writerow(coluna[0] for coluna in comandos_sql.description) 
            csv.writer(historico).writerows(dados_bd)
    
        else:
            #time.sleep(1)
            print(f"{"-"*TABULACAO}"
            "\n\033[1;34m"
            "Histórico não está vazio."
            "\033[0;30m\n"
            "\nIniciando processo de percorrer Banco de Dados e Histórico\033[0;37m\n")
            time.sleep(4)
            lista_historico = list(csv.reader(historico))
            percorrer_bd(historico, dados_bd, lista_historico)
            
def percorrer_bd(historico, dados_bd, lista_historico):
    z = 0
    for linha_bd in dados_bd:
        z += 1
        print(f"\033[0;37m{"_"*TABULACAO_MENOR} Percorrendo Banco de Dados: \033[1;34mlinha {z} do Banco de Dados\033[0;37m{"_"*TABULACAO_MENOR}")

        #time.sleep(1)
        print(f"\n- Conteúdo: "
        "\033[0;30m", end="")
        print(f"{linha_bd}\033[0;37m")
        
        action_id_bd = int(linha_bd[13])
        result_linha_bd = str(linha_bd[8])
        #time.sleep(0.1)
        print(f"- Action ID: \033[1;30m{action_id_bd}\033[0;37m")
        #time.sleep(0.1)
        print(f"- Resultado: \033[1;30m{result_linha_bd}\033[0;37m\n")
        #time.sleep(3)

        percorrer_hist(historico, lista_historico, linha_bd, action_id_bd, result_linha_bd, z)

def percorrer_hist(historico, lista_historico, linha_bd, action_id_bd, result_linha_bd, z):
    for n, linha in enumerate(lista_historico[1:]):
        #time.sleep(0.1)
        print(f"\n\033[0;30mPercorrendo Histórico: procurando ID equivalente na \033[0;35mlinha {n+1}\033[0;30m do Histórico...")
        status_linha_hist = str(linha[8])
        action_id_linha_hist = linha[13]
        #time.sleep(0.1)
        print(f"    - ID linha {n+1} histórico: {action_id_linha_hist}")
        
        if (action_id_bd == int(action_id_linha_hist)):
            #time.sleep(0.1)   
            print(f"\033[1;30mIDs iguais na linha {n+1}!\033[0;33m") 
            if ((result_linha_bd == status_linha_hist) or (status_linha_hist == "" and result_linha_bd == "None")):
                print(f"Histórico \"{status_linha_hist}\" == Banco de Dados \"{result_linha_bd}\" | STATUS é o mesmo. Ignorar\033[0;37m\n")
                #time.sleep(1)
            else:
                print("\033[1;32m"
                "STATUS diferente! Armazenar de acordo com Banco de Dados"
                "\033[0;37m\n")
                global equivalentes_validos
                equivalentes_validos[action_id_linha_hist] = status_linha_hist, f"linha {n+1} do histórico"
                csv.writer(historico).writerow(linha_bd) 
                #time.sleep(1)
        else:
            print("IDs diferentes. Linha ignorada.\n") 

def main():
    os.system('cls')
    dados_bd, comandos_sql = consultar_bd(query_sql)
    tratar_hist(dados_bd, comandos_sql)
    comandos_sql.close()

    print(f"{"\033[0;37m-"*TABULACAO}"
    "\033[1;37m\nResultado\033[0;37m:")

    print(f"\nQuantidade armazenada de IDs presente em ambos e com status diferente: {len(equivalentes_validos)}\n{equivalentes_validos}.")
    print(f"\n\033[1;32mConexão com banco de dados fechada.\n{"\033[0;37m-"*TABULACAO}")

if __name__ == "__main__":
    main()