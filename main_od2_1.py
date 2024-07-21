class TreeNode:
    def __init__(self, value):
        # Конструктор узла дерева
        self.value = value  # Значение узла
        self.left = None    # Левый потомок
        self.right = None   # Правый потомок

# Пример создания дерева
root = TreeNode(1)            # Корень дерева
root.left = TreeNode(2)       # Левый потомок корня
root.right = TreeNode(3)      # Правый потомок корня
root.left.left = TreeNode(4)  # Левый потомок левого потомка корня
root.left.right = TreeNode(5) # Правый потомок левого потомка корня

# Вывод значений дерева
print("Дерево:")
print("Корень:", root.value)
print("Левый потомок корня:", root.left.value)
print("Правый потомок корня:", root.right.value)
print("Левый потомок левого потомка корня:", root.left.left.value)
print("Правый потомок левого потомка корня:", root.left.right.value)

print('-----------------------------------')

class Graph:
    def __init__(self, vertices):
        # Конструктор графа
        self.vertices = vertices  # Количество вершин
        self.adjacency_list = [[] for _ in range(vertices)]  # Список смежности

    def add_edge(self, u, v):
        # Метод добавления ребра
        self.adjacency_list[u].append(v)  # Добавить v в список смежности u
        self.adjacency_list[v].append(u)  # Добавить u в список смежности v

# Пример создания графа
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

# Вывод списка смежности
print("Граф (ненаправленный):")
for i in range(len(g.adjacency_list)):
    print(f"Вершина {i}: {g.adjacency_list[i]}")

print('-----------------------------------')

class DirectedGraph:
    def __init__(self, vertices):
        # Конструктор графа
        self.vertices = vertices  # Количество вершин
        self.adjacency_list = [[] for _ in range(vertices)]  # Список смежности

    def add_edge(self, u, v):
        # Метод добавления ребра
        self.adjacency_list[u].append(v)  # Добавить v в список смежности u

# Пример создания направленного графа
dg = DirectedGraph(5)
dg.add_edge(0, 1)
dg.add_edge(0, 4)
dg.add_edge(1, 2)
dg.add_edge(1, 3)
dg.add_edge(2, 3)
dg.add_edge(3, 4)

# Вывод списка смежности
print("Граф (направленный):")
for i in range(len(dg.adjacency_list)):
    print(f"Вершина {i}: {dg.adjacency_list[i]}")
