import csv
import locale
from datetime import datetime
import pytz

# Configurar locale (evitar erro se não for suportado)
try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except locale.Error:
    print("Locale não suportado. Prosseguindo sem alterar...")

# Define o fuso horário para o Brasil (Brasília)
con_fuso_horario = pytz.timezone("America/Sao_Paulo")

# Função para formatar datas para o padrão brasileiro
def formatar_data(data):
    if "/" in data:  # Verifica se já está no formato correto
        mes, dia, ano = data.split("/")
        return f"{dia}/{mes}/{ano}"
    return data  # Se já estiver certo, retorna como está

# Criar arquivo CSV
dados = [
    ["Nome", "Data de Nascimento", "Dia do Cadastro", "Hora do Cadastro"],
    ["Pablo Coelho", "01/26/1974", "17/02/2025", "20:30"],
    ["Mariana Ferreira", "26/04/1995", "17/02/2025", "20:31"],
    ["Yuri Alberto", "18/03/2001", "18/02/2025", "07:35"],
    ["Rodrigo Garro", "04/01/1998", "18/02/2025", "07:44"],
    ["Ángel Romero", "04/07/1992", "18/02/2025", "11:00"]
]

# Escrever no arquivo CSV
with open("dados.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(dados)

print("Arquivo CSV criado com sucesso!")

# Ler o CSV e imprimir o registro escolhido pelo usuário
with open("dados.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    lista_dados = list(leitor)  # Converter para lista

# Pedir ao usuário qual registro deseja ver
indice = int(input("Digite o número do registro (1 a 5): "))

# Verificar se está dentro do limite
if 1 <= indice <= 5:
    nome, data_nasc, data_cadastro, hora = lista_dados[indice]
    print(f"Registro {indice}: Nome: {nome}; Data de nascimento: {formatar_data(data_nasc)}; "
          f"Data de cadastro: {formatar_data(data_cadastro)} às {hora} horas.")
else:
    print("Número inválido! Escolha entre 1 e 5.")