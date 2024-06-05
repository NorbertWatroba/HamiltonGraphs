from creators import hamilton_data


def non_hamilton_data(nodes: int) -> list[list[bool]]:
    data = hamilton_data(nodes, 50)
    for vertice in data[0:-1]:
        vertice[-1] = False
    data[-1] = [False for _ in range(nodes)]
    return data
