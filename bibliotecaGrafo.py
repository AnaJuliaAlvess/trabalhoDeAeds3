def representacao(arquivo, vertices, arestas, opcao):
    listaAd = [[] for i in range(vertices)]  # cria lista
    matrizAd = [[0 for i in range(vertices)] for i in range(vertices)]  # cria matriz
    # v = [i for i in range(vertices)]  # vetor vertices
    #a = []  # vetor com arestas
    for i in range(arestas):
        l = arquivo.readline()
        lInt = list(map(int, (l.split(' '))))
        origem = int(lInt[0])
        destino = int(lInt[1])
        peso = int(lInt[2])
        listaAd[origem].append((destino, peso))
        listaAd[destino].append((origem, peso))
        #a.append((origem, destino, peso))
        matrizAd[origem][destino] = peso
        matrizAd[destino][origem] = peso

    if opcao == 1:
        return listaAd
    if opcao == 2:
        return matrizAd

    return -1


def informacoesListaAdjacencia(listaad, arestas, vertices):
    cont = 0
    maior = 0
    menor = 0
    maiorVertice = -1
    menorVertice = -1
    grau = []
    for i in range(len(listaad)):
        cont = len(listaad[i])
        grau.append(cont)
        if cont > maior:
            maior = cont
            maiorVertice = i
        if cont < maior:
            if menorVertice < cont:
                menor = cont
                menorVertice = i

    grauMedio = (arestas * 2) / vertices
    contMaior = 0
    contMenor = 0
    for i in range(len(grau)):
        if grau[i] == maior:
            contMaior = contMaior + 1
        if grau[i] == menor:
            contMenor = contMenor + 1

    print(f"Maior grau: {maior} - vertice:  {maiorVertice}")
    print(f"Menor grau: {menor} - vertice:  {menorVertice}")
    print(f"Grau Médio: {grauMedio}")
    print("Frequecia Relativa:")
    print(f"Grau {menor} :  {contMenor / vertices}")
    print(f"Grau {maior} :  {contMaior / vertices}")


def informacoesMatrizAdjacencia(matriz, arestas, vertices):
    cont = 0
    maior = 0
    menor = 0
    maiorVertice = -1
    menorVertice = -1
    grau = []
    for i in range(vertices):
        cont = 5 - matriz[i].count(0)
        grau.append(cont)
        if cont > maior:
            maior = cont
            maiorVertice = i
        if cont < maior:
            if menorVertice < cont:
                menor = cont
                menorVertice = i

    grauMedio = (arestas * 2) / vertices
    contMaior = 0
    contMenor = 0
    for i in range(len(grau)):
        if grau[i] == maior:
            contMaior = contMaior + 1
        if grau[i] == menor:
            contMenor = contMenor + 1
    print(grau)
    print(f"Maior grau: {maior} - vertice:  {maiorVertice}")
    print(f"Menor grau: {menor} - vertice:  {menorVertice}")
    print(f"Grau Médio: {grauMedio}")
    print("Frequecia Relativa:")
    print(f"Grau {menor} :  {contMenor / vertices}")
    print(f"Grau {maior} :  {contMaior / vertices}")


def buscaLarguralista(G, s):
    desc = [0 for i in range(len(G))]
    nivel = [[] for i in range(len(G))]
    Q = [s]
    R = [s]
    desc[s] = 1
    nivel[s] = 0
    while len(Q) != 0:
        u = Q.pop(0)
        for e in G[u]:
            v = e[0]
            if desc[v] == 0:
                Q.append(v)
                R.append(v)
                desc[v] = 1
                nivel[v] = nivel[u] + 1
    # nivel_filtrado = list(filter(lambda x: x>-1, nivel))
    print("Busca largura: ")
    print("#vertice:nivel")
    for i in range(len(G)):
        if (nivel[i] != []):
            print("{}:{}".format(i, nivel[i]))

    # return R


def buscaLarguraMatriz(G, s):
    desc = [0 for i in range(len(G))]
    nivel = [[] for i in range(len(G))]
    Q = [s]
    R = [s]
    desc[s] = 1
    nivel[s] = 0
    while len(Q) != 0:
        u = Q.pop(0)
        for i in range(len(G[u])):
            if G[u][i] != 0 and desc[i] == 0:
                Q.append(i)
                R.append(i)
                desc[i] = 1
                nivel[i] = nivel[u] + 1

    print("Busca largura: ")
    print("#vertice:nivel")
    for i in range(len(G)):
        if nivel[i] != []:
            print("{}:{}".format(i, nivel[i]))


    # return R

def buscaProfundidadeLista(G,s):
    desc = [0 for i in range(len(G))]
    nivel = [[] for i in range(len(G))]
    S = [s]
    R = [s]
    desc[s] = 1
    nivel[s] = 0
    while len(S) != 0:
        u = S[-1]
        desempilhar = True
        for e in G[u]:
            v = e[0]
            if desc[v] == 0:
                desempilhar = False
                S.append(v)
                R.append(v)
                desc[v] = 1
                nivel[v] = nivel[u] + 1
                break
        if desempilhar:
            S.pop()

    print("Busca por profundidade:")
    print("#vertice:nivel")
    for i in range(len(G)):
        if (nivel[i] != []):
            print("{}:{}".format(i,nivel[i]))


    #return R

nome_arquivo = input("Digite o nome do arquivo com a sua extensão:")
manipulador = open(nome_arquivo, "r")  # colocar uma mensagem de erro se nao abrir o arquivo
linha = manipulador.readline()  # pega a linha de aresta e vertice
linhaInt = list(map(int, (linha.split(' '))))
vertice = int(linhaInt[0])
aresta = int(linhaInt[1])
op = int(input(
    "Digite 1 para representar o grafo como lista de adjacencia  ou 2  para representar como matriz de adjacência:"))
rep = representacao(manipulador, vertice, aresta, op)
print(rep)
# verificar como fazer essa escolha pq depende do usuario
informacoesListaAdjacencia(rep,aresta,vertice)
#informacoesMatrizAdjacencia(rep,aresta,vertice)
buscaLarguralista(rep,0)
#buscaLarguraMatriz(rep,0)
buscaProfundidadeLista(rep,0)


