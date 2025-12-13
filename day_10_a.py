from itertools import product

def min_num_of_pushes(buttons, on_lights):
    combs = list(product([0, 1], repeat=len(buttons)))
    pushes = []
    n = len(on_lights)
    for combo in combs:
        comb_lights = ["."] * n
        for i, on_off in enumerate(combo):
            if on_off:
                button = buttons[i]
                for place in button:
                    if comb_lights[place] == ".":
                        comb_lights[place] = "#"
                    else:
                        comb_lights[place] = "."

        if comb_lights == on_lights:
            pushes.append(combo.count(1))

    return min(pushes)


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
    for m, on_lights in enumerate(machine_lights):
        pushes += min_num_of_pushes(machine_buttons[m], on_lights)
             
    print("Odgovor 1:", pushes)


if __name__ == "__main__":
    main()
