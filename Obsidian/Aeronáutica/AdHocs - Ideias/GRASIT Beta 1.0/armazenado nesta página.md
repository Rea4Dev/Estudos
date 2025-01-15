Eis abaixo a última versão desenvolvida do Beta GRASIT 1.0.

>C:\Users\RENGCARV.ADPRDEMB\OneDrive - Embraer\Documents\GitHub\Estudos\Obsidian\Aeronáutica\AdHocs - Ideias
## v3.py
```python
import customtkinter as ctk
import v4
import json  # Para salvar as variáveis em um arquivo
import subprocess
  
# Aparência
ctk.set_appearance_mode('dark')

# Caminho para o arquivo de configuração
config_file = "config.json"

def aplicar():
    config_endereco = campo_config.get()  # Obter endereço do config.ini
    URL_endereco = campo_URL.get()  # Obter URL

  
    # Salvar as configurações em um arquivo JSON
    with open(config_file, 'w') as file:
        json.dump({"config_endereco": config_endereco, "URL_endereco": URL_endereco}, file)

    # Gerar o executável
    v4.gerar_executavel()
    resultado_aplicar.configure(text='Geração de executável feita com sucesso!', text_color='green')

# Janela principal
app = ctk.CTk()
app.title('Configurador GRASIT')
app.geometry('300x300')

# Campos
label_config = ctk.CTkLabel(app, text='Config.ini')
label_config.pack(pady=1)

campo_config = ctk.CTkEntry(app, placeholder_text='Insira o endereço do Config.ini')
campo_config.pack(pady=10)

label_URL = ctk.CTkLabel(app, text='URL')
label_URL.pack(pady=1)

campo_URL = ctk.CTkEntry(app, placeholder_text='Insira o endereço da URL com o conteúdo')
campo_URL.pack(pady=10)

botao = ctk.CTkButton(app, text='Aplicar', command=aplicar)
botao.pack(pady=10)

resultado_aplicar = ctk.CTkLabel(app, text='')
resultado_aplicar.pack(pady=10)

# Iniciar aplicação
app.mainloop()
```

## v4.py
```python
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
    subprocess.Popen(MMC, shell=True)

codigo_principal()
```

---

Eis a última versão estável do Beta GRASIT 1.0
## app.py
```python
import customtkinter as ctk

from v2 import gerar_executavel
  
# Aparência
ctk.set_appearance_mode('dark')

# Funcionalidades
def aplicar():
    config_endereco = campo_config.get() # Informações passadas
    URL_endereco = campo_URL.get() # Informações passadas
    gerar_executavel(config_endereco, URL_endereco)

    resultado_aplicar.configure(text='Geração de executável feita com sucesso!', text_color='green')

# Janela principal
app=ctk.CTk()
app.title('Configurador GRASIT')
app.geometry('300x300')

# Campos
label_config = ctk.CTkLabel(app, text='Config.ini')
label_config.pack(pady=1)

campo_config = ctk.CTkEntry(app, placeholder_text='Insira o endereço do Config.ini')
campo_config.pack(pady=10)

label_URL = ctk.CTkLabel(app, text='URL')
label_URL.pack(pady=1)

campo_URL = ctk.CTkEntry(app, placeholder_text='Insira o endereço da URL com o conteúdo')
campo_URL.pack(pady=10)

botao = ctk.CTkButton(app, text='Aplicar', command = aplicar)
botao.pack(pady=10)

resultado_aplicar = ctk.CTkLabel(app, text='')
resultado_aplicar.pack(pady=10)

# Iniciar aplicação
app.mainloop()
```

## v2.py
```python
import requests  # Usado para requisições HTTP
import subprocess #Abre arquivo sem mostrar CMD

config_endereco_final = "C:\ProgramData\Embraer\SIT\MMC-0761 WLS Clinometer\Teste2.txt"
URL_endereco_final = "https://raw.githubusercontent.com/Rea4Dev/Estudos/main/Ad-Hocs/urls.properties.txt"

def gerar_executavel(config_endereco, URL_endereco):

    global config_endereco_final
    config_endereco_final = config_endereco

    global URL_endereco_final
    URL_endereco_final = URL_endereco

    subprocess.run(["pyinstaller", "-w", "v2.py"])

def codigo_principal():
    conteudo_atualizado = requests.get(URL_endereco_final, verify=False).text
    MMC = r"C:\Users\RENGCARV.ADPRDEMB\OneDrive^ -^ Embraer\Desktop\MMC-0761^ WLS^ Clinometer.lnk" #Uso de ^ antes dos espaços quando houverem.

    # 2°
    def limpar_arquivo():
        with open(config_endereco_final, 'w') as file:
            pass  

    # 3°
    def mudar_arquivo(conteudo_atualizado):
        with open(config_endereco_final, 'w') as file:
            file.write(f"{conteudo_atualizado}\n")

    # 1° Parte main, executado primeiro
    limpar_arquivo()
    mudar_arquivo(conteudo_atualizado)

    #4° Abre o MMC
    subprocess.Popen(MMC, shell=True)

if __name__ == "__main__":
    codigo_principal()
```