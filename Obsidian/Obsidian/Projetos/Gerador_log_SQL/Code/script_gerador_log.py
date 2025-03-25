import cx_Oracle
import sys
import csv
import os

TABULACAO = 140
TABULACAO_MENOR = 30

query_1 = """
SELECT its_test.last_update_time,
       its_actions.action_id
FROM its_test

LEFT JOIN its_operations ON its_operations.test_id = its_test.test_id
LEFT JOIN its_actions ON its_actions.operation_id = its_operations.operation_id 

WHERE its_test.last_update_time >= SYSTIMESTAMP - interval '5' minute AND its_actions.status <> 'PASSED' AND its_actions.status IS NOT NULL -- Apenas STATUS FAILED
""" # nao pode possuir ponto e vírgula no final, framework não compreende

def consultar_bd(query_1):
    try:
        comandos_sql = cx_Oracle.connect(
            user='its_man', 
            password='maint#its06', 
            dsn=cx_Oracle.makedsn('ora-qa37', 1521, service_name='qa37')
        ).cursor() 
        
    except cx_Oracle.DatabaseError as falha_conexao:
        error, = falha_conexao.args
        print(f"{"_"*TABULACAO}")
        print(f"\n\033[1;31m"
        "\nBanco de Dados não conectado.")

        if error.code == 1017:
            print("\033[0;37m"
            "- Login não autorizado, verifique o nome de usuário e senha informados. Erro: cx_Oracle.DatabaseError 1017\n")
        print(f"{"_"*TABULACAO}")
        sys.exit()

    else:
        print(f"{"_"*TABULACAO}"
        "\n\033[1;32m"
        "\nBanco de Dados conectado com sucesso.", end="")

        print(f"\n\033[0;30m"
        "Consulta sendo feita analisando os últimos 5 minutos.\n")
        comandos_sql.execute(query_1)

        print("\033[0;37m"
        "- Consulta feita.")

        lista_dados_bd = comandos_sql.fetchall()
        print("- Consulta do Banco de Dados armazenados na variável lista_dados_bd.\n")

        print(f"\033[0;32mResultados últimos 5 minutos:\n{len(lista_dados_bd)} encontrados")
        if len(lista_dados_bd) > 0:
            for i in range(0 , len(lista_dados_bd)):
                print(f'\033[0;37m{lista_dados_bd[i]}') # Não tem problema estar em datetime.datetime. A Q2 usará assim no final mesmo.
        else:
            print(f'\033[0;31mNão foi encontrado dados para os últimos 5 minutos.\033[0;37m')
            print(f"{"_"*TABULACAO}")
            sys.exit()
        
        return lista_dados_bd, comandos_sql
    
def verificar_historico(lista_dados_bd, comandos_sql):
        try:
            with open ('historico.csv', 'r+', newline='') as historico: 
                if (os.path.getsize("./historico.csv") == 0):
                    print(f"{"-"*TABULACAO}")
                    print(f"\n\033[1;33m"
                    "Histórico de falhas está vazio."
                    "\033[0;30m\n"
                    "\nArmazenando falhas em histórico\033[0;37m\n")
                    csv.writer(historico).writerow(coluna[0] for coluna in comandos_sql.description) 
                    csv.writer(historico).writerows(lista_dados_bd)

                else:
                    print(f"{"-"*TABULACAO}"
                    "\n\033[1;34m"
                    "Histórico de falhas não está vazio."
                    "\033[0;30m\n"
                    "\nIniciando comparações.\033[0;37m")
                    comparar_lista_com_csv(lista_dados_bd)
        
        except FileNotFoundError as arquivo_nao_encontrado:
            print(f'\033[0;31m\nO arquivo "historico.csv" não foi encontrado. Certifique-se que está no mesmo diretório da execução (Erro: FileNotFoundError).\033[0;37m')
            print(f"{"_"*TABULACAO}")
            sys.exit()

def comparar_lista_com_csv(lista_dados_bd):
    with open('historico.csv', 'r+', newline='', encoding='latin1') as historico:
        lista_historico = list(csv.reader(historico, delimiter=','))
        ids_historico = [linha_historico[1] for linha_historico in lista_historico[1:] if len(linha_historico) > 1]
        datetime_historico = [linha_historico[0] for linha_historico in lista_historico[1:] if len(linha_historico) > 1]
        print(f"\033[0;30m\n"
        "Comparando ID.\033[0;37m")

        for linha in lista_dados_bd:
            id_lista_bd = str(linha[1])  
            datetime_lista_bd = str(linha[0])
            print(f'ID Lista_bd: {id_lista_bd}', end="")
            
            if id_lista_bd in ids_historico and datetime_lista_bd in datetime_historico:
                print(f" - Há também em historico com a mesma data. Ignorado.")
            else:
                print(f" - Caso novo (novo ID ou ID já presente em histórico mas com horário diferente)", end="")
                csv.writer(historico).writerow(linha)
                print(" - Salvo no Histórico de falhas de acordo com o Banco de Dados")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    lista_dados_bd, comandos_sql = consultar_bd(query_1)
    verificar_historico(lista_dados_bd, comandos_sql)

if __name__ == "__main__":
    main()