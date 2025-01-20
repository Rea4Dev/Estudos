import customtkinter as ctk

endereco= ""
URL = ""

# Funcionalidade
def armazenamento():
    with open("../../../Script_base/dist/script_base/texto.txt", "w") as file:
        open("../../../Script_base/dist/script_base/texto.txt", "w").write(f'{endereco}\n{URL}')

def aplicar():
    global endereco
    global URL

    endereco = campo_config.get()
    URL = campo_URL.get()
    
    armazenamento()

    app.destroy()
    

# Aparência
ctk.set_appearance_mode('dark')

# Janela principal
app = ctk.CTk()
app.title('Configurador GRASIT')
app.geometry('300x300')

# Campos
label_config = ctk.CTkLabel(app, text='Config.ini')
label_config.pack(pady=10)
campo_config = ctk.CTkEntry(app, placeholder_text='Insira o endereço do Config.ini')
campo_config.pack(pady=1)

label_URL = ctk.CTkLabel(app, text='URL')
label_URL.pack(pady=10)
campo_URL = ctk.CTkEntry(app, placeholder_text='Insira o endereço da URL com o conteúdo')
campo_URL.pack(pady=1)

botao = ctk.CTkButton(app, text='Aplicar e fechar', command=aplicar, hover_color='red')
botao.pack(pady=20)

resultado_aplicar = ctk.CTkLabel(app, text='')
resultado_aplicar.pack(pady=10)

# Iniciar aplicação
app.mainloop()