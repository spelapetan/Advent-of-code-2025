
def all_paths(graph, root):
    paths = []

    def dfs(node, path):
        # add this node to current path
        path.append(node)

        # if leaf → store the path
        if not graph[node]:  
            paths.append(path.copy())
        else:
            # continue DFS to children
            for child in graph[node]:
                dfs(child, path)

        # backtrack
        path.pop()

    dfs(root, [])
    return paths

mem = {}

def count_paths(graph, node):
    # if this node has no children → it's a leaf → 1 path ends here
    if not graph[node]:
        return 1
    
    total = 0
    for child in graph[node]:
        res = mem.get(child)
        if res is not None:
            total += res
        else:
           res = count_paths(graph, child)
           mem[child] = res
           total += res
    return total

def main():
    grid = []
    with open("datas/7_data.txt") as f:
        lines = f.readlines()
        for line in lines:
            grid.append(list(line.strip()))
    
    count = 0
    # build a tree
    graph = {}
    root = None
    for i, row in enumerate(grid):
        for j, el in enumerate(row):
            if el == "^":
                if 0 <= i-1 < len(grid) and grid[i-1][j] == "|":
                    if 0 <= j-1:
                        grid[i][j-1] = "|"
                        graph[(i, j-1)] = set()
                        graph[(i-1, j)].add((i, j-1))
                    if j+1 < len(row):
                        grid[i][j+1] = "|"
                        graph[(i, j+1)] = set()
                        graph[(i-1, j)].add((i, j+1))
            elif el == "S":
                grid[i+1][j] = "|"
                graph[(i+1, j)] = set()
                root = (i+1, j)
            else:
                if 0 <= i-1 < len(grid) and grid[i-1][j] == "|":
                    grid[i][j] = "|"
                    graph[(i, j)] = set()
                    graph[(i-1, j)].add((i,j))
    
    count = count_paths(graph, root)
                
    print("Odgovor 2:", count)


if __name__ == "__main__":
    main()
