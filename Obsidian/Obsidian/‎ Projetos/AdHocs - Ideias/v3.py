import customtkinter as ctk
import v4
import json  # Para salvar as variáveis em um arquivo
import subprocess

# Aparência
ctk.set_appearance_mode('dark')

# Caminho para o arquivo de configuração
config_file = "config.json"

def aplicar():
    config_endereco = campo_config.get()  # Obter endereço do config.ini
    URL_endereco = campo_URL.get()  # Obter URL

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