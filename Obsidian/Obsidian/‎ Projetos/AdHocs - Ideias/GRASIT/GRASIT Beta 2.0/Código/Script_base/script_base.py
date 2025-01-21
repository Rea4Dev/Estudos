import requests
from winotify import Notification

# Variaveis Globais
lista = []
URL = "https://git.embraer.com.br/projects/ITS-MUL/repos/app-0167_grasi/raw/hospedado.txt?at=refs%2Fheads%2Fmaster"
endereco = ""
conteudo_atualizado = ""

# Lê o log do configurador e define os conteudos
def ler_log():
    with open("script_base/texto.txt", "r") as file: # Problemático
        for line in file:
            lista.append(line)

    global URL
    global endereco
    global conteudo_atualizado

    endereco = lista[0].replace("\n", " ").strip()
    URL = lista[1]

    conteudo_atualizado = requests.get(URL, verify=False).text

# Atualizar o arquivo com o novo conteúdo e deleta antigo
def mudar_arquivo(conteudo_atualizado):
    with open(endereco, 'w') as file:
        file.write(f"{conteudo_atualizado}\n")
    Notification(app_id="Aplicação SIT", title="Aplicação SIT atualizada com sucesso!").show()

# Executar as etapas principais
ler_log()
mudar_arquivo(conteudo_atualizado)