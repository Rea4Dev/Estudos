import requests
from winotify import Notification
import ftplib
from os import getcwd
from sys import exit

armazenagem_intermediaria = []
url_ftp = ""
absoluto_config_ini = ""
conteudo_atualizado = ""

def conectar_ftp():
    try:
        ftp = ftplib.FTP()
        ftp.connect("sjkap577.sjk.emb", 9021)
        ftp.login("sit-ftp-grasit", "g5>E8!cYp(>K&dPv")
        ftp.dir("GRASIT_Configs/")
        ftp.cwd("GRASIT_Configs/")
        ftp.quit()

    except ftplib.error_perm as falha_conexao:
        print("\n\033[1;31mFalha ao conectar no banco FTP\033[0;37m.")
        print("Verifique as informações de login.\n")
        exit()

    else:
        print("\n\033[1;32mBanco FTP conectado com sucesso.\033[0;37m\n")
        
def descobrir_path():
    path = getcwd()
    simulacao = None

    if ('dist' not in path):
        print("\033[0;33m    - Execução de simulação/teste detectada (fora da pasta dist).\033[0;37m\n")
        simulacao = True

    else:
        print("\033[0;31m    - Execução de executável detectada (dentro da pasta dist).\033[0;37m\n\n")
        simulacao = False

    return simulacao

def armazenar_config_ini(simulacao):
    intermediario = []

    if simulacao == True:
        with open("grasit_config.ini", "r") as config:
            for linha in config:
                intermediario.append(linha.replace("\n", " ").strip())
        print()
        print(intermediario)
        
def main():
    conectar_ftp()
    simulacao = descobrir_path()
    armazenar_config_ini(simulacao)

if __name__ == "__main__":
    main()