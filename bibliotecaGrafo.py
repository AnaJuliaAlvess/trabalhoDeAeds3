def representacao(arquivo, vertices, arestas, opcao):
    listaAd = [[] for i in range(vertices)]  # cria lista
    matrizAd = [[0 for i in range(vertices)] for i in range(vertices)]  # cria matriz
    for i in range(arestas):
        l = arquivo.readline()
        lInt = list(map(int, (l.split(' '))))
        origem = int(lInt[0])
        destino = int(lInt[1])
        peso = int(lInt[2])
        listaAd[origem].append((destino, peso))
        listaAd[destino].append((origem, peso))
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

    print("-"*30)
    print("Maior grau: {} -  vertice: {}".format(maior, maiorVertice))
    print("Menor grau: {} -  vertice: {}".format(menor, menorVertice))
    print("Grau Médio: {}".format(grauMedio))
    print("Frequecia Relativa: ")
    print("Grau {} :  {} ".format(menor,contMenor/vertices))
    print("Grau {} :  {}".format(maior,contMaior/vertices))
    print("-" * 30)

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

    print("-" * 30)
    print("Maior grau: {} -  vertice: {}".format(maior, maiorVertice))
    print("Menor grau: {} -  vertice: {}".format(menor, menorVertice))
    print("Grau Médio: {}".format(grauMedio))
    print("Frequecia Relativa: ")
    print("Grau {} :  {} ".format(menor, contMenor / vertices))
    print("Grau {} :  {}".format(maior, contMaior / vertices))
    print("-" * 30)


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
    print("-"*30)
    print("Busca largura: ")
    print("#vertice:nivel")
    for i in range(len(G)):
        if (nivel[i] != []):
            print("{}:{}".format(i, nivel[i]))
    print("-" * 30)

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
    print("-" * 30)
    print("Busca largura: ")
    print("#vertice:nivel")
    for i in range(len(G)):
        if nivel[i] != []:
            print("{}:{}".format(i, nivel[i]))
    print("-" * 30)

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
    print("-" * 30)
    print("Busca por profundidade:")
    print("#vertice:nivel")
    for i in range(len(G)):
        if (nivel[i] != []):
            print("{}:{}".format(i,nivel[i]))
    print("-" * 30)

    #return R
def buscaProfundidadeMatriz(G,s):
    desc = [0 for i in range(len(G))]
    nivel = [[] for i in range(len(G))]
    S = [s]
    R = [s]
    desc[s] = 1
    nivel[s] = 0
    while len(S) != 0:
        u = S[-1]
        desempilhar = True
        for i in range(len(G[u])):
            if G[u][i] != 0 and desc[i] == 0:
                desempilhar = False
                S.append(i)
                R.append(i)
                desc[i] = 1
                nivel[i] = nivel[u] + 1
                break
        if desempilhar:
            S.pop()
    print("-"*30)
    print("Busca por profundidade:")
    for i in range(len(G)):
        if (nivel[i] != []):
            print ("{}:{}".format(i, nivel[i]))
    print("-"*30)
    return R

def buscaProfundidadeListaConexa(G, s, marca):
    desc = [0 for i in range(len(G))]
    S = [s]
    R = [s]
    desc[s] = 1
    vComp[s]=marca
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
                break
        vComp[u]=marca
        if desempilhar:
            S.pop()


def componentesConexasLista(G):
    global vComp
    vComp = [0 for i in range(len(G))]
    marca = 0
    for i in range(len(G)):
        if vComp[i] == 0:
            marca= marca + 1
            buscaProfundidadeListaConexa(G, i, marca)

    print("Componentes Conexas:{}".format(marca))
    n = max(vComp)
    for i in range(1,n+1):
        print("{} vertices".format(vComp.count(i)))

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
#informacoesListaAdjacencia(rep,aresta,vertice)
informacoesMatrizAdjacencia(rep,aresta,vertice)
#buscaLarguralista(rep,0)
#buscaLarguraMatriz(rep,0)
#buscaProfundidadeLista(rep,0)
#buscaProfundidadeMatriz(rep,0)
componentesConexasLista(rep)


