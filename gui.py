import tkinter
from tkinter import messagebox
from main import gerar_senha, senhas_armazenadas, armazenar_senha, carregar_senha, deletar_senha

# Função para mostrar os widgets de seleção de caracteres e entrada de tamanho
def mostrar_opcoes():
    label_tamanho.grid(row=1, column=0, pady=10)
    entry_tamanho.grid(row=1, column=1, columnspan=2, pady=5)
    label_uso.grid(row=2, column=0, pady=10)
    entry_uso.grid(row=2, column=1, columnspan=2, pady=5)
    label_file_path.grid(row=3, column=0, pady=10)
    entry_file_path.grid(row=3, column=1, columnspan=2, pady=5)
    checkbox_digitos.grid(row=4, column=0, sticky="w", padx=10)
    checkbox_especiais.grid(row=4, column=1, sticky="w", padx=10)
    checkbox_maiusculas.grid(row=5, column=0, sticky="w", padx=10)
    checkbox_minusculas.grid(row=5, column=1, sticky="w", padx=10)

# Função para gerar a senha e mostrar as opções
def button_gerar_senha():
    if not entry_tamanho.winfo_ismapped() or not entry_file_path.winfo_ismapped():
        mostrar_opcoes()
    else:
        # Se as opções já estão visíveis, gera a senha
        try:
            tamanho_senha = int(entry_tamanho.get())
            uso_senha = entry_uso.get()
            file_path = entry_file_path.get()
            incluir_digitos = var_digitos.get()
            incluir_caracteres_especiais = var_caracteres_especiais.get()
            incluir_maiusculas = var_maiusculas.get()
            incluir_minusculas = var_minusculas.get()

            # Obtém o caminho do arquivo da entrada de texto


            senha = gerar_senha(tamanho_senha, uso_senha, incluir_digitos, incluir_caracteres_especiais, incluir_maiusculas, incluir_minusculas, file_path)
            if senha:
                armazenar_senha(uso_senha, senha) # Armazena a senha gerada em uma lista
                messagebox.showinfo("Senha gerada!", f"A senha gerada é: {senha}")
            elif 16 < tamanho_senha < 8:
                messagebox.showwarning("Aviso", "A senha deve conter entre 8 a 16 caracteres.")
            else:
                messagebox.showwarning("Aviso", "Nenhum caractere selecionado. A senha não pôde ser gerada.")
        except ValueError:
            messagebox.showerror("Erro", "Por favor insira um número válido para o tamanho da senha.")
        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo não encontrado.")
        except PermissionError:
            messagebox.showerror("Erro", "Você não tem permissão para acessar este arquivo.")

# Função para listar senhas armazenadas
def button_suas_senhas():
    listbox_senhas.delete(0, tkinter.END)  # Limpa a Listbox antes de atualizar
    file_path = entry_file_path.get()
    if not file_path:
        messagebox.showerror("Erro", "Por favor, forneça o caminho do arquivo.")
        return
    senhas_armazenadas.clear()  # Limpa a lista de senhas
    carregar_senha(file_path)
    if senhas_armazenadas:  # Verifica se há senhas armazenadas
        for senha in senhas_armazenadas:
            if senha not in listbox_senhas.get(0, tkinter.END):
                listbox_senhas.insert(tkinter.END, senha)  # Insere as senhas na Listbox

        # Torna a Listbox visível, caso esteja oculta
        listbox_senhas.grid(row=9, column=0, columnspan=2, padx=10, pady=10)
    else:
        messagebox.showinfo("Aviso", "Você não possui senhas salvas.")

def button_deletar_senha():
    try:
        selecionado = listbox_senhas.curselection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Nenhuma senha selecionada")
            return

        senha_selecionada = listbox_senhas.get(selecionado)
        listbox_senhas.delete(selecionado)
        senhas_armazenadas.remove(senha_selecionada)

        file_path = entry_file_path.get()
        deletar_senha(file_path)
        listbox_senhas.config(width=0, height=0)
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

def encerrar_programa():
    window.destroy()

# Configuração da GUI
window = tkinter.Tk()
window.title("Gerenciador de Senhas")
window.geometry('410x470')
window.configure(bg='#040926')

# Criação dos widgets que serão inicialmente escondidos
label_tamanho = tkinter.Label(window, text="Tamanho da senha:", bg='#040926', fg='#F7F7F2')
entry_tamanho = tkinter.Entry(window)
label_uso = tkinter.Label(window, text="Uso da senha:", bg='#040926', fg='#F7F7F2')
entry_uso = tkinter.Entry(window)
label_file_path = tkinter.Label(window, text="Local do Arquivo:", bg='#040926', fg='#F7F7F2')
entry_file_path = tkinter.Entry(window)

var_digitos = tkinter.BooleanVar()
var_caracteres_especiais = tkinter.BooleanVar()
var_maiusculas = tkinter.BooleanVar()
var_minusculas = tkinter.BooleanVar()

checkbox_digitos = tkinter.Checkbutton(window, text="Incluir dígitos (0-9)?", variable=var_digitos, bg='#040926', fg='#F7F7F2', selectcolor='#C97B84')
checkbox_especiais = tkinter.Checkbutton(window, text="Incluir caracteres especiais (#$%*)?", variable=var_caracteres_especiais, bg='#040926', fg='#F7F7F2', selectcolor='#C97B84')
checkbox_maiusculas = tkinter.Checkbutton(window, text="Incluir letras maiúsculas?", variable=var_maiusculas, bg='#040926', fg='#F7F7F2', selectcolor='#C97B84')
checkbox_minusculas = tkinter.Checkbutton(window, text="Incluir letras minúsculas?", variable=var_minusculas, bg='#040926', fg='#F7F7F2', selectcolor='#C97B84')

# Esconder inicialmente as opções de tamanho e caracteres
label_tamanho.grid_forget()
entry_tamanho.grid_forget()
label_file_path.grid_forget()
entry_file_path.grid_forget()
label_uso.grid_forget()
entry_uso.grid_forget()
checkbox_digitos.grid_forget()
checkbox_especiais.grid_forget()
checkbox_maiusculas.grid_forget()
checkbox_minusculas.grid_forget()

# Botões
gerar_button = tkinter.Button(window, text="Gerar Senhas", bg='#C97B84', fg='#F7F7F2',
                                    activebackground='#9F414C', activeforeground='#F7F7F2', font=("Roboto", 16), command=button_gerar_senha)
gerar_button.grid(row=0, column=0, padx=10, pady=10)

suas_senhas_button = tkinter.Button(window, text="Suas Senhas", bg='#C97B84', fg='#F7F7F2',
                                    activebackground='#9F414C', activeforeground='#F7F7F2', font=("Roboto", 16), command=button_suas_senhas)
suas_senhas_button.grid(row=0, column=1, padx=10, pady=10)

deletar_button = tkinter.Button(window, text="Deletar Senhas", bg='#C97B84', fg='#F7F7F2',
                                activebackground='#9F414C', activeforeground='#F7F7F2', font=("Roboto", 16), command=button_deletar_senha)
deletar_button.grid(row=8, column=0, padx=10, pady=10)

encerrar_button = tkinter.Button(window, text="Fechar programa", bg='#C97B84', fg='#F7F7F2',
                                 activebackground='#9F414C', activeforeground='#F7F7F2', font=("Roboto", 16), command=encerrar_programa)
encerrar_button.grid(row=8, column=1, padx=10, pady=10)

# Criação da Listbox para armazenar as senhas
listbox_senhas = tkinter.Listbox(window, bg='#F7F7F2', fg='#4A4E69', font=("Roboto", 12), width=50, height=10)
listbox_senhas.config(width=0,height=0)

# Executa o loop principal da GUI
window.mainloop()
