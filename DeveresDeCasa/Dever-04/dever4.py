import os
import pandas as pd
import random

frutas = ["maçã", "banana", "laranja", "uva", "maçã", "melão", "mamão", "banana"]

quantidades = {fruta: random.randint(0, 100) for fruta in frutas}

pasta = "DeveresDeCasa/Dever-04"
caminho_arquivo = os.path.join(pasta, "minhas_frutas.txt")

os.makedirs(pasta, exist_ok=True)

with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
    for fruta, quantidade in quantidades.items():
        arquivo.write(f"{fruta},{quantidade}\n")

try:
    df = pd.read_csv(caminho_arquivo, header=None, names=["Fruta", "Quantidade"], encoding="utf-8", dtype={"Quantidade": int})
    df = df.groupby("Fruta", as_index=False).sum()  
    print(df)
except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")