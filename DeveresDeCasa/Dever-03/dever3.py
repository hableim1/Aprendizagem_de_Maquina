import csv

with open("dados.csv", mode="w", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Nome", "Idade"])  # Cabeçalho
    escritor.writerows([
        ["Ana", 25],
        ["Bruno", 30],
        ["Carla", 22],
        ["Daniel", 28],
        ["Eduardo", 35]
    ])

dados = []
with open("dados.csv", mode="r") as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor)
    for linha in leitor:
        nome, idade = linha
        dados.append((nome, int(idade)))


nome_digitado = input("Digite um nome: ").strip()


nomes = [pessoa[0] for pessoa in dados]
idades = [pessoa[1] for pessoa in dados]

if nome_digitado in nomes:
    idade_pessoa = dict(dados)[nome_digitado]
    idade_maxima = max(idades)

    if idade_pessoa == idade_maxima:
        print(
            f"{nome_digitado} tem {idade_pessoa} anos, é a pessoa mais velha da lista.")
    else:
        print(
            f"{nome_digitado} tem {idade_pessoa} anos, não é a pessoa mais velha da lista.")
else:
    print("Nome não encontrado.")
