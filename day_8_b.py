import math
import networkx as nx

def main():
    points = []
    with open("datas/8_data.txt") as f:
        lines = f.readlines()
        for line in lines:
            points.append(line.strip().split(","))

    edges = []
    G = nx.Graph()
    for i, point1 in enumerate(points):
        G.add_node(i, pos=point1)
        if i == len(points) - 1:
            continue
        for j, point2 in enumerate(points[i+1:]):
            dist = math.sqrt(
                    (int(point1[0]) - int(point2[0]))**2 +
                    (int(point1[1]) - int(point2[1]))**2 +
                    (int(point1[2]) - int(point2[2]))**2
                )
            edges.append((i, i+j+1, dist))
    
    ordered_edges = sorted(edges, key=lambda x: x[2])
    last1 = None
    last2 = None
    for u, v, d in ordered_edges:
        if nx.is_connected(G):
            break
        # points are isolated
        if not nx.has_path(G, u, v):
            G.add_edge(u, v)
            last1 = u
            last2 = v
    
    multi = int(G.nodes[last1]["pos"][0]) * int(G.nodes[last2]["pos"][0])
             
    print("Odgovor 2:", multi)


if __name__ == "__main__":
    main()
