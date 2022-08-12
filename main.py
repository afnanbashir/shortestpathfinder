class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    def add_edge(self, src, dest):
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


def add_area_corners(x, y, length, width, shop_entrance):
    top_left_corner_x = x - length // 2
    top_left_corner_y = y - width // 2
    xx = top_left_corner_x
    yy = top_left_corner_y
    while yy <= top_left_corner_y + width - 1:
        if str(xx) + "," + str(yy) not in shop_entrance:
            walls_list.append(str(xx) + "," + str(yy))
        yy += 1
    yy -= 1
    while xx <= top_left_corner_x + length - 1:
        if str(xx) + "," + str(yy) not in shop_entrance:
            walls_list.append(str(xx) + "," + str(yy))
        xx += 1
    xx -= 1
    while yy >= top_left_corner_y:
        if str(xx) + "," + str(yy) not in shop_entrance:
            walls_list.append(str(xx) + "," + str(yy))
        yy -= 1
    yy += 1
    while xx >= top_left_corner_x:
        if str(xx) + "," + str(yy) not in shop_entrance:
            walls_list.append(str(xx) + "," + str(yy))
        xx -= 1


def shortest_path(graph, start, goal):
    explored = []
    queue = [[start]]
    if start == goal:
        print("Same Node")
        return
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbour = graph[node]
            while neighbour:
                new_path = list(path)
                new_path.append(neighbour.vertex)
                queue.append(new_path)
                if neighbour.vertex == goal:
                    return new_path
                neighbour = neighbour.next
            explored.append(node)
    print("Path not found")
    return None


def add_graph_edges(x, y, xx, yy, graph):
    if str(x) + "," + str(y) not in walls_list and str(xx) + "," + str(yy) in coord_list and str(xx) + "," + str(
            yy) not in walls_list:
        graph.add_edge(coord_list.index(str(x) + "," + str(y)), coord_list.index(str(xx) + "," + str(yy)))
    return graph


if __name__ == '__main__':
    coord_list = []
    walls_list = []
    # currently doing it using hard coded values, in reality it will be based on data from the database.
    # for loading the map of a specific building:
    building_length = 24
    building_width = 60
    x = 0
    for i in range(building_length):
        for j in range(building_width):
            coord_list.append(str(i) + "," + str(j))
    add_area_corners(12, 30, building_length, building_width, ["0,1", "0,2", "0,3", "0,4", "0,5",
                                                               "0,6", "0,7", "0,8", "0,9", "0,10",
                                                               "0,11", "0,12", "0,13", "0,14", "0,15",
                                                               "0,16", "0,17", "0,18", "0,19", "0,20",
                                                               "0,21", "0,22", "0,23", "22,59", "21,59",
                                                               "20,59"])
    graph = Graph(building_length * building_width)
    for x in range(building_length):
        for y in range(building_width):
            graph = add_graph_edges(x, y, x + 1, y, graph)
            graph = add_graph_edges(x, y, x+1, y+1, graph)
            graph = add_graph_edges(x, y, x+1, y-1, graph)
            graph = add_graph_edges(x, y, x - 1, y, graph)
            graph = add_graph_edges(x, y, x-1, y+1, graph)
            graph = add_graph_edges(x, y, x-1, y-1, graph)
            graph = add_graph_edges(x, y, x, y + 1, graph)
            graph = add_graph_edges(x, y, x, y - 1, graph)
    for m in range(building_length):
        for n in range(building_width):
            if str(m) + "," + str(n) in walls_list:
                print("•", end='')
            else:
                print(" ", end='')
        print("\n")

    # for finding shortest path between user's location and the destination:
    # currently taking locationas as input from user.
    # in reality, the source location will be taken from user's gps location.
    # and for destination the user will select the category or shop, and we will get the location from the database.
    a = "4,42"
    b = "4,12"
    c = "11,30"
    d = "18,12"
    e = "22,7"
    f = "17,42"
    g = "21,42"
    my_list = [a, b, c, d, e, f, g]
    print(" 0 for A \n 1 for B \n 2 for C \n 3 for D \n 4 for E \n 5 for F \n 6 for G")
    source = my_list[int(input("select your source: "))]
    destination = my_list[int(input("select your destination: "))]
    import os

    os.system('cls' if os.name == 'nt' else 'clear')
    for m in range(building_length):
        for n in range(building_width):
            if str(m) + "," + str(n) in walls_list:
                print("•", end='')
            elif str(m) + "," + str(n) == source:
                print("S", end='')
            elif str(m) + "," + str(n) == destination:
                print("D", end='')
            else:
                print(" ", end='')
        print("\n")

    option = input("Confirm? (y/n) ")
    if option == "y":
        path = shortest_path(graph.graph, coord_list.index(source),
                             coord_list.index(destination))
        if path:
            new_path = []
            for p in path:
                new_path.append(coord_list[p])
                print(coord_list[p])
            os.system('cls' if os.name == 'nt' else 'clear')
            for m in range(building_length):
                for n in range(building_width):
                    if str(m) + "," + str(n) in walls_list:
                        print("•", end='')
                    elif str(m) + "," + str(n) == source:
                        print("S", end='')
                    elif str(m) + "," + str(n) == destination:
                        print("D", end='')
                    elif str(m) + "," + str(n) in new_path:
                        print("o", end='')
                    else:
                        print(" ", end='')
                print("\n")
