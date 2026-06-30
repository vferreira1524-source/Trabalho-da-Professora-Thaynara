
from database import *

criar_tabela()


def cadastrar():
    titulo = input("Título: ")
    autor = input("Autor: ")

    cd_livro(titulo, autor)

    print("Livro cadastrado com sucesso!\n")


def listar():
    livros = exibir_livros()

    if not livros:
        print("Nenhum livro cadastrado.\n")
        return False

    print("\n" + "=" * 70)
    print("📙📘📗             LISTA DE LIVROS          📙📘📗")
    print("=" * 70)

    for livro in livros:
        status = "Disponível" if livro[3] == 1 else "Emprestado"

        print(
            f"ID: {livro[0]} | "
            f"Título: {livro[1]} | "
            f"Autor: {livro[2]} | "
            f"Status: {status}"
        )

    print()
    return True


def emprestar():
    if not listar():
        return

    try:
        id_livro = int(input("Digite o ID do livro: "))

        if emprestar_livro(id_livro):
            print("📙 Livro emprestado!\n")
        else:
            print("❌ Livro não encontrado ou já emprestado.\n")

    except ValueError:
        print("❌ Digite apenas números!\n")


def devolver():
    if not listar():
        return

    try:
        id_livro = int(input("Digite o ID do livro: "))

        if devolver_livro(id_livro):
            print("✅ Livro devolvido!\n")
        else:
            print("❌ Livro não encontrado ou já disponível.\n")

    except ValueError:
        print("❌ Digite apenas números!\n")


def remover():
    print("\n📗📘📙 LIVROS CADASTRADOS 📗📘📙")
    
    if not listar():
        return
    
    try:
        id_livro = int(input("\nDigite o ID do livro a ser removido: "))

        if remover_livro(id_livro):
            print("\n🗑️ Livro removido com sucesso!")

            print("\n📗📘📙 LIVROS ATUALIZADOS 📗📘📙")  #Chamar lista atualizada
            listar()

        else:
            print("\n🛑 Livro não encontrado.")

    except ValueError:
        print("\n🛑 Digite apenas números!")


def menu():
    while True:
        print("=" * 70)
        print("📚         BIBLIOTECA - MENU PRINCIPAL         📚")
        print("=" * 70)
        print("1 - Cadastrar livro")
        print("2 - Listar livros")
        print("3 - Emprestar livro")
        print("4 - Devolver livro")
        print("5 - Remover livro")
        print("0 - Sair")
        print("=" * 70)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            emprestar()
        elif opcao == "4":
            devolver()
        elif opcao == "5":
            remover()
        elif opcao == "0":
            print("Saindo... Até logo!")
            break
        else:
            print("❌ Opção inválida!\n")


if __name__ == "__main__":
    menu()
