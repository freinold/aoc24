import numpy as np

def main() -> None:
    with open("stub") as file:
        input_string: str = file.read()

    list2d: list[list[str]] = list()

    for horizontal_line in input_string.splitlines():
        horizontal_list: list[str] = list(horizontal_line)
        list2d.append(horizontal_list)

    array = np.array(list2d)
    visited_locations = np.zeros(array.shape)
    print(array)
    print(visited_locations)

if __name__ == "__main__":
    main()