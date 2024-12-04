import numpy as np
from numpy.lib.stride_tricks import sliding_window_view


def is_mas(string: str) -> bool:
    return string == "MAS" or string == "SAM"


def main() -> None:
    with open("input") as file:
        input_string: str = file.read()

    list2d: list[list[str]] = list()

    for horizontal_line in input_string.splitlines():
        horizontal_list: list[str] = list(horizontal_line)
        list2d.append(horizontal_list)

    array = np.array(list2d)
    window = (3, 3)
    sliding_window = sliding_window_view(array, window)
    height, width = sliding_window.shape[:2]
    xmas_occurences: int = 0

    for i in range(height):
        for j in range(width):
            window: np.ndarray = sliding_window[i, j]
            diagonal_string = "".join(window.diagonal())
            antidiagonal_string = "".join(np.fliplr(window).diagonal())
            if is_mas(diagonal_string) and is_mas(antidiagonal_string):
                xmas_occurences += 1

    print(f"Total occurences X-MAS pattern: {xmas_occurences}")


if __name__ == "__main__":
    main()
