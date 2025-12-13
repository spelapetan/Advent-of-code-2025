import numpy as np
import pulp

def min_num_of_pushes(matrix_A, joltages):
    prob = pulp.LpProblem("button_pushes", pulp.LpMinimize)

    n = matrix_A.shape[1]
    buttons = [pulp.LpVariable(f"b{i}", lowBound=0, cat="Integer") for i in range(n)]

    # constraints: Ax = b
    for i in range(matrix_A.shape[0]):
        prob += pulp.lpSum(matrix_A[i,j]*buttons[j] for j in range(n)) == joltages[i]

    # minimize sum of button pushes
    prob += pulp.lpSum(buttons)

    prob.solve(pulp.PULP_CBC_CMD(msg=False)) # disable stats
    return sum([int(bi.value()) for bi in buttons])


def main():
    machine_lights = []
    machine_buttons = []
    machine_joltages = []
    with open("datas/10_data.txt") as f:
        lines = f.readlines()
        for line in lines:
            els = line.strip().split(" ")
            machine_lights.append(list(els[0][1:-1]))
            machine_joltages.append([int(x) for x in els[-1][1:-1].split(",")])
            buttons = []
            for button in els[1:-1]:
                buttons.append([int(x) for x in button[1:-1].split(",")])
            machine_buttons.append(buttons)

    pushes = 0
    for m, joltages in enumerate(machine_joltages):
        buttons = machine_buttons[m]
        matrix_A = [[0] * len(buttons) for _ in range(len(joltages))]
        for i, button in enumerate(buttons):
            for el in button:
                matrix_A[el][i] = 1

        pushes += min_num_of_pushes(np.array(matrix_A), np.array(joltages))
             
    print("Odgovor 2:", pushes)


if __name__ == "__main__":
    main()
