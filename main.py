from funcoes import adicionar, carregar_compromissos, excluir, listar, sair


def main():
    compromissos = carregar_compromissos()

    while True:
        print("\n=== Agenda ===")
        print("1. Lista")
        print("2. Adicionar")
        print("3. Excluir")
        print("4. Sair")

        try:
            opcao = input("Escolha uma opção: ").strip()
        except EOFError:
            print()
            sair()
            break

        if opcao == "1":
            listar(compromissos)
        elif opcao == "2":
            adicionar(compromissos)
        elif opcao == "3":
            excluir(compromissos)
        elif opcao == "4":
            sair()
            break
        else:
            print("Opção inválida. Escolha um número de 1 a 4.")


if __name__ == "__main__":
    main()
