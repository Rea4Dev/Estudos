import requests
import configurador
import customtkinter as ctk

MMC = r"C:\Users\RENGCARV.ADPRDEMB\OneDrive^ -^ Embraer\Desktop\MMC-0761^ WLS^ Clinometer.lnk"

#Pega só o texto da URL
conteudo_atualizado = requests.get(configurador.URL, verify=False).text

# Limpar o que tinha no .txt
def limpar_arquivo():
    with open(configurador.endereco, 'w') as file:
        pass

# Atualizar o arquivo com o novo conteúdo
def mudar_arquivo(conteudo_atualizado):
    with open(configurador.endereco, 'w') as file:
        file.write(f"{conteudo_atualizado}\n")

# Executar as etapas principais
limpar_arquivo()
mudar_arquivo(conteudo_atualizado)