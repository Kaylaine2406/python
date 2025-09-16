def validaLogin(nome, senha):
    if (nome == "Kay" and senha =="senha123"):
        return print("Seja bem vindo",nome, senha)
    else:
        return print("Senha ou Login inválidos")
print("=== Digite seu nome ===")
nome = input()
print("=== Digite sua Senha")
senha = input()

validaLogin(nome, senha)