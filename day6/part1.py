import numpy as np

STARTING_LOCATION: str = "^"


def main() -> None:
    with open("input") as file:
        input_string: str = file.read()

    list2d: list[list[str]] = list()

    for horizontal_line in input_string.splitlines():
        horizontal_list: list[str] = list(horizontal_line)
        list2d.append(horizontal_list)

    array = np.array(list2d)
    visited_locations = np.zeros(array.shape)
    y, x = np.where(array == STARTING_LOCATION)
    y, x = int(y[0]), int(x[0])
    visited_locations[y, x] = 1
    heading = "North"

    turns: dict[str, str] = {
        "North": "East",
        "East": "South",
        "South": "West",
        "West": "North",
    }

    moves: dict[str, tuple[int, int]] = {
        "North": (-1, 0),
        "East": (0, 1),
        "South": (1, 0),
        "West": (0, -1),
    }

    def move(heading: str, x: int, y: int) -> tuple[str, int, int]:
        dy, dx = moves[heading]
        new_x, new_y = x + dx, y + dy

        if new_x < 0 or new_x >= array.shape[1] or new_y < 0 or new_y >= array.shape[0]:
            # Finished
            raise StopIteration
        if array[new_y, new_x] == "#":
            # Turn right
            heading = turns[heading]
        else:
            # Move forward
            x, y = new_x, new_y
            visited_locations[y, x] = 1

        return heading, x, y

    while True:
        try:
            heading, x, y = move(heading, x, y)
        except StopIteration:
            break

    print(f"Visited locations: {visited_locations.sum():.0f}")


if __name__ == "__main__":
    main()
