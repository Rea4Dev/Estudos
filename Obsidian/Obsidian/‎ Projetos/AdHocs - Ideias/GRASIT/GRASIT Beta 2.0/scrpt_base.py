import requests

config_endereco = "C:\ProgramData\Embraer\SIT\MMC-0761 WLS Clinometer\Teste.txt"
URL_endereco = "https://raw.githubusercontent.com/Rea4Dev/Estudos/refs/heads/main/Obsidian/Obsidian/%E2%80%8E%20Projetos/AdHocs%20-%20Ideias/GRASIT/GRASIT%20Beta%202.0/config.txt"
MMC = r"C:\Users\RENGCARV.ADPRDEMB\OneDrive^ -^ Embraer\Desktop\MMC-0761^ WLS^ Clinometer.lnk"

#Pega só o texto da URL
conteudo_atualizado = requests.get(URL_endereco, verify=False).text

# Limpar o que tinha no .txt
def limpar_arquivo():
    with open(config_endereco, 'w') as file:
        pass

# Atualizar o arquivo com o novo conteúdo
def mudar_arquivo(conteudo_atualizado):
    with open(config_endereco, 'w') as file:
        file.write(f"{conteudo_atualizado}\n")

# Executar as etapas principais
limpar_arquivo()
mudar_arquivo(conteudo_atualizado)