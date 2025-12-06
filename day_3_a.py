
def main():
    data = []
    with open("data/3_data.txt") as f:
        lines = f.readlines()
        for line in lines:
            data.append(line[:-1])

    count = 0
    for line in data:
        num1 = max(line[:-1])
        index = line.index(num1)
        num2 = max(line[index+1:])
        count += int(num1+num2)

    print("Odgovor 1:", count)


if __name__ == "__main__":
    main()
