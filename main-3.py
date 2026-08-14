from arquivo import salvar_livros


def cadastrar_livro(livros):
    print("\n--- CADASTRAR LIVRO ---")

    titulo = input("Digite o título: ")
    autor = input("Digite o autor: ")
    ano = input("Digite o ano: ")
    isbn = input("Digite o ISBN: ")

    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "isbn": isbn,
        "status": "Disponível"
    }

    livros.append(livro)

    salvar_livros(livros)

    print("Livro cadastrado!")


def emprestar_livro(livros):
    print("\n--- EMPRESTAR LIVRO ---")

    isbn = input("Digite o ISBN do livro: ")

    for livro in livros:
        if livro["isbn"] == isbn:

            if livro["status"] == "Disponível":
                livro["status"] = "Emprestado"
                salvar_livros(livros)
                print("Livro emprestado!")
            else:
                print("O livro já está emprestado.")

            return

    print("Livro não encontrado.")


def devolver_livro(livros):
    print("\n--- DEVOLVER LIVRO ---")

    isbn = input("Digite o ISBN do livro: ")

    for livro in livros:
        if livro["isbn"] == isbn:

            if livro["status"] == "Emprestado":
                livro["status"] = "Disponível"
                salvar_livros(livros)
                print("Livro devolvido!")
            else:
                print("O livro já está disponível.")

            return

    print("Livro não encontrado.")
