import requests  # Usado para requisições HTTP

endereco_arquivo = r"C:\ProgramData\Embraer\SIT\MMC-0761 WLS Clinometer\Config.ini.txt"
endereco_web = "https://raw.githubusercontent.com/Rea4Dev/Estudos/main/Ad-Hocs/urls.properties.txt"


# Abre o arquivo em modo de escrita, limpando o conteúdo
def limpar_arquivo():
    with open(endereco_arquivo, 'w') as file:
        pass  


def mudar_url(new_url):
    conteudo_lido = ler_arquivo()
    conteudo_lido['PingUrl'] = new_url
    with open(endereco_arquivo, 'w') as file:
        for key, value in conteudo_lido.items():
            file.write(f"{key} = {value}\n")


def ler_arquivo():
    conteudo_lido = {}    
    with open(endereco_arquivo, 'r') as file:
        for line in file:
            if line.startswith('#') or not line.strip():  # Ignorar comentários e linhas em branco
                continue  
            if '=' in line:  # Apenas linhas válidas com '='
                key, value = line.strip().split('=', 1)
                conteudo_lido[key] = value
    return conteudo_lido


def mitigar(caminho_arquivo):
    with open(caminho_arquivo, 'r') as file:
        conteudo = file.read()[10:]  # Remove os 10 primeiros caracteres
    with open(caminho_arquivo, 'w') as file:
        file.write(conteudo)


def main():
    limpar_arquivo()
    response = requests.get(endereco_web, verify=False)
    new_url = response.text.strip()
    mudar_url(new_url)
    mitigar(endereco_arquivo)


if __name__ == "__main__":
    main()