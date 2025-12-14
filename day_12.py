A = [
["#", "#", "#"],
["#", ".", "#"],
["#", ".", "#"],
]

B = [
["#", "#", "#"],
[".", "#", "."],
["#", "#", "#"],
]

C = [
["#", "#", "#"],
["#", "#", "."],
["#", ".", "."],
]

D = [
["#", "#", "."],
[".", "#", "#"],
[".", ".", "#"],
]

E = [
["#", ".", "#"],
["#", "#", "#"],
["#", "#", "."],
]

F = [
[".", ".", "#"],
["#", "#", "#"],
["#", "#", "#"],
]


def main():
    shape_types = [A, B, C, D, E, F]
    dimensions = []
    presentes = []
    with open("datas/12_data.txt") as f:
        lines = f.readlines()
        for line in lines[30:]:
            els = line.strip().split(" ")
            dimensions.append([int(x) for x in els[0][:-1].split("x")])
            presentes.append([int(e) for e in els[1:]])

    present_sizes = []
    for shape_type in shape_types:
        present_sizes.append(sum(row.count('#') for row in shape_type))

    count = 0
    for i, region in enumerate(dimensions):
        area = region[0] * region[1]
        num_of_presents = presentes[i]
        min_area = 0
        for j, num in enumerate(num_of_presents):
            min_area += num * present_sizes[j]
        if min_area < area:
            count += 1

    print("Odgovor 1:", count)


if __name__ == "__main__":
    main()
