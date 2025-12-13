
def main():
    devices = dict()
    with open("datas/11_data.txt") as f:
        lines = f.readlines()
        for line in lines:
            dev_data = line.strip().split(" ")
            devices[dev_data[0][:-1]] = dev_data[1:]

    steps_to_out = dict()
    def num_of_paths(dev, seen_fft, seen_dac):
        if steps_to_out.get((dev, seen_fft, seen_dac)) is not None:
            return steps_to_out[(dev, seen_fft, seen_dac)]

        if dev == "fft":
            seen_fft = True
        elif dev == "dac":
            seen_dac = True

        if "out" in devices[dev]:
            return 1 if seen_fft and seen_dac else 0

        num_paths = 0
        for out_dev in devices[dev]:
            num_paths += num_of_paths(out_dev, seen_fft, seen_dac)

        steps_to_out[(dev, seen_fft, seen_dac)] = num_paths
        return num_paths

    paths = num_of_paths("svr", False, False)

    print("Odgovor 2:", paths)


if __name__ == "__main__":
    main()
