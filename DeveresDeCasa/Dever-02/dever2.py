def obter_frase():
    """Solicita ao usuário que insira uma frase, garantindo que não esteja vazia."""
    while True:
        frase = input("Digite uma frase: ").strip()
        if frase:
            return frase
        print("Erro: A frase não pode estar vazia. Tente novamente.")

def analisar_frase(frase):
    """Realiza a análise da frase, incluindo contagem de caracteres e palavras, além da identificação da maior palavra."""
    num_caracteres = len(frase)
    palavras = frase.split()
    num_palavras = len(palavras)
    maior_palavra = max(palavras, key=len) if palavras else ""

    return num_caracteres, num_palavras, maior_palavra, palavras

def manipular_frase(frase, palavras):
    """Executa operações de manipulação e formatação da frase."""
    frase_invertida = frase[::-1]
    frase_invertida_palavras = " ".join(palavras[::-1])
    frase_maiuscula = frase.upper()
    frase_minuscula = frase.lower()
    tupla_palavras = tuple(palavras)

    return frase_invertida, frase_invertida_palavras, frase_maiuscula, frase_minuscula, tupla_palavras

def exibir_resultados(num_caracteres, num_palavras, maior_palavra, frase_invertida, frase_invertida_palavras, frase_maiuscula, frase_minuscula, tupla_palavras):
    """Exibe os resultados formatados."""
    print("\n--- Resultados da Análise ---")
    print(f"Número de caracteres: {num_caracteres}")
    print(f"Número de palavras: {num_palavras}")
    print(f"Maior palavra: {maior_palavra}")
    print(f"Frase invertida por caracteres: {frase_invertida}")
    print(f"Frase invertida por palavras: {frase_invertida_palavras}")
    print(f"Frase em maiúsculas: {frase_maiuscula}")
    print(f"Frase em minúsculas: {frase_minuscula}")
    print(f"Tupla de palavras: {tupla_palavras}")

def main():
    frase = obter_frase()

    # Análise da frase
    num_caracteres, num_palavras, maior_palavra, palavras = analisar_frase(frase)

    # Manipulação da frase
    frase_invertida, frase_invertida_palavras, frase_maiuscula, frase_minuscula, tupla_palavras = manipular_frase(frase, palavras)

    # Exibir os resultados
    exibir_resultados(num_caracteres, num_palavras, maior_palavra, frase_invertida, frase_invertida_palavras, frase_maiuscula, frase_minuscula, tupla_palavras)

if __name__ == "__main__":
    main()
