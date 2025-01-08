import requests  # Usado para requisições HTTP

# Caminhos para o arquivo local e o endereço remoto
ENDERECO_ARQUIVO = r"C:\ProgramData\Embraer\SIT\MMC-0761 WLS Clinometer\Config.ini.txt"
ENDERECO_WEB = "https://raw.githubusercontent.com/Rea4Dev/Estudos/main/Ad-Hocs/urls.properties.txt"

def limpar_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'w') as file:
        pass  # Apenas abre o arquivo em modo de escrita, limpando o conteúdo

def ler_arquivo_preservando_secoes(caminho_arquivo):
    with open(caminho_arquivo, 'r') as file:
        return file.readlines()  # Retorna todas as linhas do arquivo

def atualizar_url_no_arquivo(caminho_arquivo, nova_url):
    linhas = ler_arquivo_preservando_secoes(caminho_arquivo)
    novas_linhas = []

    for linha in linhas:
        if linha.strip().startswith("PingUrl"):  # Localiza a linha da chave 'PingUrl'
            chave, _ = linha.split("=", 1)
            novas_linhas.append(f"{chave.strip()} = \"{nova_url}\"\n")  # Atualiza o valor
        else:
            novas_linhas.append(linha)  # Mantém as outras linhas intactas

    with open(caminho_arquivo, 'w') as file:
        file.writelines(novas_linhas)  # Sobrescreve o arquivo com as novas linhas

def remover_caracteres_iniciais(caminho_arquivo, num_caracteres):
    with open(caminho_arquivo, 'r') as file:
        conteudo = file.read()[num_caracteres:]  # Lê o conteúdo excluindo os caracteres iniciais
    with open(caminho_arquivo, 'w') as file:
        file.write(conteudo)  # Escreve o conteúdo atualizado

def main():
    # Limpa o arquivo antes de qualquer operação
    limpar_arquivo(ENDERECO_ARQUIVO)

    # Obtém a nova URL do repositório remoto
    print("Buscando nova URL...")
    response = requests.get(ENDERECO_WEB, verify=False)
    response.raise_for_status()  # Lança erro caso a requisição falhe
    nova_url = response.text.strip()  # Remove espaços e quebras de linha
    print(f"Nova URL obtida: {nova_url}")

    # Atualiza o arquivo com a nova URL
    atualizar_url_no_arquivo(ENDERECO_ARQUIVO, nova_url)

    # Remove os 10 primeiros caracteres do arquivo
    remover_caracteres_iniciais(ENDERECO_ARQUIVO, 10)
    print("Arquivo atualizado com sucesso!")

if __name__ == "__main__":
    main()