import csv
import os

lista_dados_bd = [
    (1597, 50839, 50839087, 'INTEGRATED OPERATIONAL TEST - PARKING AREA', '1.0', 'CONDIÇÕES INICIAIS', 'A', 'CONFIG', 'PASSED', '1', None, "datetime.datetime(2025, 3, 12, 12, 50, 7, 670000)", 37179, 32551956, 9994),
    (1597, 50839, 50839087, 'INTEGRATED OPERATIONAL TEST - PARKING AREA', '1.0', 'CONDIÇÕES INICIAIS', 'B', 'CONFIG', 'PASSED', '1', None, "datetime.datetime(2025, 3, 12, 12, 50, 7, 670000)", 37179, 32551959, 9994),
    (1597, 50839, 50839087, 'INTEGRATED OPERATIONAL TEST - PARKING AREA', '1.0', 'CONDIÇÕES INICIAIS', 'C', 'CONFIG', 'PASSED', '1', None, "datetime.datetime(2025, 3, 12, 12, 50, 7, 670000)", 37179, 32551953, 9994),
    (1597, 50839, 50839087, 'INTEGRATED OPERATIONAL TEST - PARKING AREA', '1.0', 'CONDIÇÕES INICIAIS', 'D', 'CONFIG', 'PASSED', '1', None, "datetime.datetime(2025, 3, 12, 12, 50, 7, 670000)", 37179, 32551954, 9994),
    (1597, 50839, 50839087, 'INTEGRATED OPERATIONAL TEST - PARKING AREA', '1.0', 'CONDIÇÕES INICIAIS', 'E', 'CONFIG', 'PASSED', '1', None, "datetime.datetime(2025, 3, 12, 12, 50, 7, 670000)", 37179, 32551955, 9994),
    (1597, 50839, 50839087, 'INTEGRATED OPERATIONAL TEST - PARKING AREA', '1.0', 'CONDIÇÕES INICIAIS', 'F', 'CONFIG', 'PASSED', '1', None, "datetime.datetime(2025, 3, 12, 12, 50, 7, 670000)", 37179, 32551926, 9994),
    (1597, 50839, 50839087, 'INTEGRATED OPERATIONAL TEST - PARKING AREA', '1.0', 'CONDIÇÕES INICIAIS', 'G', 'CONFIG', 'PASSED', '1', None, "datetime.datetime(2025, 3, 12, 12, 50, 7, 670000)", 37179, 32551957, 9994),
    (1597, 50839, 50839087, 'INTEGRATED OPERATIONAL TEST - PARKING AREA', '1.0', 'CONDIÇÕES INICIAIS', 'H', 'CONFIG', 'PASSED', '1', None, "datetime.datetime(2025, 3, 12, 12, 50, 7, 670000)", 37179, 32551958, 9994),
    (1597, 50839, 50839087, 'INTEGRATED OPERATIONAL TEST - PARKING AREA', '1.0', 'CONDIÇÕES INICIAIS', 'I', 'CONFIG', 'PASSED', '1', None, "datetime.datetime(2025, 3, 12, 12, 50, 7, 670000)", 37179, 32551929, 9994),
    (1597, 50839, 50839087, 'INTEGRATED OPERATIONAL TEST - PARKING AREA', '1.0', 'CONDIÇÕES INICIAIS', 'J', 'CONFIG', 'PASSED', '1', None, "datetime.datetime(2025, 3, 12, 12, 50, 7, 670000)", 37179, 32551921, 9994),
    (1597, 50839, 50839087, 'INTEGRATED OPERATIONAL TEST - PARKING AREA', '1.0', 'CONDIÇÕES INICIAIS', 'K', 'CONFIG', 'PASSED', '1', None, "datetime.datetime(2025, 3, 12, 12, 50, 7, 670000)", 37179, 32551922, 9994),
    (1597, 50839, 50839087, 'INTEGRATED OPERATIONAL TEST - PARKING AREA', '1.0', 'CONDIÇÕES INICIAIS', 'L', 'CONFIG', 'PASSED', '1', None, "datetime.datetime(2025, 3, 12, 12, 50, 7, 670000)", 37179, 32551923, 9994),
]

def comparar_lista_com_csv():
    with open('historico.csv', 'r', newline='', encoding='utf-8') as historico:
        lista_historico = list(csv.reader(historico, delimiter=','))
        ids_historico = [linha_historico[13] for linha_historico in lista_historico[1:] if len(linha_historico) > 13]

        for linha in lista_dados_bd:
            id_lista_bd = str(linha[13])  
            
            if id_lista_bd in ids_historico:
                status_lista_bd = linha[8]  # Obtém o status da lista_dados_bd
                status_historico = lista_historico[ids_historico.index(id_lista_bd) + 1][8]  # Obtém o status correspondente no histórico

                if status_lista_bd == status_historico:
                    print(f'ID: {id_lista_bd} encontrado no arquivo historico.csv com status correspondente: {status_lista_bd}')
                else:
                    print(f'ID: {id_lista_bd} encontrado no arquivo historico.csv, mas com status diferente (BD: {status_lista_bd}, Histórico: {status_historico})')
            else:
                print(f'ID: {id_lista_bd} não encontrado no arquivo historico.csv')

def main():
    os.system('cls')
    comparar_lista_com_csv()

if __name__ == "__main__":
    main()