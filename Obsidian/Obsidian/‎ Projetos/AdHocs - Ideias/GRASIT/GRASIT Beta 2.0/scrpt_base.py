import requests 
import json  

config_endereco_final = "C:\ProgramData\Embraer\SIT\MMC-0761 WLS Clinometer\Teste.txt"
URL_endereco_final = ""
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
# subprocess.Popen(MMC, shell=True)