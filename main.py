import bibliotecaGrafo
try:
    nome_arquivo = input("Digite o nome do arquivo com a sua extensão:")
    manipulador = open(nome_arquivo, "r")  # colocar uma mensagem de erro se nao abrir o arquivo
    linha = manipulador.readline()  # pega a linha de aresta e vertice
    linhaInt = list(map(int, (linha.split(' '))))
    vertice = int(linhaInt[0])
    aresta = int(linhaInt[1])
    op = int(input("Digite 1 para representar o grafo como lista de adjacencia  ou 2  para representar como matriz de adjacência:"))
    rep = bibliotecaGrafo.representacao(manipulador, vertice, aresta, op)
    if op == 1:
        print("-" *30)
        print("Lista de Adjacencia")
        print(rep)
        print("-" * 30)
        bibliotecaGrafo.informacoesListaAdjacencia(rep,aresta,vertice)

        bibliotecaGrafo.buscaLarguralista(rep, 0)
        bibliotecaGrafo.buscaProfundidadeLista(rep, 0)
        bibliotecaGrafo.componentesConexasLista(rep)
    if op ==2:
        print("-" * 30)
        print("Matriz de Adjacencia")
        print(rep)
        print("-" * 30)
        bibliotecaGrafo.informacoesMatrizAdjacencia(rep,aresta,vertice)
        bibliotecaGrafo.buscaLarguraMatriz(rep,0)
        bibliotecaGrafo.buscaProfundidadeMatriz(rep,0)
        #falta componentes conexas matriz
except:
    print("Verifique o nome do arquivo digitado!!!")