from arquivo import salvar_livros


def listar_livros(livros):
    print("\n--- TODOS OS LIVROS ---")

    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
    else:
        for livro in livros:
            print("-------------------------")
            print("Título:", livro["titulo"])
            print("Autor:", livro["autor"])
            print("Ano:", livro["ano"])
            print("ISBN:", livro["isbn"])
            print("Status:", livro["status"])


def buscar_livro(livros):
    print("\n--- BUSCAR LIVRO ---")

    busca = input("Digite o título ou autor: ").lower()

    encontrou = False

    for livro in livros:
        titulo = livro["titulo"].lower()
        autor = livro["autor"].lower()

        if busca in titulo or busca in autor:
            print("-------------------------")
            print("Título:", livro["titulo"])
            print("Autor:", livro["autor"])
            print("Ano:", livro["ano"])
            print("ISBN:", livro["isbn"])
            print("Status:", livro["status"])

            encontrou = True

    if encontrou == False:
        print("Nenhum livro encontrado.")


def ordenar_livros(livros):
    print("\n--- ORDENAR LIVROS ---")
    print("1 - Título")
    print("2 - Autor")
    print("3 - Ano")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        for i in range(len(livros)):
            for j in range(i + 1, len(livros)):
                if livros[i]["titulo"].lower() > livros[j]["titulo"].lower():
                    temp = livros[i]
                    livros[i] = livros[j]
                    livros[j] = temp

        print("Livros ordenados por título.")

    elif opcao == "2":
        for i in range(len(livros)):
            for j in range(i + 1, len(livros)):
                if livros[i]["autor"].lower() > livros[j]["autor"].lower():
                    temp = livros[i]
                    livros[i] = livros[j]
                    livros[j] = temp

        print("Livros ordenados por autor.")

    elif opcao == "3":
        for i in range(len(livros)):
            for j in range(i + 1, len(livros)):
                if livros[i]["ano"] > livros[j]["ano"]:
                    temp = livros[i]
                    livros[i] = livros[j]
                    livros[j] = temp

        print("Livros ordenados por ano.")

    else:
        print("Opção inválida.")

    salvar_livros(livros)
