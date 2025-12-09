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
    checked_edges = 0
    for u, v, d in ordered_edges:
        # points are isolated
        if not nx.has_path(G, u, v):
            G.add_edge(u, v)
        checked_edges += 1
        if checked_edges == 1000:
            break
    
    components = list(nx.connected_components(G))
    components_sorted = sorted(components, key=len, reverse=True)
    largest_three = components_sorted[:3]
    multi = 1
    for comp in largest_three:
        multi *= len(comp)
             
    print("Odgovor 1:", multi)


if __name__ == "__main__":
    main()
