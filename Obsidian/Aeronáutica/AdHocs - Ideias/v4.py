import requests 
import json  

config_endereco_final = "default_config.txt"
URL_endereco_final = "https://default-url.com"

def gerar_executavel():
    import subprocess
    subprocess.run(["pyinstaller", "-w", "v4.py"])


def carregar_configuracoes():
    with open("config.json", 'r') as file: #Mova o executavel
        config = json.load(file)
        global config_endereco_final, URL_endereco_final
        config_endereco_final = config.get("config_endereco", config_endereco_final)
        URL_endereco_final = config.get("URL_endereco", URL_endereco_final)


def codigo_principal():
    carregar_configuracoes()

    conteudo_atualizado = requests.get(URL_endereco_final, verify=False).text

    # Caminho do arquivo MMC
    MMC = r"C:\Users\RENGCARV.ADPRDEMB\OneDrive^ -^ Embraer\Desktop\MMC-0761^ WLS^ Clinometer.lnk"

    # Limpar o arquivo
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

    # Abrir o MMC (descomentar se necessário)
    # subprocess.Popen(MMC, shell=True)

codigo_principal()