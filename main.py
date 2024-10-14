import secrets
import string

# Armazena as senhas em uma lista
senhas_armazenadas = []

# Especifica os tipos de caracteres que serão usados para gerar as senhas
def gerar_senha(tamanho_senha, uso_senha, incluir_digitos, incluir_especiais, incluir_maiusculas, incluir_minusculas, file_path):
    caracteres = []

    if incluir_digitos:
        caracteres.append(string.digits)
    if incluir_especiais:
        caracteres.append(string.punctuation)
    if incluir_maiusculas:
        caracteres.append(string.ascii_uppercase)
    if incluir_minusculas:
        caracteres.append(string.ascii_lowercase)

    if not caracteres:
        return None  # Retorna None se nenhum caractere foi selecionado

    caracteres = ''.join(caracteres)
    senha = ""
    while len(senha) < tamanho_senha:
        senha += secrets.choice(caracteres)

    senhagen_txt = f"{uso_senha}: {senha}"
    with open(file_path, "a") as file:
        if file.tell() != 0: # Verifica se o arquivo está vazio
            file.write("\n")
        file.write(senhagen_txt)

    return senha

# Armazenar a senha
def armazenar_senha(uso_senha, senha):
    senhas_armazenadas.append(f"{uso_senha}: {senha}")

# Carrega as senhas
#def salvar_senha(uso_senha, senha, file_path):
#    senhagen_txt = f"{uso_senha}: {senha}"
#    with open(file_path, "a") as file:
#        if file.tell() != 0: # Verifica se o arquivo está vazio
#            file.write("\n")
#        file.write({senhagen_txt})

def carregar_senha(file_path):
    try:
        with open(file_path, "r") as file:
            for line in file:
                senhas_armazenadas.append(line.lstrip())
    except FileNotFoundError:
        pass

def deletar_senha(file_path):
    with open(file_path, "w") as file:
        for senha in senhas_armazenadas:
            file.write(senha)