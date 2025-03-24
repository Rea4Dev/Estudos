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
    its_actions.action_id as id_acao,
    its_test.user_id as id_usuario
    
FROM its_test 
INNER JOIN its_operations ON its_test.test_id = its_operations.test_id
INNER JOIN its_actions ON its_operations.operation_id = its_actions.operation_id
INNER JOIN its_request ON its_actions.action_id = its_request.action_id
INNER JOIN its_test_data ON its_request.request_id = its_test_data.request_id

WHERE LAST_UPDATE_TIME IS NOT NULL
ORDER BY LAST_UPDATE_TIME DESC, its_operations.xml_name ASC, its_actions.parameter_identifier ASC
FETCH FIRST 2500 ROWS ONLY
"""

def consultar_bd(query_sql):
    try:
        comandos_sql = cx_Oracle.connect(
            user='its_man', 
            password='maint#its06', 
            dsn=cx_Oracle.makedsn('ora-qa37', 1521, service_name='qa37')
        ).cursor() 
        
    except cx_Oracle.DatabaseError as falha_conexao:
        error, = falha_conexao.args
        print("\n\033[1;31mBanco de Dados não conectado.")

        if error.code == 1017:
            print("\033[0;37m- Login não autorizado, verifique o nome de usuário e senha informados.\n")
        sys.exit()

    else:
        print(f"{'-'*TABULACAO}\n\033[1;32mBanco de Dados conectado com sucesso.")
        print("\n\033[0;30mConsulta sendo feita. Aguarde...\n")
        comandos_sql.execute(query_sql)

        print("\033[0;37m- Consulta feita.")
        dados_bd = comandos_sql.fetchall()
        print("- Consulta do Banco de Dados armazenada na variável dados_bd.")
        os.system('cls')
        
        return dados_bd, comandos_sql

def carregar_historico():
    historico_dict = {}
    
    if not os.path.exists("historico.csv") or os.path.getsize("historico.csv") == 0:
        print("\n\033[1;33mHistórico está vazio. Armazenando tudo de dados_bd em histórico\033[0;37m\n")
        return historico_dict, []

    with open("historico.csv", "r", newline='') as historico:
        leitor = csv.reader(historico)
        colunas = next(leitor)  # Cabeçalho
        for linha in leitor:
            action_id = linha[13]  # Índice do action_id
            historico_dict[action_id] = linha  # Armazena a linha completa
    
    return historico_dict, colunas

def tratar_hist(dados_bd, comandos_sql):
    historico_dict, colunas = carregar_historico()
    
    with open("historico.csv", "a", newline='') as historico:
        escritor_csv = csv.writer(historico)

        if not historico_dict:  # Se o histórico estiver vazio, escrever cabeçalho e todas as linhas
            escritor_csv.writerow([coluna[0] for coluna in comandos_sql.description])
            escritor_csv.writerows(dados_bd)
            return

        verificar_novos_dados(dados_bd, historico_dict, escritor_csv)

def verificar_novos_dados(dados_bd, historico_dict, escritor_csv):
    for linha_bd in dados_bd:
        action_id_bd = str(linha_bd[13])
        result_bd = str(linha_bd[8])

        if action_id_bd in historico_dict:
            status_hist = str(historico_dict[action_id_bd][8])

            if result_bd != status_hist:
                print(f"\033[1;32mSTATUS diferente! Adicionando nova linha para {action_id_bd}.\033[0;37m")
                escritor_csv.writerow(linha_bd)
                equivalentes_validos[action_id_bd] = (status_hist, result_bd)
        else:
            print(f"\033[1;34mNovo ID encontrado ({action_id_bd}), ignorando...\033[0;37m")

def main():
    os.system('cls')
    dados_bd, comandos_sql = consultar_bd(query_sql)
    tratar_hist(dados_bd, comandos_sql)
    comandos_sql.close()

    print(f"\033[0;37m{'-'*TABULACAO}\033[1;37m\nResultado\033[0;37m:")
    print(f"\nQuantidade armazenada de IDs com status diferente: {len(equivalentes_validos)}\n{equivalentes_validos}.")
    print(f"\n\033[1;32mConexão com banco de dados fechada.\n{'-'*TABULACAO}")

if __name__ == "__main__":
    main()