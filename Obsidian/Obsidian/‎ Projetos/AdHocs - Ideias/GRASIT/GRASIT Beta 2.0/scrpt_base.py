import requests
import subprocess

config_endereco_final = "C:\ProgramData\Embraer\SIT\MMC-0761 WLS Clinometer\Teste.txt"
URL_endereco_final = "https://raw.githubusercontent.com/Rea4Dev/Estudos/refs/heads/main/Obsidian/Obsidian/%E2%80%8E%20Projetos/AdHocs%20-%20Ideias/GRASIT/hospedado.txt"
MMC = r"C:\Users\RENGCARV.ADPRDEMB\OneDrive^ -^ Embraer\Desktop\MMC-0761^ WLS^ Clinometer.lnk"

#Pega só o texto da URL
conteudo_atualizado = requests.get(URL_endereco_final, verify=False).text

# Limpar o que tinha no .txt
def limpar_arquivo():
    with open(config_endereco_final, 'w') as file:
        pass

# Atualizar o arquivo com o novo conteúdo
def mudar_arquivo(conteudo_atualizado):
    with open(config_endereco_final, 'w') as file:
        file.write(f"{conteudo_atualizado}\n")

# Executar as etapas principais
limpar_arquivo()
mudar_arquivo(conteudo_atualizado)

# Abrir o MMC
subprocess.Popen(MMC, shell=True)