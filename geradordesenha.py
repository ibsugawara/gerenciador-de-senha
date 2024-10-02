import secrets
import string

# Armazena as senhas em uma lista
senhas_armazenadas = []

# Especifica os tipos de caracteres que serão usados para gerar as senhas
def gerar_senha(tamanho_senha):
    caracteres = []

    while True:
        numeros = input("Defina se a senha conterá dígitos de 0 a 9 (S/N): ").upper()
        if numeros == 'S':
            caracteres.append(string.digits)
            break
        elif numeros == 'N':
            break
        else:
            print("Resposta inválida. Insira entre (S/N): ")
            continue

    while True:
        charespecial = input("Defina se a senha conterá caracteres especiais (!@#$%...) (S/N): ").upper()
        if charespecial == 'S':
            caracteres.append(string.punctuation)
            break
        elif charespecial == 'N':
            break
        else:
            print("Resposta inválida. Insira entre (S/N): ")
            continue

    while True:
        uppercase = input("Defina se a senha conterá letras maiúsculas (S/N): ").upper()
        if uppercase == 'S':
            caracteres.append(string.ascii_uppercase)
            break
        elif uppercase == 'N':
            break
        else:
            print("Resposta inválida. Insira entre (S/N): ")
            continue

    while True:
        lowercase = input("Defina se a senha conterá letras minúsculas (S/N): ").upper()
        if lowercase == 'S':
            caracteres.append(string.ascii_lowercase)
            break
        elif lowercase =='N':
            break
        else:
            print("Resposta inválida. Insira entre (S/N): ")
            continue

    if not caracteres:
        while True:
            tentar_novamente = input("Nenhum caractere selecionado. A senha não pôde ser gerada. Deseja tentar novamente (S/N)?").upper()
            if tentar_novamente == 'S':
                return gerar_senha(tamanho_senha)
            elif tentar_novamente == 'N':
                print("Problema seu! Tente novamente..")
                return None
            else:
                print("Resposta inválida. Insira entre (S/N): ")
                continue

    caracteres = ''.join(caracteres)
    senha = ""
    while len(senha) < tamanho_senha:
        senha += secrets.choice(caracteres)
    return senha

#Armazena senhas em um arquivo de texto
def armazenar_senhas(senha, uso, file_path):
    if senha is None:
        print("Insira pelo menos um caractere e tente novamente.")
    else:
        print(f"Senha gerada para {uso}: {senha}")

    senhagen_txt = f"{uso}: {senha}"

    try:
        with open(file_path, "a") as file:
            file.write("\n" + senhagen_txt)
            print(f"Senhas geradas encontradas em: {file_path}")
    except FileNotFoundError:
        print("O caminho especificado não foi encontrado.")
    except PermissionError:
        print("Você não tem permissão para acessar este arquivo.")

# Oferece a opção de deletar uma senha
def deletar_senha(file_path):
    uso_deletar = input("Digite o uso da senha a ser deletada: ").capitalize()

# Abre o arquivo no modo leitura e lê todas as senhas
    with open(file_path, 'r') as file:
        lista_senhas = file.readlines()

    novo_senhas = []
    i = 0
    while i < len (lista_senhas):
        if uso_deletar not in lista_senhas[i]: # Verifica se a senha a ser deletada está na linha atual da lista
            novo_senhas.append(lista_senhas[i]) # Mantém senhas que não correspondem
        i+=1

# Verifica se a senha foi encontrada e se foi removida
    if len(novo_senhas) < len (lista_senhas):
        print("Senha removida!")
    else:
        print("Senha não encontrada!")

# Reescreve o arquivo, deletando a senha
    with open(file_path, 'w') as file:
        file.writelines(novo_senhas)

def main():
    file_path = ""
    while True:
        print("-- Menu --")
        print("1. Gerar senha")
        print("2. Deletar senha")
        print("3. Encerrar programa")

        escolha = input("Insira a opção desejada: ")

        if escolha == '1':
            # Solicita o uso, o comprimento e o local para armazenar a senha
            uso = input("Insira o website/app em que a senha será utilizada: ").capitalize()

            while True:
                try:
                    comprimento = int(input("Defina o comprimento da senha a ser gerada (8 a 20): "))
                    if 8 <= comprimento <= 20:
                        break
                    else:
                        print("O comprimento deve ser entre 8 e 20.")
                except ValueError:
                    print("Valor inválido! Insira um valor numérico.")

            file_path = input("Insira o caminho do arquivo de texto para armazenar suas senhas: ")

            # Gera a senha
            senha = gerar_senha(comprimento)

            if senha is not None:
                # Armazena a senha gerada
                armazenar_senhas(senha, uso, file_path)

        elif escolha == '2':
            if not file_path:
                file_path = input("Insira o caminho do arquivo de texto onde as senhas estão armazenadas: ")

            while True:
                deletar =  input("Deseja deletar uma senha (S/N)?").upper()
                if deletar == 'S':
                    deletar_senha(file_path)
                elif deletar == 'N':
                    return main()
                else:
                    print("Resposta inválida! Insira entre (S/N)")

        elif escolha == '3':
            print("Programa encerrado!")
            break
        else:
            print("Escolha inválida! Tente novamente.")
main()