
import math


def get_divisors(n: int):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


def check_symmetry(num: str):
    num_len = len(num)
    divisors = get_divisors(num_len)
    for symmetry_len in divisors:
        if symmetry_len == num_len:
            continue
        seq = num[:symmetry_len]
        repeat = num_len // symmetry_len
        if seq * repeat == num:
            return True
    return False


def main():
    ranges = []
    with open("data/2_data.txt") as f:
        lines = f.readlines()
        data = lines[0].split(",")
        for r in data:
            ranges.append(list(map(int, r.split('-'))))
    
    results = {}
    count = 0
    for r in ranges:
        for i in range(r[0], r[1]+1):
            is_sym = results.get(i)
            if is_sym is None:
                is_sym = check_symmetry(str(i))
                results[i] = is_sym
            if is_sym:
                count += i

    print("Odgovor 1: ", count)


if __name__ == "__main__":
    main()