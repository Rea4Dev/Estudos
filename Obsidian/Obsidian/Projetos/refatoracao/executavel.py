import requests
from winotify import Notification
import ftplib
import os
from sys import exit

def verificar_operacao():
    print("\n\033[1;30m Verificando modo de operação...\033[0;37m")

    try:
        if (os.path.getsize("./grasit_config.ini") == 0):
            print("\033[0;30m Há algo em grasit.ini? | Não :\033[0;33m Iniciando protocolo de Configuração. \033[0;37m\n")
            ha_conteudo_grasit = True
        else:
            print("\033[0;30m Há algo em grasit.ini? | Sim :\033[0;33m Iniciando protocolo de Operação. \033[0;37m\n")
            ha_conteudo_grasit = False

    except FileNotFoundError as falha:
        print("\n\033[1;31m ERRO: grasit.ini inexistente.\033[0;37m")
        print("\033[1;31m Programa finalizado.\033[0;37m\n")
        exit()

    else:
        return ha_conteudo_grasit

def main():
    ha_conteudo_grasit = verificar_operacao()

if __name__ == "__main__":
    main()