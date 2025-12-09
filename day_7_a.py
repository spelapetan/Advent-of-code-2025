
def main():
    grid = []
    with open("datas/7_data.txt") as f:
        lines = f.readlines()
        for line in lines:
            grid.append(list(line.strip()))
    
    count = 0
    for i, row in enumerate(grid):
        for j, el in enumerate(row):
            if el == "^":
                is_split = False
                if 0 <= i-1 < len(grid) and grid[i-1][j] == "|":
                    if 0 <= j-1:
                        grid[i][j-1] = "|"
                        is_split = True
                    if j+1 < len(row):
                        grid[i][j+1] = "|"
                        is_split = True
                
                if is_split:
                    count += 1
            elif el == "S":
                grid[i+1][j] = "|"
            else:
                if 0 <= i-1 < len(grid) and grid[i-1][j] == "|":
                    grid[i][j] = "|"
                
    print("Odgovor 1:", count)


if __name__ == "__main__":
    main()
