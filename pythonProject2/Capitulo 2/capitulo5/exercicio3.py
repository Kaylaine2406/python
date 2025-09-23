def apresentacao(nome, nomeMae, nomePai):
    print(f"Nome: {nome}")
    print(f"Nome da mãe: {nomeMae}")
    print(f"Nome do pai: {nomePai}")

nome = str(input("digite seu nome completo"))
nomeMae = str(input("digite o nome da mãe"))
nomePai = str(input("digite o nome do pai"))

print(f"{nome},{nomeMae},{nomePai}")

apresentacao(nome, nomeMae, nomePai)