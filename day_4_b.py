
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
    with open("data/4_data.txt") as f:
        lines = f.readlines()
        data = [list(line.strip()) for line in lines]

    counts = []
    rows = len(data)
    columns = len(data[0])
    while True:
        round_count = 0
        for i, row in enumerate(data):
            for j, column in enumerate(row):
                if column == "@" and can_be_taken(i, j, data, rows, columns):
                    round_count += 1
                    data[i][j] = "x"
        if round_count == 0:
            break
        counts.append(round_count)
    
    print("Odgovor 2:", sum(counts))


if __name__ == "__main__":
    main()
