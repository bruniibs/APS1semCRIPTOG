def cifra_cesar(texto, chave=3):
    """Aplica a cifra de César com chave fixa = 3"""
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) - base + chave) % 26 + base)
        else:
            resultado += char
    return resultado  # CORREÇÃO: return fora do loop

def xor(texto, chave):
    """Aplica XOR em cada caractere"""
    return "".join(chr(ord(c) ^ chave) for c in texto)

def criptografar(texto, chave_xor):
    """Criptografa com César (3) + XOR"""
    cesar = cifra_cesar(texto, 3)
    return xor(cesar, chave_xor)

def descriptografar(texto, chave_xor):
    """Descriptografa com XOR + César inverso (3)"""
    texto_xor = xor(texto, chave_xor)
    return cifra_cesar(texto_xor, -3)

# ------------------------ PROGRAMA PRINCIPAL ------------------------------
def main():
    while True:
        print("\n=== Criptografia César (fixo=3) + XOR ===")
        print("1 - Criptografar")
        print("2 - Descriptografar")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "3":
            print("Saindo do programa...")
            break

        if opcao not in ["1", "2"]:
            print("Opção inválida!")
            continue

        mensagem = input("Digite a mensagem (máx 128 caracteres): ")[:128]
        chave_xor = int(input("Digite a chave XOR (0~255): "))

        if opcao == "1":
            cript = criptografar(mensagem, chave_xor)
            print("\nMensagem criptografada:")
            print(cript.encode("latin1"))
            print("(selecionar apenas a mensagem DENTRO das aspas!!!")
        elif opcao == "2":
            try:
                # Para descriptografar, assumimos que a entrada já está em formato criptografado
                decript = descriptografar(mensagem, chave_xor)
                print("\nMensagem descriptografada:")
                print(decript)
            except Exception as e:
                print(f"Erro ao descriptografar: {e}")

if __name__ == "__main__":
    main()