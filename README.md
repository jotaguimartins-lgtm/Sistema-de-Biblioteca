# Sistema de Biblioteca
Sistema em Python para controlar o acervo de uma biblioteca. Dá pra cadastrar livro, emprestar, devolver, listar, buscar e ordenar o catálogo. Os dados são salvos em `livros.txt`, então não se perde nada quando o programa fecha. O código foi separado em 4 arquivos pra ficar mais organizado, cada um cuidando de uma parte do sistema.
 Como rodar:
 
1. Precisa ter o Python 3 instalado.
2. Baixe os arquivos e coloque todos na mesma pasta.
3. No terminal, dentro da pasta, rode:
   ```
   python main.py
   ```
4. Aparece o menu, é só digitar o número da opção.
 
 O que o sistema faz:
 
Cadastrar livro**: pede título, autor, ano e ISBN e já cadastra como "Disponível".
Emprestar livro**: busca pelo ISBN e muda o status pra "Emprestado" (se já estiver emprestado, avisa).
Devolver livro**: busca pelo ISBN e volta o status pra "Disponível".
Listar livros**: mostra todos os livros cadastrados com os dados completos.
Buscar livro**: procura por título ou autor (não faz diferença entre maiúscula e minúscula).
Ordenar livros**: organiza por título, autor ou ano.

Arquivos do projeto:

`main.py` — é o arquivo que roda o programa, mostra o menu e fica em loop até o usuário sair.
`arquivo.py` — cuida de ler e salvar os dados no `livros.txt`.
`operacoes.py` — as funções que mexem no acervo: cadastrar, emprestar e devolver.
`consultas.py` — as funções que só consultam ou reorganizam: listar, buscar e ordenar.

Detalhes de implementação:

 O menu usa `if/elif/else` dentro de um `while True`, que só para quando a opção 7 (Sair) é escolhida.
 Cada livro é representado por um dicionário (`titulo`, `autor`, `ano`, `isbn`, `status`), e todos ficam guardados numa lista.
 A ordenação foi feita "na mão", com dois loops (tipo bubble sort), sem usar `sort()` pronto do Python.
 Os dados são salvos no `livros.txt` em texto puro, com os campos separados por `;`, e recarregados toda vez que o programa é aberto.
