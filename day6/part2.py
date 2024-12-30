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
        "West": "North"
    }

    moves: dict[str, tuple[int, int]] = {
        "North": (-1, 0),
        "East": (0, 1),
        "South": (1, 0),
        "West": (0, -1)
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

    def move2(heading: str, x: int, y: int, arr: np.ndarray) -> tuple[str, int, int]:
        dy, dx = moves[heading]
        new_x, new_y = x + dx, y + dy
        
        if new_x < 0 or new_x >= arr.shape[1] or new_y < 0 or new_y >= arr.shape[0]:
            # Finished
            raise StopIteration
        if arr[new_y, new_x] == "#":
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

    new_arrays = list()

    for y in range(array.shape[0]):
        for x in range(array.shape[1]):
            if visited_locations[y, x] == 1 and array[y, x] != STARTING_LOCATION:
                new_array = array.copy()
                new_array[y, x] = "#"
                new_arrays.append(new_array)

    n_loops = 0

    for arr in new_arrays:
        y, x = np.where(arr == STARTING_LOCATION)
        y, x = int(y[0]), int(x[0])
        heading = "North"
        visited_locations = np.zeros(arr.shape)
        visited: set[tuple[str, int, int]] = set()
        while True:
            try:
                heading, x, y = move2(heading, x, y, arr)
                if (heading, x, y) in visited:
                    n_loops += 1
                    break
                visited.add((heading, x, y))
            except StopIteration:
                break

    print(f"Number of loops: {n_loops}")
        

if __name__ == "__main__":
    main()