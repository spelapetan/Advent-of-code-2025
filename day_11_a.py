
def main():
    devices = dict()
    with open("datas/11_data.txt") as f:
        lines = f.readlines()
        for line in lines:
            dev_data = line.strip().split(" ")
            devices[dev_data[0][:-1]] = dev_data[1:]

    steps_to_out = dict()
    def num_of_paths(dev):
        if steps_to_out.get(dev) is not None:
            return steps_to_out[dev]

        if "out" in devices[dev]:
            return 1

        num_paths = 0
        for out_dev in devices[dev]:
            num_paths += num_of_paths(out_dev)

        steps_to_out[dev] = num_paths
        return num_paths

    paths = num_of_paths("you")

    print("Odgovor 1:", paths)


if __name__ == "__main__":
    main()
