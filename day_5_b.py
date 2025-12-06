
def main():
    fresh_ranges = []
    with open("data/5_data.txt") as f:
        lines = f.readlines()
        for line in lines:
            if line == "\n":
                break
            line = line.strip()
            interval = [int(i) for i in line.strip().split("-")]
            fresh_ranges.append(interval)
    
    fresh_ranges.sort(key=lambda x: x[0])
    merged_ranges = [fresh_ranges[0]]
    for r in fresh_ranges:
        last_range = merged_ranges[-1]
        if last_range[1] < r[0]:
            merged_ranges.append(r)
        else:
            merged_ranges[-1] = [last_range[0], max(r[1], last_range[1])]
    
    count = 0
    for r in merged_ranges:
        count += r[1] - r[0] + 1

    print("Odgovor 2:", count)


if __name__ == "__main__":
    main()
