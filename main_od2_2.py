import networkx as nx
import matplotlib.pyplot as plt

# Класс для узла дерева
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Функция для построения графа из дерева
def build_tree_graph(node, graph=None, pos=None, x=0, y=0, layer=1):
    if graph is None:
        graph = nx.DiGraph()
    if pos is None:
        pos = {}
    graph.add_node(node.value, pos=(x, y))
    pos[node.value] = (x, y)
    if node.left:
        graph.add_edge(node.value, node.left.value)
        build_tree_graph(node.left, graph=graph, pos=pos, x=x-layer, y=y-1, layer=layer/2)
    if node.right:
        graph.add_edge(node.value, node.right.value)
        build_tree_graph(node.right, graph=graph, pos=pos, x=x+layer, y=y-1, layer=layer/2)
    return graph, pos

# Пример создания дерева
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Построение и визуализация дерева
tree_graph, tree_pos = build_tree_graph(root)
nx.draw(tree_graph, tree_pos, with_labels=True, arrows=False, node_size=700, node_color="lightblue")
plt.title("Дерево")
plt.show()


print('---------------------------------------------------------------------------------')

# Класс для графа
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

# Функция для построения и визуализации графа
def visualize_graph(graph):
    G = nx.Graph()
    for i in range(len(graph.adjacency_list)):
        for j in graph.adjacency_list[i]:
            G.add_edge(i, j)
    pos = nx.spring_layout(G)  # Позиции для всех узлов
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightgreen")
    plt.title("Граф (ненаправленный)")
    plt.show()

# Пример создания графа
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

# Визуализация графа
visualize_graph(g)


print('---------------------------------------------------------------------------------')

# Класс для направленного графа
class DirectedGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)

# Функция для построения и визуализации направленного графа
def visualize_directed_graph(graph):
    G = nx.DiGraph()
    for i in range(len(graph.adjacency_list)):
        for j in graph.adjacency_list[i]:
            G.add_edge(i, j)
    pos = nx.spring_layout(G)  # Позиции для всех узлов
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightcoral", arrows=True)
    plt.title("Граф (направленный)")
    plt.show()

# Пример создания направленного графа
dg = DirectedGraph(5)
dg.add_edge(0, 1)
dg.add_edge(0, 4)
dg.add_edge(1, 2)
dg.add_edge(1, 3)
dg.add_edge(2, 3)
dg.add_edge(3, 4)

# Визуализация направленного графа
visualize_directed_graph(dg)

