import numpy as np


def main() -> None:
    with open("input") as file:
        input_string: str = file.read()

    list2d: list[list[str]] = list()

    for horizontal_line in input_string.splitlines():
        horizontal_list: list[str] = list(horizontal_line)
        list2d.append(horizontal_list)

    array = np.array(list2d)
    height, width = array.shape

    xmas_occurences: int = 0

    # Checking horizontally forwards and backwards
    for i in range(height):
        horizontal_string = "".join(array[i,:])
        xmas_occurences += horizontal_string.count("XMAS") + horizontal_string.count("SAMX")

    # Checking vertically down and up
    for i in range(width):
        vertical_string = "".join(array[:,i])
        xmas_occurences += vertical_string.count("XMAS") + vertical_string.count("SAMX")

    # Iterate over all diagonals
    for i in range(-height + 1, width - 1):
        # Checking diagonally top left to bottom right and backwards
        diagonal_string = "".join(array.diagonal(i))
        xmas_occurences += diagonal_string.count("XMAS") + diagonal_string.count("SAMX")
        
        # Checking diagonally top right to bottom left and backwards
        antidiagonal_string = "".join(np.fliplr(array).diagonal(i))
        xmas_occurences += antidiagonal_string.count("XMAS") + antidiagonal_string.count("SAMX")
        
    print(f"Total occurences of the phrase 'XMAS': {xmas_occurences}")


if __name__ == "__main__":
    main()
