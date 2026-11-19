class graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _  in range(size)]

def print_graph(graph, name) :
    print("=== " + name + " 그래프 정보 출력 ===")
    for row in range(graph.SIZE) :
        for col in range(graph.SIZE) :
            print(graph.graph[row][col], end=' ')
        print()


G1, G3 = None, None

G1 = graph(4)
G1.graph[0][1] = 1
G1.graph[0][2] = 1
G1.graph[0][3] = 1
G1.graph[1][1] = 1
G1.graph[1][2] = 1
G1.graph[2][0] = 1
G1.graph[2][1] = 1
G1.graph[2][3] = 1
G1.graph[3][0] = 1
G1.graph[3][2] = 1
print_graph(G1, "G1")

G3 = graph(4)
G3.graph[0][1] = 1
G3.graph[0][2] = 1
G3.graph[3][0] = 1
G3.graph[3][2] = 1
print_graph(G3, "G3")