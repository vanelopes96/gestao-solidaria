# Sistema de Gestão Comunitária — MVP
# Projeto: Igreja Assembleia de Deus / Guaianases

def tela_menu():
    print("=" * 50)
    print("          SISTEMA DE GESTÃO SOLIDÁRIA")
    print("=" * 50)
    print()
    print("        === MENU PRINCIPAL ===")
    print()
    print("    1. 📋 Cadastro de Famílias")
    print("    2. 📦 Controle de Estoque")
    print("    3. 📝 Registro de Entregas")
    print("    4. 📊 Relatórios")
    print("    0. Sair")
    print()
    print("=" * 50)
    opcao = input("   Selecione uma opção: ")
    return opcao

def tela_registro_entrega():
    print("\n" + "=" * 50)
    print("        REGISTRO DE ENTREGA DE DOAÇÕES")
    print("=" * 50)
    print()
    familia = input("  Nome da Família: ")
    data = input("  Data da Entrega (dd/mm/aaaa): ")
    print()
    print("  Itens entregues:")
    arroz = input("    Arroz (kg): ")
    feijao = input("    Feijão (kg): ")
    oleo = input("    Óleo (unid): ")
    print()
    print("  ✅ Entrega registrada com sucesso!")
    print(f"  Família: {familia} | Data: {data}")
    print("=" * 50)
    input("\n  Pressione ENTER para voltar...")

def main():
    while True:
        opcao = tela_menu()
        if opcao == "1":
            print("\n  📋 Tela de Cadastro de Famílias — em construção...")
            input("  Pressione ENTER para voltar...")
        elif opcao == "2":
            print("\n  📦 Tela de Estoque — em construção...")
            input("  Pressione ENTER para voltar...")
        elif opcao == "3":
            tela_registro_entrega()
        elif opcao == "0":
            print("\n  Saindo do sistema... Até logo!")
            break
        else:
            print("\n  ❌ Opção inválida! Tente novamente.")
            input("  Pressione ENTER para continuar...")

if __name__ == "__main__":
    main()
