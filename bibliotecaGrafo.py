def listaAdjacencia(arquivo,vertices,arestas):
    listaAd = [[] for i in range(vertices)]  # cria lista
    matrizAd = [[0 for i in range(vertices)] for i in range(vertices)]
    v = [i for i in range(vertices)] #vetor vertices
    a = [] #vetor com arestas
    for i in range(arestas):
        l = arquivo.readline()
        lInt= list(map(int, (l.split(' '))))
        origem= int(lInt[0])
        destino= int(lInt[1])
        peso=int(lInt[2])
        listaAd[origem].append((destino, peso))
        listaAd[destino].append((origem, peso))
        a.append((origem, destino, peso))
        matrizAd[origem][destino] = peso
        matrizAd[destino][origem] = peso

    for i in range(vertices):
        for j in range(vertices):
            print(matrizAd[i][j], end= " ")
        print()
    return listaAd

def matriz_adjacencia(arquivo,vertices,arestas):
    listaAd = [[] for i in range(vertices)]  # cria lista
    matrizAd = [[0 for i in range(vertices)] for i in range(vertices)]
    v = [i for i in range(vertices)]  # vetor vertices
    a = []  # vetor com arestas
    for i in range(arestas):
        l = arquivo.readline()
        lInt = list(map(int, (l.split(' '))))
        origem = int(lInt[0])
        destino = int(lInt[1])
        peso = int(lInt[2])
        listaAd[origem].append((destino, peso))
        listaAd[destino].append((origem, peso))
        a.append((origem, destino, peso))
        matrizAd[origem][destino] = peso
        matrizAd[destino][origem] = peso

    for i in range(vertices):
        for j in range(vertices):
            print(matrizAd[i][j], end=" ")
        print()
    return matrizAd

nome_arquivo = input("Digite o nome do arquivo com a sua extensão:")
manipulador= open(nome_arquivo, "r") # colocar uma mensagem de erro se nao abrir o arquivo
linha= manipulador.readline() #pega a linha de aresta e vertice
linhaInt= list(map(int, (linha.split(' '))))
vertice= int(linhaInt[0])
aresta=int(linhaInt[1])
op = int(input ("Digite 1 para representar o grafo como lista de adjacencia  ou 2  para representar como matriz de adjacência:"))
if op == 1:
    print(listaAdjacencia(manipulador,vertice,aresta))
else:
    matriz_adjacencia(manipulador, vertice,  aresta)