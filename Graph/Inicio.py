from graphviz import Graph


def crearGraph(self):
    grafo = Graph(name=self.nombre, format='png', filename=self.nombre)
    grafo.node('i', 'i', shape='circle')
    grafo.node('p', 'p', shape='circle')
    grafo.node('q', 'q', shape='circle')
    grafo.node('f', 'f', shape='doublecircle')
    impresion = ''
    for elemento in self.produccionesAP:
        prod = ''
        for elemento1 in elemento.guarda:
            prod += elemento1
        palabra = elemento.lectura + ',' + elemento.pila + ';' + prod
        if elemento.inicio == elemento.final:
            impresion += palabra + '\n'
        else:
            grafo.edge(elemento.inicio, elemento.final, palabra)
    grafo.edge('q', 'q', impresion)
    grafo.render(view=True)


def crearArbol(ast):
    graph = Grafo()
    grafo = Graph(name="arbol", format='png', filename="./static/images/arbol")
    grafo.attr('node', shape='record')
    grafo.node(str(graph.indice), 'INSTRUCCIONES')
    graph.indice += 1
    for instr in ast:
        instr.graph(grafo, graph)
        graph.indice += 1
        graph.pivote1 = 0
    print(grafo.source)
    grafo.render(view=False)


class Grafo:
    def __init__(self):
        self.indice = 0
        self.pivote1 = 0
        self.pivote2 = 0
        self.pivote3 = 0
