import customtkinter as ctk

endereco= ""
URL = ""

# Funcionalidade
def aplicar():
    global endereco
    global URL

    endereco = campo_config.get()
    URL = campo_URL.get()

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

# Acredito não ser mais necessário o MMC, haja vista que não irá funcionar mais como um app safadão.
# label_MMC = ctk.CTkLabel(app, text='MMC')
# label_MMC.pack(pady=1)
# campo_MMC = ctk.CTkEntry(app, placeholder_text='Insira o endereço do MMC com o conteúdo')
# campo_MMC.pack(pady=10)

botao = ctk.CTkButton(app, text='Aplicar e fechar', command=aplicar, hover_color='red')
botao.pack(pady=20)

resultado_aplicar = ctk.CTkLabel(app, text='')
resultado_aplicar.pack(pady=10)

# Iniciar aplicação
app.mainloop()