import numpy as np

def find_xmas_occurences(line: np.ndarray) -> int:
    line_str: str = "".join(line)
    return line_str.count("XMAS")


def main() -> None:
    with open("stub") as file:
        input: str = file.read()

    # list2d: list[list[str]] = list()

    # for horizontal_line in input.splitlines():
    #     horizontal_list: list[str] = list(horizontal_line)
    #     list2d.append(horizontal_list)


    # for vertical_line in array.
    # print(array)
    


if __name__ == "__main__":
    main()
