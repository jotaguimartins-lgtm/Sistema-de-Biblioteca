ARQUIVO = "livros.txt"


def carregar_livros():
    livros = []

    arquivo = open(ARQUIVO, "a", encoding="utf-8")
    arquivo.close()

    arquivo = open(ARQUIVO, "r", encoding="utf-8")

    for linha in arquivo:
        dados = linha.strip().split(";")

        if len(dados) == 5:
            livro = {
                "titulo": dados[0],
                "autor": dados[1],
                "ano": dados[2],
                "isbn": dados[3],
                "status": dados[4]
            }

            livros.append(livro)

    arquivo.close()

    return livros


def salvar_livros(livros):
    arquivo = open(ARQUIVO, "w", encoding="utf-8")

    for livro in livros:
        linha = (
            livro["titulo"] + ";" +
            livro["autor"] + ";" +
            livro["ano"] + ";" +
            livro["isbn"] + ";" +
            livro["status"] + "\n"
        )

        arquivo.write(linha)

    arquivo.close()
