
def main():
    points = []
    with open("datas/9_data.txt") as f:
        lines = f.readlines()
        for line in lines:
            points.append([int(x) for x in line.strip().split(",")])

    max_area = 0
    for i, point1 in enumerate(points[:-1]):
        for point2 in points[i+1:]:
            area = (abs(point1[0] - point2[0]) + 1) * (abs(point1[1] - point2[1])+1)
            if area > max_area:
                max_area = area
             
    print("Odgovor 1:", max_area)


if __name__ == "__main__":
    main()
