import cx_Oracle
import csv
import time
from typing import Optional, Tuple, List, Sequence
import logging
from collections import defaultdict

NIVEL_LOG = logging.DEBUG
MINUTOS_FILTRAGEM_QUERY1 = 5  # Normal é 5
SEGUNDOS_DELAY_SCRIPT = 10 # Normal é 300
SEGUNDOS_ERRO_CONEXAO = 5 # Normal é 5



def armazenar_id_historico():
    with open("historico.csv", "r") as historico:
        armazenagem_hist = csv.reader(historico)
        next(armazenagem_hist)  

        list_id_hist = [linha[1] for linha in armazenagem_hist]  

    logging.info("\n" + "_" * 140 + "\n")
    logging.debug('"armazenar_id_historico()"')
    logging.debug(f"Lista de ID do historico (list_id_hist): {list_id_hist}\n")
    
    return list_id_hist



def conectar_bd(query_2: str) -> Optional[Tuple[List[tuple], Sequence]]:
    tentativas = 0
    while True:
        tentativas += 1

        try:
            comandos_banco = cx_Oracle.connect(
                user='its_man', 
                password='maint#its06', 
                dsn=cx_Oracle.makedsn('ora-qa37', 1521, service_name='qa37')
            ).cursor()

            logging.debug('"conectar_bd()"')
            logging.info("Banco de Dados conectado com sucesso.")
            logging.debug("| Triangulando IDs.")
                    
            comandos_banco.execute(query_2)
            retorno_query_2 = comandos_banco.fetchall()

            if len(retorno_query_2) > 0:
                for linha in retorno_query_2:
                    logging.debug(f'| {linha}')
            logging.debug("| (Acima estao apenas os IDS unicos. IDs repetidos nao aparecem acima, mas sao computados.)")
            logging.debug("| Consulta armazenada na variavel retorno_query_2.\n")

            return retorno_query_2, comandos_banco
        
        except cx_Oracle.DatabaseError as falha_conexao:
            error, = falha_conexao.args
            logging.debug('"conectar_bd()"')
            logging.critical("Banco de Dados nao conectado.")

            if error.code == 1017:
                logging.critical(f"{tentativas} tentativa - Login nao autorizado, verifique usuario/senha. Erro: cx_Oracle.DatabaseError 1017")
            else:
                logging.critical(f"{tentativas} tentativa - Verifique sua conexao, VPN e permissoes.")

            logging.debug("| Tentando novamente em " + str(SEGUNDOS_ERRO_CONEXAO) + " segundos\n")
            time.sleep(SEGUNDOS_ERRO_CONEXAO)
            continue



def adicionar_query_visu_csv(retorno_query_2, comandos_banco):
    logging.debug('"adicionar_query_visu_csv()"')
    logging.info("Gerando visualizacao crua\n")
    with open("visualizacao.csv", "w", newline='') as visu:
        csv.writer(visu).writerow(coluna[0] for coluna in comandos_banco.description)
        csv.writer(visu).writerows(retorno_query_2)



def adicionar_horarios_visualizacao():
    logging.debug('"adicionar_horarios_visualizacao()"')
    logging.info("Gerando visualizacao + horario")

    # {id: [horario1, horario2, ...]}
    historico_dict = {}
    with open("historico.csv", "r", newline="") as historico:
        leitor_hist = csv.reader(historico)
        next(leitor_hist)  
        for linha in leitor_hist:
            horario, id_hist = linha[0], linha[1]
            historico_dict.setdefault(id_hist, []).append(horario)
            logging.debug(f"horario = {horario} | id_hist = {id_hist}")

    with open("visualizacao.csv", "r", newline="") as visu:  
        dict_reader = csv.DictReader(visu)
        fieldnames = dict_reader.fieldnames  
        lista_linhas_visu = list(dict_reader)
        logging.debug(f"fieldnames = {fieldnames} | lista_linhas_visu = {lista_linhas_visu}")
        logging.debug(f"lista_linhas_visu = {lista_linhas_visu}")


    new_fieldnames = fieldnames + ["HORARIO_ACAO"] 
    ocorrencias = defaultdict(int) 
    ultima_linha = {}
    resultado = [] 

    for linha in lista_linhas_visu:
        id_acao = linha["ID_ACAO"]
        indice = ocorrencias[id_acao]
        ocorrencias[id_acao] += 1
        if id_acao in historico_dict and indice < len(historico_dict[id_acao]):
            linha["HORARIO_ACAO"] = historico_dict[id_acao][indice]
        else:
            linha["HORARIO_ACAO"] = ""
        resultado.append(linha)
        ultima_linha[id_acao] = linha

    for id_acao, cont in ocorrencias.items():
        horarios = historico_dict.get(id_acao, [])
        if len(horarios) > cont:
            for horario_extra in horarios[cont:]:
                nova_linha = ultima_linha[id_acao].copy()
                nova_linha["HORARIO_ACAO"] = horario_extra
                resultado.append(nova_linha)

    with open("visualizacao.csv", "w", newline="") as visu:
        writer = csv.DictWriter(visu, fieldnames=new_fieldnames)
        writer.writeheader()
        writer.writerows(resultado)




def main() -> None:
    
    list_id_hist = armazenar_id_historico()  
    
    if list_id_hist:  
        ids_str = ", ".join(list_id_hist) 
    else:
        ids_str = "NULL" 

    query_2 = f"""
    SELECT
        t.mmc,
        t.serial_number AS aeronave,
        t.op,
        t.name AS teste,
        o.xml_name AS operação,
        o.name AS nome_operação,
        a.parameter_identifier AS acao,
        a.behavior AS tipo_acao,
        a.status AS result_acao,
        td.value AS valor_esperado,
        td.current_value AS valor_obtido,
        t.test_id AS id_test,
        a.action_id AS id_acao,
        t.user_id AS id_usuario
    FROM its_test t
    INNER JOIN its_operations o ON t.test_id = o.test_id
    INNER JOIN its_actions a ON o.operation_id = a.operation_id
    INNER JOIN its_request r ON a.action_id = r.action_id
    INNER JOIN its_test_data td ON r.request_id = td.request_id
    WHERE a.action_id IN ({ids_str}) 
    """

    retorno_query_2, comandos_banco = conectar_bd(query_2)

    adicionar_query_visu_csv(retorno_query_2, comandos_banco)
    adicionar_horarios_visualizacao()



if __name__ == "__main__":
    logging.basicConfig(
        level=NIVEL_LOG,
        format="%(levelname)s %(asctime)s %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S",
        filename = "script_gerador_visu.log",
    )
    main()