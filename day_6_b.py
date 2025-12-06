import math

def main():
    grid = []
    with open("data/6_data.txt") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if i == len(lines) - 1:
                operators = line.strip().split()
            else:
                grid.append(list(line[:-1]))
    
    count = 0
    acc = 0 if operators[-1] == "+" else 1
    for j in range(len(grid[0])-1, -1, -1):
        all_rows_are_empty = True
        column_number = ""
        for i in range(len(grid)):
            if grid[i][j] != " ":
                all_rows_are_empty = False
                column_number += grid[i][j]
        
        if all_rows_are_empty:
            operators.pop()
            count += acc
            acc = 0 if operators[-1] == "+" else 1
        else:        
            if operators[-1] == "+":
                acc += int(column_number)
            else:
                acc *= int(column_number)

        if j == 0:
            count += acc


    print("Odgovor 2:", count)


if __name__ == "__main__":
    main()
