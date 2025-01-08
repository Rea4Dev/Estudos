import requests #Usado para requisições HTTP
import os 

# Caminhos para os arquivos
endereco_arquivo = r"C:\ProgramData\Embraer\SIT\MMC-0761 WLS Clinometer\Config.ini.txt" #"r" antes para ficar como raw string e não tem problemas com o endereço (relativo a barras, sem o raw string teria que ter sempre dois \\ para tirar a especialidade da barra).
endereco_web = "https://raw.githubusercontent.com/Rea4Dev/Estudos/main/Ad-Hocs/urls.properties.txt" 

def ler_arquivo(parametro_arquivo):

    conteudo_lido = {}
    secao_atual = None
    
    #Estrutura condicional relativo à existência do endereço_arquivo fornecido
    if not os.path.exists(parametro_arquivo):
        raise FileNotFoundError(f"Erro detectado: O arquivo não foi encontrado.")
    
    #Estrutura de controle que percorre e lê o arquivo
    with open(parametro_arquivo, 'r') as file:
        for line in file:

            if line.startswith('#') or not line.strip(): # Ignorar comentários e linhas em branco ou só com espaços
                continue  

            if '=' in line:  # Apenas linhas válidas com '='
                key, value = line.strip().split('=', 1)
                conteudo_lido[key] = value

    return conteudo_lido

def mitigar(caminho_arquivo):
    # Verifica se o arquivo existe
    if not os.path.exists(caminho_arquivo):
        raise FileNotFoundError(f"Erro: O arquivo {caminho_arquivo} não foi encontrado.")
    
    # Lê o conteúdo do arquivo, ignorando os 10 primeiros caracteres
    with open(caminho_arquivo, 'r') as file:
        conteudo = file.read()[10:]  # Remove os 10 primeiros caracteres
    
    # Escreve o conteúdo atualizado de volta no arquivo
    with open(caminho_arquivo, 'w') as file:
        file.write(conteudo)

def mudar_url(config_path, new_url):
    # Lê o Config.ini
    conteudo_lido = ler_arquivo(config_path)
    # Substitui a URL antiga pela nova
    if 'PingUrl' in conteudo_lido:
        old_url = conteudo_lido['PingUrl']
        print(f"Substituindo URL antiga: {old_url} pela nova: {new_url}")
    else:
        print("A chave 'PingUrl' não foi encontrada no arquivo. Adicionando nova entrada.")
    conteudo_lido['PingUrl'] = new_url
    # Escreve de volta no arquivo
    with open(config_path, 'w') as file:
        for key, value in conteudo_lido.items():
            file.write(f"{key} = {value}\n")
    print(f"Config.ini atualizado com a nova URL: {new_url}")

def main():
    print("Buscando nova URL no GitHub...")
    # Baixa o conteúdo do arquivo no GitHub
    try:
        response = requests.get(endereco_web, verify=False)  # Adicione verify=False
        response.raise_for_status()  # Lança exceção se houver erro na requisição
        new_url = response.text.strip()  # Remove espaços e quebras de linha
        print(f"Nova URL obtida: {new_url}")
    except requests.RequestException as e:
        print(f"Erro ao buscar a URL no GitHub: {e}")
        return

    # Atualiza o Config.ini com a nova URL
    try:
        mudar_url(endereco_arquivo, new_url)
    except Exception as e:
        print(f"Erro ao atualizar o Config.ini: {e}")
        return

    # Remoção dos 10 primeiros caracteres
    try:
        mitigar(endereco_arquivo)
    except Exception as e:
        print(f"Erro ao mitigar o arquivo: {e}")
        return

if __name__ == "__main__":
    main()