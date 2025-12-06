import math

def main():
    grid = []
    operators = []
    with open("data/6_data.txt") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split()
            i = 0
            for el in line:
                if el not in ["+", "*"]:
                    if i >= len(grid):
                        grid.append([int(el)])
                    else:
                        grid[i].append(int(el))
                    i += 1
                else:
                    operators.append(el)
    
    count = 0
    for i, row in enumerate(grid):
        if operators[i] == "+":
            count += sum(row)
        else:
            count += math.prod(row)

    print("Odgovor 1:", count)


if __name__ == "__main__":
    main()
