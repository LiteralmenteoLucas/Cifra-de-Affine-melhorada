# Importando o dicionário criado
from dicionario_pt_fr import dicionario_pt_fr  # Seu dicionário de traduções

# Função para calcular o MDC de dois números usando o Algoritmo de Euclides
def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Função para aplicar a cifra de Affine
def cifra_affine(texto, a, b, modo='criptografar'):
    resultado = ""
    for letra in texto:
        if letra.isalpha():  # Se for uma letra
            # Converte a letra para seu valor numérico
            valor = ord(letra.lower()) - ord('a')  # A = 0, B = 1, ..., Z = 25

            if modo == 'criptografar':
                # Criptografa com a fórmula (a * x + b) % 26
                valor_cripto = (a * valor + b) % 26
            elif modo == 'descriptografar':
                # Descriptografa com a fórmula a^-1 * (x - b) % 26
                # Primeiro, precisamos calcular o inverso de a modulo 26
                a_inv = pow(a, -1, 26)
                valor_desc = (a_inv * (valor - b)) % 26
                valor_cripto = valor_desc

            # Converte o valor numérico de volta para a letra
            resultado += chr(valor_cripto + ord('a'))
        else:
            # Se não for letra (como espaço, pontuação), adiciona como está
            resultado += letra

    return resultado

# Função de criptografia
def criptografar(texto, dicionario, a, b):
    palavras = texto.split()  # Divide o texto em palavras
    texto_cripto = []

    # Exibe as palavras traduzidas
    print("Texto Original e Traduzido:")

    for palavra in palavras:
        if palavra in dicionario:
            texto_cripto.append(dicionario[palavra])  # Substitui com a tradução do dicionário
            print(f"Palavra original: {palavra} -> Traduzida: {dicionario[palavra]}")
        else:
            texto_cripto.append(palavra)  # Deixa a palavra sem tradução, se não estiver no dicionário
            print(f"Palavra sem tradução: {palavra}")

    # Junta o texto e aplica a cifra de Affine no texto traduzido
    texto_cripto = ' '.join(texto_cripto)
    texto_cripto = cifra_affine(texto_cripto, a, b, modo='criptografar')  # Criptografa
    return texto_cripto


# Função de descriptografia
def descriptografar(texto, dicionario, a, b):
    # Aplica a cifra de Affine no texto cifrado
    texto_descifrado = cifra_affine(texto, a, b, modo='descriptografar')  # Descriptografa

    palavras = texto_descifrado.split()  # Divide o texto descriptografado em palavras
    texto_original = []

    for palavra in palavras:
        # Inversão de dicionário para traduzir de volta
        palavra_original = {v: k for k, v in dicionario.items()}.get(palavra, palavra)
        texto_original.append(palavra_original)

    return ' '.join(texto_original)

# Função principal para escolher entre criptografar ou descriptografar
def main():
    escolha = input("Escolha uma opção (criptografar/descriptografar): ").strip().lower()

    coprimos_26 = [1, 3, 5, 7, 11, 13, 15, 17, 19, 23, 25]

    print("Valores válidos para 'a' (cóprimos com 26):", coprimos_26)

    if escolha == "criptografar":
        texto_original = input("Insira o texto a ser criptografado: ").strip()

        # Escolha dos parâmetros 'a' e 'b'
        a = int(input("Escolha o valor de 'a' (deve ser coprimo com 26): ").strip())
        b = int(input("Escolha o valor de 'b': ").strip())

        # Verifica se 'a' é coprimo com 26
        if a not in coprimos_26:
            print(f"O valor de 'a' ({a}) não é coprimo com 26. Escolha outro valor de 'a'.")
        else:
            texto_criptografado = criptografar(texto_original, dicionario_pt_fr, a, b)
            print("Texto Criptografado:", texto_criptografado)
    
    elif escolha == "descriptografar":
        # Escolher 'a' e 'b' para descriptografar
        a = int(input("Insira o valor de 'a' usado na criptografia (deve ser coprimo com 26): ").strip())
        b = int(input("Insira o valor de 'b' usado na criptografia: ").strip())

        # Verifica se 'a' é coprimo com 26
        if a not in coprimos_26:
            print(f"O valor de 'a' ({a}) não é coprimo com 26. Escolha outro valor de 'a'.")
        else:
            texto_cripto = input("Insira o texto criptografado: ").strip()
            texto_descriptografado = descriptografar(texto_cripto, dicionario_pt_fr, a, b)
            print("Texto Descriptografado:", texto_descriptografado)
    
    else:
        print("Opção inválida! Escolha 'criptografar' ou 'descriptografar'.")

# Chama a função principal
if __name__ == "__main__":
    main()


