# Taking number of nodes that we need in our graph
num_nodes = int(input("enter no of nodes: "))

# Taking number of edges we need in our graph
num_edges = int(input("how many edges?: "))

# Taking the edges
edges = [tuple(map(int, input("enter edge: ").split())) for r in range(num_edges)]

# It's a graph class that will form a graph which will connect the edges to each other and it is responsible for display
# the graph in the proper format
class Graph:
    def __init__(self, num_nodes, edges):
        self.data = [[] for _ in range(num_nodes)]

        # link nodes
        for v1, v2 in edges:
            for edge in edges:
                self.data[v1].append(v2)
                self.data[v2].append(v1)

        # remove duplicates
        self.data = [list(set(entry)) for entry in self.data]

    def __repr__(self):
        return "\n".join(["{} : {}".format(i, neighbors) for (i, neighbors) in enumerate(self.data)])

    def __str__(self):
        return repr(self)
g1 = Graph(num_nodes, edges)


# Looping the operation
while True:
    print("Enter\n1.Display Graph 2.BFS  3.DFS 4.Quit:  ")
    user = int(input());

    # Displaying the graph that has been created through the graph class
    if user == 1:
        print(g1)

    # taking source input for BFS and display the bfs of the graph
    elif user == 2:
        source = int(input("Enter the source for bfs:"))
        def bfs(graph, source):

            visited = [False] * len(graph.data)
            queue = []

            visited[source] = True
            queue.append(source)
            i = 0

            while i < len(queue):
                for v in graph.data[queue[i]]:
                    if not visited[v]:
                        visited[v] = True
                        queue.append(v)
                i += 1

            return queue
        print(bfs(g1,source ))

   # taking source input for BFS and display the dfs of the graph
    elif user == 3:
        source1 =int(input("Enter the source for dfs:"))

        def dfs(graph, source):
            visited = [False] * len(graph.data)
            stack = [source]
            result = []

            while len(stack) > 0:
                current = stack.pop()
                if not visited[current]:
                    result.append(current)
                    visited[current] = True
                    for v in graph.data[current]:
                        stack.append(v)

            return result
        print(dfs(g1,source1))

    # it will help to exit from session
    elif user == 4:
        break
    # Will show error to user to input a right input
    else:
        print("Please choose correct answer !!!")














