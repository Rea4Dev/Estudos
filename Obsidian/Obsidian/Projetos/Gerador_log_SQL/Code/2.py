import cx_Oracle
import csv
import os
import time
from typing import Optional, Tuple, List, Sequence
import logging

NIVEL_LOG = logging.DEBUG
MINUTOS_FILTRAGEM_QUERY1 = 5  # Normal é 5
SEGUNDOS_DELAY_SCRIPT = 10 # Normal é 300
SEGUNDOS_ERRO_CONEXAO = 5 # Normal é 5

query_1 = """
SELECT its_actions.datetime_start,
       its_actions.action_id
FROM its_actions
WHERE its_actions.datetime_start >= SYSTIMESTAMP - interval '""" + str(MINUTOS_FILTRAGEM_QUERY1) +"""' minute AND its_actions.status <> 'PASSED' AND its_actions.status IS NOT NULL
""" # nao pode possuir ponto e vírgula no final da query, framework não compreende

def consultar_bd(query_1: str) -> Optional[Tuple[List[tuple], Sequence]]:
    tentativas = 0
    while True:
        tentativas += 1

        try:
            comandos_sql = cx_Oracle.connect(
                user='its_man', 
                password='maint#its06', 
                dsn=cx_Oracle.makedsn('ora-qa37', 1521, service_name='qa37')
            ).cursor() 

            logging.info("\n" + "_" * 140 + "\n")
            logging.info("Banco de Dados conectado com sucesso.\n")
            logging.debug("| Consulta ao Banco de Dados buscando apenas acoes FAILED sendo feita analisando os ultimos " + str(MINUTOS_FILTRAGEM_QUERY1) + " minutos.")
                    
            comandos_sql.execute(query_1)
            logging.debug("| Consulta feita com sucesso!")

            lista_dados_bd = comandos_sql.fetchall()
            logging.debug("| Consulta armazenada na variavel lista_dados_bd.\n")
            logging.info("Resultados dos ultimos " + str(MINUTOS_FILTRAGEM_QUERY1) + " minutos: "  + f"{len(lista_dados_bd)} casos encontrados neste intervalo para analise.\n")

            if len(lista_dados_bd) > 0:
                for linha in lista_dados_bd:
                    logging.debug(f'| {linha}')
            else:
                logging.info(f"Esperando " + str(SEGUNDOS_DELAY_SCRIPT) + " segundos para proxima varredura.\n")
                time.sleep(SEGUNDOS_DELAY_SCRIPT)

            return lista_dados_bd, comandos_sql
        

        except cx_Oracle.DatabaseError as falha_conexao:
            error, = falha_conexao.args
            logging.critical("\n" + "_" * 140 + "\n")
            logging.critical("Banco de Dados nao conectado.")

            if error.code == 1017:
                logging.critical(f"{tentativas} tentativa - Login nao autorizado, verifique usuario/senha. Erro: cx_Oracle.DatabaseError 1017")
            else:
                logging.critical(f"{tentativas} tentativa - Verifique sua conexao, VPN e permissoes.")

            logging.debug("| Tentando novamente em " + str(SEGUNDOS_ERRO_CONEXAO) + " segundos\n")
            time.sleep(SEGUNDOS_ERRO_CONEXAO)
            continue
    


def verificar_historico(lista_dados_bd: list, comandos_sql: Sequence) -> None:
        try:
            with open ('historico.csv', 'r+', newline='') as historico: 
                if (os.path.getsize("./historico.csv") == 0):
                    logging.debug(f"| Historico de falhas esta vazio. Armazenando falhas em historico.csv.\n")
                    csv.writer(historico).writerow(coluna[0] for coluna in comandos_sql.description) 
                    csv.writer(historico).writerows(lista_dados_bd)
                    time.sleep(SEGUNDOS_DELAY_SCRIPT)

                else:
                    logging.debug(f"| Historico de falhas nao esta vazio. Iniciando comparacoes entre dados obtidos (lista_dados_bd) e dados presentes no historico (historico.csv).\n")
                    comparar_lista_com_csv(lista_dados_bd)
        
        except FileNotFoundError as arquivo_nao_encontrado:
            logging.warning(f'O arquivo "historico.csv" nao foi encontrado. (Erro: FileNotFoundError). Novo arquivo historico.csv criado.\n')
            open('historico.csv', 'w').close()
            verificar_historico(lista_dados_bd, comandos_sql)



def comparar_lista_com_csv(lista_dados_bd: list) -> None:
    with open('historico.csv', 'r+', newline='', encoding='latin1') as historico:
        lista_historico = list(csv.reader(historico, delimiter=','))
        ids_historico = [linha_historico[1] for linha_historico in lista_historico[1:] if len(linha_historico) > 1]
        datetime_historico = [linha_historico[0] for linha_historico in lista_historico[1:] if len(linha_historico) > 1]
        logging.debug(f"| Comparando ID.")

        if len(lista_dados_bd) == 0:
            logging.info("Ainda nao houveram novos dados. Aguardando novos dados...\n")

        else:
            for linha in lista_dados_bd:
                id_lista_bd = str(linha[1])  
                datetime_lista_bd = str(linha[0])

                if id_lista_bd in ids_historico and datetime_lista_bd in datetime_historico:
                    logging.debug(f"| ID Lista_bd: {id_lista_bd} - Ha tambem em historico com a mesma data. Ignorado.")
                else:
                    logging.debug(f"| ID Lista_bd: {id_lista_bd} - Caso novo (novo ID ou ID ja presente em historico mas com horario diferente) salvo no Historico de falhas de acordo com o Banco de Dados")
                    csv.writer(historico).writerow(linha)
            time.sleep(SEGUNDOS_DELAY_SCRIPT)



def main() -> None:
    logging.basicConfig(
    level = NIVEL_LOG,
    format = "%(levelname)s %(asctime)s %(message)s",
    datefmt = "%d-%m-%Y %H:%M:%S",
    filename = "script_gerador_hist.log",
    )
    while True:
        lista_dados_bd, comandos_sql = consultar_bd(query_1)
        verificar_historico(lista_dados_bd, comandos_sql)
        comandos_sql.close()



if __name__ == "__main__":
    main()