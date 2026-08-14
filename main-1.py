from arquivo import carregar_livros, salvar_livros
from operacoes import cadastrar_livro, emprestar_livro, devolver_livro
from consultas import listar_livros, buscar_livro, ordenar_livros


livros = carregar_livros()

while True:

    print("\n==========================")
    print("      BIBLIOTECA")
    print("==========================")
    print("1 - Cadastrar livro")
    print("2 - Emprestar livro")
    print("3 - Devolver livro")
    print("4 - Listar livros")
    print("5 - Buscar livro")
    print("6 - Ordenar livros")
    print("7 - Sair")
    print("==========================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_livro(livros)

    elif opcao == "2":
        emprestar_livro(livros)

    elif opcao == "3":
        devolver_livro(livros)

    elif opcao == "4":
        listar_livros(livros)

    elif opcao == "5":
        buscar_livro(livros)

    elif opcao == "6":
        ordenar_livros(livros)

    elif opcao == "7":
        salvar_livros(livros)
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")
