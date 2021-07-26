import time
import bibliotecaGrafo
try:
    nome_arquivo = input("Digite o nome do arquivo com a sua extensão:")
    manipulador = open(nome_arquivo, "r")
    linha = manipulador.readline()  # pega a linha de aresta e vertice
    linhaInt = linha.split(' ')
    vertice = int(linhaInt[0])
    aresta = int(linhaInt[1])
    op = int(input("Digite 1 para representar o grafo como lista de adjacencia  ou 2  para representar como matriz de adjacência:"))
    if op == 1:
        print("Lista de Adjacência")
        inicio=time.time()
        try:
            rep= bibliotecaGrafo.representacao_lista(manipulador, vertice, aresta)
        except:
             print("Erro de memória")
        fim=time.time()
        print("Tempo execução: {}".format(fim-inicio))
        print("-" * 30)
        print("Lista de Adjacencia")
        print(rep)
        print("-" * 30)
        diamentro=[]
        for i in range(vertice):
            diamentro.append(bibliotecaGrafo.buscaLarguralista(rep,i))
        print(diamentro)
        x=max(diamentro)
        print("Maximo:{}".format(x))
        bibliotecaGrafo.informacoesListaAdjacencia(rep, aresta, vertice)
        bibliotecaGrafo.buscaLarguralista(rep, 1)
        bibliotecaGrafo.buscaProfundidadeLista(rep, 0)
        bibliotecaGrafo.componentesConexasLista(rep)

    if op == 2:
        print("Matriz de Adjacência")
        inicio = time.time()
        try:
            rep = bibliotecaGrafo.representacao_matriz(manipulador, vertice, aresta)
        except:
            print("Erro de memória")
        fim = time.time()
        print("Tempo execução: {}".format(fim - inicio))
        print("-" * 30)
        print("Matriz de Adjacencia")
        print(rep)
        print("-" * 30)
        bibliotecaGrafo.informacoesMatrizAdjacencia(rep, aresta, vertice)
        bibliotecaGrafo.buscaLarguraMatriz(rep, 0)
        bibliotecaGrafo.buscaProfundidadeMatriz(rep, 0)
        bibliotecaGrafo.componentesConexasMatriz(rep)

    manipulador.close()

except:
    print("Verifique o nome do arquivo")
