
def main():
    data = []
    with open("day3/3_data.txt") as f:
        lines = f.readlines()
        for line in lines:
            data.append(line.strip())

    count = 0
    for line in data:
        joltage = ""
        last_index = 0
        for i in range(11,-1, -1):
            if i == 0:
                num = max(line[last_index:])
                last_index += line[last_index:].index(num) + 1
            else:
                num = max(line[last_index:-i])
                last_index += line[last_index:-i].index(num) + 1
            joltage += num
        count += int(joltage)

    print("Odgovor 2:", count)


if __name__ == "__main__":
    main()
