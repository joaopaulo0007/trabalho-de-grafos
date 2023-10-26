import networkx as nx
import matplotlib.pyplot as plt 

class Grafo:
    def __init__(self):
        self.grafo = {}

    def cria_lista_vazia(self):
        return []
    
    def retorna_vertices_ligados(self,vertices):
        return self.grafo[vertices]

    def retorna_vertices(self):
        list_vertices = list(self.grafo)
        return list_vertices

    def add_vertice(self, vertice):
        self.grafo[vertice] = self.cria_lista_vazia()

    def add_aresta(self, vertice_1, vertice_2):
        self.grafo[vertice_1].append(vertice_2)
        self.grafo[vertice_2].append(vertice_1)

    def remove_aresta(self, vertice_1, vertice_2):
        if vertice_2 in self.grafo[vertice_1]:
            self.grafo[vertice_1].remove(vertice_2)
            self.grafo[vertice_2].remove(vertice_1)

    def calcula_grau(self, vertice):
        if vertice in self.grafo:
            return self.grafo[vertice].__len__()
        else:
            return 0

    def sao_vizinhos(self, vertice_1, vertice_2):
        if vertice_2 in self.grafo[vertice_1]:
            return True
        else:
            return False
    def ordena_grau_vertices(self):
        dict_vert = {}
        for vertice in self.grafo:
            vertice_graus = self.calcula_grau(vertice)
            dict_vert[vertice] = vertice_graus
        dict_vert = dict(sorted(dict_vert.items(), key=lambda item: item[1], reverse=True))
        return dict_vert
    def imprime_interface(self):
        dicionario = {}
        for chave in self.grafo:
            dicionario[chave] = self.grafo[chave]

        return dicionario
    def existe_vizinho_com_aquela_cor(self,dicionario,cor,vertice):
        vertices_ligados=self.retorna_vertices_ligados(vertice)
        ligado=False
        for vert in vertices_ligados:
            if vert  in dicionario[cor]:
                ligado=True
                break
        return ligado

    def colorir(self):
        vertices_ordenados = self.ordena_grau_vertices()
        dict_coloracao = {}
        cor = 0
        for vertice in vertices_ordenados:
            for i in range(cor + 1):
                if i not in dict_coloracao:
                    dict_coloracao[i] = []
                if not self.existe_vizinho_com_aquela_cor(dict_coloracao, i, vertice):
                    dict_coloracao[i].append(vertice)
                    break
            cor += 1
        return dict_coloracao
    
    def americaDoSul(self):
        grafoAmericaDoSul = Grafo() 


        listaPaisesAmericaDoSul = ["Argentina", "Bolivia", "Chile", "Brazil", "Colombia", "Ecuador", "Paraguay", "Venezuela", "Uruguay", "Guyana", "Peru", "Suriname", "France"]

        chavePaisesAmericaDoSul = {} 
        for i in range(0, 13): 
            grafoAmericaDoSul.add_vertice(i)
            chavePaisesAmericaDoSul[i] = listaPaisesAmericaDoSul[i] 


        listaFronteriasAmericaDoSul = [(0, 3), (0, 2), (0,8), (0,6), (0, 1), (1, 3), (1, 6), (1, 2), 
                                    (1, 10), (3, 8), (3, 6), (3, 10), (3, 4), (3, 7), (3, 11), (3, 9), (3, 12),
                                    (4, 10), (4, 5), (4, 7), (5, 10), (7, 9), (9, 11), (11, 12)]

        for fronteira in listaFronteriasAmericaDoSul: 
            grafoAmericaDoSul.add_aresta(fronteira[0], fronteira[1])
            
        colorirAmericaDoSUl = grafoAmericaDoSul.colorir()

        cores_finais = {cor: [chavePaisesAmericaDoSul[pais] for pais in listaPaisesAmericaDoSul] for cor, listaPaisesAmericaDoSul in colorirAmericaDoSUl.items()}
        
        G_americadosul = nx.Graph(grafoAmericaDoSul.imprime_interface())
        coloracao = nx.coloring.greedy_color(G_americadosul, strategy="largest_first")
        labels_americadosul = {vertice: chavePaisesAmericaDoSul[vertice] for vertice in G_americadosul.nodes()}
        cores = [coloracao[vertice] for vertice in G_americadosul.nodes()]
        pos_americadosul = nx.spring_layout(G_americadosul, seed=42)
        nx.draw(G_americadosul, pos_americadosul, with_labels=True, labels=labels_americadosul, node_color=cores, cmap=plt.cm.rainbow, node_size=500)
        plt.show()
        
        
        return cores_finais 
    
    def nordeste(self): 
        grafoNordeste = Grafo() 
        
        #                          0          1          2           3           4             5                  6        7       8 
        listaEstadosNordeste = ["Bahia", "Sergipe", "Alagoas", "Pernambuco", "Paraíba","Rio Grande do Norte", "Ceará", "Piauí", "Maranhão"]
        
        chaveEstadosNordeste = {}
        
        for i in range(0, 9): 
            grafoNordeste.add_vertice(i) 
            chaveEstadosNordeste[i] = listaEstadosNordeste[i] 
            
        listaFronteirasNordeste = [(0, 1), (0, 2), (0, 3), (0, 7), (1, 2), (2, 3), (3, 7), (3, 4), (3, 6), (4, 5), [4, 6], (5, 6), (6, 7), (7, 8)]
        
        for fronteira in listaFronteirasNordeste: 
            grafoNordeste.add_aresta(fronteira[0], fronteira[1])
        
        colorirNordeste = grafoNordeste.colorir()
        
        cores_finais = {cor: [chaveEstadosNordeste[pais] for pais in listaEstadosNordeste] for cor, listaEstadosNordeste in colorirNordeste.items()}
        
        G_Nordeste = nx.Graph(grafoNordeste.imprime_interface())
        coloracao = nx.coloring.greedy_color(G_Nordeste, strategy="largest_first")
        labels_nordeste = {vertice: chaveEstadosNordeste[vertice] for vertice in G_Nordeste.nodes()}
        cores = [coloracao[vertice] for vertice in G_Nordeste.nodes()]
        pos_nordeste = nx.spring_layout(G_Nordeste, seed=42)
        nx.draw(G_Nordeste, pos_nordeste, with_labels=True, labels=labels_nordeste, node_color=cores, cmap=plt.cm.rainbow, node_size=500)
        plt.show()
        
        return cores_finais






