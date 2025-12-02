
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
        step = -1 if num < 0 else 1
        for i in range(abs(num)):
            password += step
            if password % 100 == 0:
                count += 1
        password %= 100

    print("Odgovor 2:", count)


if __name__ == "__main__":
    main()
