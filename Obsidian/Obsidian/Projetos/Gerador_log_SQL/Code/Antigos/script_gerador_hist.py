import cx_Oracle
import csv
import os
import time
from typing import Optional, Tuple, List, Sequence
import logging
logging.basicConfig(
    level = logging.DEBUG,
    format = "%(levelname)s %(asctime)s %(message)s",
    datefmt = "%d-%m-%Y %H:%M:%S",
    filename = "script_gerador_hist.log",
    )

TABULACAO = 140
TABULACAO_MENOR = 30

MINUTOS_FILTRAGEM_QUERY1 = 5 
SEGUNDOS_DELAY_SCRIPT = 20
SEGUNDOS_ERRO_CONEXAO = 5

query_1 = """
SELECT its_actions.datetime_start,
       its_actions.action_id
FROM its_actions
WHERE its_actions.datetime_start >= SYSTIMESTAMP - interval '""" + str(MINUTOS_FILTRAGEM_QUERY1) +"""' minute AND its_actions.status <> 'PASSED' AND its_actions.status IS NOT NULL -- Apenas STATUS FAILED
""" # nao pode possuir ponto e vírgula no final da query, framework não compreende

def consultar_bd(query_1: str) -> Optional[Tuple[List[tuple], Sequence]]:
    tentativas = 0

    while True:
        tentativas += 1

        try:
            with cx_Oracle.connect( # 'with' para garantir que a conexão seja fechada após o bloco
                user='its_man', 
                password='maint#its06', 
                dsn=cx_Oracle.makedsn('ora-qa37', 1521, service_name='qa37')
            ) as conexao:
                with conexao.cursor() as comandos_sql: # 'with' para garantir que o cursor seja fechado automaticamente
                    print("_" * TABULACAO)
                    print("\033[1;32mBanco de Dados conectado com sucesso.")
                    print("\033[0;30mConsulta sendo feita analisando os últimos " 
                          + str(MINUTOS_FILTRAGEM_QUERY1) + " minutos.\n")
                    
                    comandos_sql.execute(query_1)
                    print("\033[0;37m- Consulta feita.")

                    lista_dados_bd = comandos_sql.fetchall()
                    print("- Consulta do Banco de Dados armazenada na variável lista_dados_bd.\n")
                    print("\033[0;32mResultados dos últimos " 
                          + str(MINUTOS_FILTRAGEM_QUERY1) + " minutos:\n" 
                          + f"{len(lista_dados_bd)} encontrados")

                    if len(lista_dados_bd) > 0:
                        for linha in lista_dados_bd:
                            print(f'\033[0;37m{linha}')
                    else:
                        print(f'\033[0;31mNão foi encontrado dados para os últimos '
                              + str(MINUTOS_FILTRAGEM_QUERY1) + ' minutos.\033[0;37m'
                              + "\n" + "_" * TABULACAO)
                        time.sleep(SEGUNDOS_DELAY_SCRIPT)

                    # Retorna os dados e a descrição (se necessário para outras funções)
                    return lista_dados_bd, comandos_sql.description

        except cx_Oracle.DatabaseError as falha_conexao:
            error, = falha_conexao.args
            print("\n" + "_" * TABULACAO)
            print("\033[1;31mBanco de Dados não conectado.")

            if error.code == 1017:
                print(f"\033[0;37m [{tentativas}° tentativa] - Login não autorizado, verifique usuário/senha. Erro: cx_Oracle.DatabaseError 1017")
            else:
                print(f"\033[0;37m [{tentativas}° tentativa] - Verifique sua conexão, VPN e permissões.")

            print("\nTentando novamente em " + str(SEGUNDOS_ERRO_CONEXAO) + " segundos\n")
            time.sleep(SEGUNDOS_ERRO_CONEXAO)
            continue
    


def verificar_historico(lista_dados_bd: list, comandos_sql: Sequence) -> None:
        try:
            with open ('historico.csv', 'r+', newline='') as historico: 
                if (os.path.getsize("./historico.csv") == 0):
                    print(f"{"-"*TABULACAO}"
                    "\n\033[1;33m"
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



def comparar_lista_com_csv(lista_dados_bd: list) -> None:
    with open('historico.csv', 'r+', newline='', encoding='latin1') as historico:
        lista_historico = list(csv.reader(historico, delimiter=','))
        ids_historico = [linha_historico[1] for linha_historico in lista_historico[1:] if len(linha_historico) > 1]
        datetime_historico = [linha_historico[0] for linha_historico in lista_historico[1:] if len(linha_historico) > 1]
        print(f"\033[0;30m\n"
        "Comparando ID.\033[0;37m")

        if len(lista_dados_bd) == 0:
            print("\nDesde a criação, não houveram novos dados.\n"
            "\n\033[0;30mAguardando novos dados...\033[0;37m"
            f"\n{"-"*TABULACAO}")

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



def main() -> None:
    lista_dados_bd, comandos_sql = consultar_bd(query_1)
    verificar_historico(lista_dados_bd, comandos_sql)



if __name__ == "__main__":
    execucao = 0
    while True:
        execucao += 1
        main()
        print("\n\033[1;34mAguardando 5 minutos para a próxima execução... \033[0;37m"
        f"\nExecução atual: {execucao}° às {time.strftime("%H:%M:%S")}")