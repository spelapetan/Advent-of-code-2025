
def main():
    points: list[list[int]] = []
    with open("datas/9_data.txt") as f:
        vertical_lines = f.readlines()
        for line in vertical_lines:
            points.append([int(x) for x in line.strip().split(",")])

    vertical_lines = dict()
    for i in range(len(points)):
        px1, py1 = points[i-1] if i != 0 else points[-1]
        px2, py2 = points[i]
        
        x1 = min(px1, px2)
        x2 = max(px1, px2)
        y1 = min(py1, py2)
        y2 = max(py1, py2)
        for y in range(y1, y2+1):
            if vertical_lines.get(y) is None:
                vertical_lines[y] = [x1, x2]
            else:
                a, b = vertical_lines[y]
                vertical_lines[y] = [min(x1, a), max(x2, b)]

    def check_area(px1, py1, px2, py2):   
        x1 = min(px1, px2)
        x2 = max(px1, px2)
        y1 = min(py1, py2)
        y2 = max(py1, py2)
        for y in range(y1, y2+1):
            if vertical_lines.get(y) is None:
                return False
            a, b = vertical_lines[y]
            if x1 < a or x1 > b or x2 < a or x2 > b:
                return False
        return True

    max_area = 0
    for i, point in enumerate(points):
        x1, y1 = point
        for point2 in points[i+1:]:
            x2, y2 = point2
            if x1 != x2 and y1 != y2 and check_area(x1, y1, x2, y2):
                area = (abs(x1 - x2) + 1) * (abs(y1 - y2)+1)
                if area > max_area:
                    max_area = area
    
    print("Odgovor 2:", max_area)


if __name__ == "__main__":
    main()
