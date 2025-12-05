
positions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1,1)]

def can_be_taken(i, j, data, num_rows, num_cols):
    count = 0
    for pos in positions:
        r = i + pos[0]
        c = j + pos[1]
        if 0 <= r < num_rows and 0<= c < num_cols:
            is_roll = data[r][c] == "@"
            if is_roll:
                count += 1
                if count >= 4:
                    return False
    return True

def main():
    data = []
    with open("day4/4_data.txt") as f:
        lines = f.readlines()
        for line in lines:
            data.append(line.strip())

    count = 0
    rows = len(data)
    columns = len(data[0])
    for i, row in enumerate(data):
        for j, column in enumerate(row):
            if column == "@":
                count += 1 if can_be_taken(i, j, data, rows, columns) else 0

    print("Odgovor 1:", count)


if __name__ == "__main__":
    main()
