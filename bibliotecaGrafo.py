#def lista_adjacencia(listaArquivo):




nome_arquivo = input("Digite o nome do arquivo com a sua extensão:")
manipulador = open(nome_arquivo, "r")
print(manipulador.read()) #imprime a lista só para  verificar se abriu
manipulador.seek(0) #volta para o inicio do arquivo
lista_arquivo= manipulador.readlines() #cria uma lista com os elementos do arquivo .txt
lista_grafo= []
for i in lista_arquivo:
     for e in i:
         if  e == '\n':
             break;
         else:
             lista_grafo.index(e)

print(lista_arquivo)
print (lista_grafo)