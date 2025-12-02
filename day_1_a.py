
def main():
    data = []
    with open("day1/1_data.txt") as f:
        lines = f.readlines()
        for line in lines:
            sign = line[0]
            if sign == "R":
                data.append(int(line[1:]))
            else:
                data.append(int("-" + line[1:]))
    
    password = 50
    count = 0
    for num in data:
        password += num
        password %= 100
        if password == 0:
            count += 1

    print("Odgovor 1:", count)


if __name__ == "__main__":
    main()
