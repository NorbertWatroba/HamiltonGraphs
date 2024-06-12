import random


def hamilton_data(size: int, saturation: int) -> list[list[bool]]:
    data = [[False for _ in range(size)] for _ in range(size)]

    # total amount of 3-node cycles to add after the first hamilton cycle in the graph
    additional_cycles = ((size * (size - 1) // 2) * saturation // 100) // 3

    hamilton_cycle = list(range(size))
    random.shuffle(hamilton_cycle)

    # first cycle
    previous_node = hamilton_cycle[0]
    for current_node in hamilton_cycle[1:]:
        data[previous_node][current_node] = True
        data[current_node][previous_node] = True
        previous_node = current_node
    data[hamilton_cycle[-1]][hamilton_cycle[0]] = True
    data[hamilton_cycle[0]][hamilton_cycle[-1]] = True

    # additional edges
    while additional_cycles:
        a, b, c = random.sample(hamilton_cycle, 3)
        if data[a][b] or data[b][c] or data[c][a]:
            continue
        data[a][b] = True
        data[b][a] = True
        data[b][c] = True
        data[c][b] = True
        data[c][a] = True
        data[a][c] = True
        additional_cycles -= 1

    return data
