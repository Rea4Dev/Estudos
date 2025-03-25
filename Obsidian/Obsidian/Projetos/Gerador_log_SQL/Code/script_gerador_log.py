import cx_Oracle
import sys
import csv
import os
import time

TABULACAO = 140
TABULACAO_MENOR = 30

SEGUNDOS_DELAY_SCRIPT = 30
SEGUNDOS_ERRO_CONEXAO = 5
MINUTOS_FILTRAGEM_QUERY1 = 5

query_1 = """
SELECT its_test.last_update_time,
       its_actions.action_id
FROM its_test

LEFT JOIN its_operations ON its_operations.test_id = its_test.test_id
LEFT JOIN its_actions ON its_actions.operation_id = its_operations.operation_id 

WHERE its_test.last_update_time >= SYSTIMESTAMP - interval '""" + str(MINUTOS_FILTRAGEM_QUERY1) + """' minute AND its_actions.status <> 'PASSED' AND its_actions.status IS NOT NULL -- Apenas STATUS FAILED
""" # nao pode possuir ponto e vírgula no final, framework não compreende

def consultar_bd(query_1):
    tentativas = 0

    while True:
        tentativas += 1
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
                print(f"\033[0;37m [{tentativas}° tentativa] "
                "- Login não autorizado, verifique o nome de usuário e senha informados. Erro: cx_Oracle.DatabaseError 1017"
                "\n\nTentando novamente em " + str(SEGUNDOS_ERRO_CONEXAO) + " segundos\n")
                time.sleep(SEGUNDOS_ERRO_CONEXAO)
                continue
            else:
                print(f"\033[0;37m [{tentativas}° tentativa] "
                "- Verifique sua conexão, Zscaler, VPN e permissões.\nTentando novamente em " + str(SEGUNDOS_ERRO_CONEXAO) + " segundos\n")
                time.sleep(SEGUNDOS_ERRO_CONEXAO)
                continue

        else:
            print(f"{"_"*TABULACAO}"
            "\n\033[1;32m"
            "\nBanco de Dados conectado com sucesso.", end="")

            print(f"\n\033[0;30m"
            "Consulta sendo feita analisando os últimos " + str(MINUTOS_FILTRAGEM_QUERY1) +" minutos.\n")
            comandos_sql.execute(query_1)

            print("\033[0;37m"
            "- Consulta feita.")

            lista_dados_bd = comandos_sql.fetchall()
            print("- Consulta do Banco de Dados armazenados na variável lista_dados_bd.\n")

            print(f"\033[0;32mResultados últimos " + str(MINUTOS_FILTRAGEM_QUERY1) + f" minutos:\n{len(lista_dados_bd)} encontrados")
            if len(lista_dados_bd) > 0:
                for i in range(0 , len(lista_dados_bd)):
                    print(f'\033[0;37m{lista_dados_bd[i]}') # Não tem problema estar em datetime.datetime. A Q2 usará assim no final mesmo.
            else:
                print(f'\033[0;31mNão foi encontrado dados para os últimos '+ str(MINUTOS_FILTRAGEM_QUERY1) +' minutos.\033[0;37m')
                print(f"{"_"*TABULACAO}")
                time.sleep(SEGUNDOS_DELAY_SCRIPT)

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
                    time.sleep(SEGUNDOS_DELAY_SCRIPT)

                else:
                    print(f"{"-"*TABULACAO}"
                    "\n\033[1;34m"
                    "Histórico de falhas não está vazio."
                    "\033[0;30m\n"
                    "\nIniciando comparações.\033[0;37m")
                    comparar_lista_com_csv(lista_dados_bd)
        
        except FileNotFoundError as arquivo_nao_encontrado:
            print(f'\033[0;33m\nO arquivo "historico.csv" não foi encontrado. (Erro: FileNotFoundError).\033[0;37m\nNovo historico.csv criado.\n')
            open('historico.csv', 'w').close()
            verificar_historico(lista_dados_bd, comandos_sql)



def comparar_lista_com_csv(lista_dados_bd):
    with open('historico.csv', 'r+', newline='', encoding='latin1') as historico:
        lista_historico = list(csv.reader(historico, delimiter=','))
        ids_historico = [linha_historico[1] for linha_historico in lista_historico[1:] if len(linha_historico) > 1]
        datetime_historico = [linha_historico[0] for linha_historico in lista_historico[1:] if len(linha_historico) > 1]
        print(f"\033[0;30m\n"
        "Comparando ID.\033[0;37m")

        if len(lista_dados_bd) == 0:
            print("\nDesde a criação, não houveram novos dados.\n")
            print("\033[0;30mAguardando novos dados...\033[0;37m")
            print(f"{"-"*TABULACAO}")

        else:
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
            time.sleep(SEGUNDOS_DELAY_SCRIPT)



def main():
    lista_dados_bd, comandos_sql = consultar_bd(query_1)
    verificar_historico(lista_dados_bd, comandos_sql)



if __name__ == "__main__":
    execucao = 0
    while True:
        execucao += 1
        main()
        print("\n\033[1;34mAguardando 5 minutos para a próxima execução... \033[0;37m")
        print(f"Execução atual: {execucao}° às {time.strftime("%H:%M:%S")}")
        # time.sleep(300)