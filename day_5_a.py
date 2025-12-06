
def main():
    fresh = []
    ids = []
    with open("data/5_data.txt") as f:
        lines = f.readlines()
        second_part = False
        for line in lines:
            if line == "\n":
                second_part = True
                continue
            line = line.strip()
            if not second_part:
                interval = [int(i) for i in line.strip().split("-")]
                fresh.append(interval)
                # for i in range(interval[0], interval[1]+1):
                #     if i not in fresh:
                #         fresh.append(i)
            else:
                ids.append(int(line.strip()))
                

    # count = sum(list(set(fresh) & set(ids)))
    count = 0
    for id in ids:
        for r in fresh:
            if r[0] <= id <= r[1]:
                count += 1
                break

    print("Odgovor 1:", count)


if __name__ == "__main__":
    main()
