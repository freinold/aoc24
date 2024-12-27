import numpy as np

STARTING_LOCATION: str = "^"

def main() -> None:
    with open("stub") as file:
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

    

    def move(heading: str, x: int, y: int):


    while True:
        match heading:
            case "North":
                if array[y - 1, x] == "#":
                    heading == "East"
                else:
                    y -= 1
                    visited_locations[y, x] == 1
            case "East":
                if array[y, x + 1] == "#":
                    heading == "South"
                else:
                    x += 1
                    visited_locations[y, x] == 1
            case "South":
                if array[y + 1, x] == "#":
                    heading == "West"
                else:
                    y += 1
                    visited_locations[y, x] == 1
            case "West":
                if array[y, x - 1] == "#":
                    heading == "North"
                else:
                    x -= 1
                    visited_locations[y, x] == 1
        

if __name__ == "__main__":
    main()