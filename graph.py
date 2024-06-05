class Graph:
    def __init__(self, data: list[list[bool]]):
        self.matrix = data
        self.size = len(data)

    def __str__(self):
        representation = ''
        # header
        representation += (f'   | {"  ".join(str(i) for i in range(1, min(self.size+1, 10)))}  '
                           f'{" ".join(str(i) for i in range(10, self.size+1))}\n')
        representation += f'---+{"---" * self.size}\n'
        # body
        for i in range(self.size):
            row = [str(int(cell)) for cell in self.matrix[i]]
            representation += f'{i + 1:2} | {"  ".join(row)}\n'
        return representation

    def hamilton_cycle(self) -> list[int]:
        def _hamilton_cycle_util(path: list[int], pos: int) -> bool:
            if pos == self.size:
                if self.matrix[path[pos - 1]][path[0]] == 1:
                    return True
                else:
                    return False

            for value in range(1, self.size):
                if _is_safe(value, path, pos):
                    path[pos] = value

                    if _hamilton_cycle_util(path, pos + 1):
                        return True

                    # Backtrack
                    path[pos] = -1
            return False

        def _is_safe(value: int, path: list[int], pos: int) -> bool:
            # Check if this vertex is an adjacent vertex of the previously added vertex
            if self.matrix[path[pos - 1]][value] == 0:
                return False

            if value in path:
                return False
            return True

        cycle = [-1] * self.size
        cycle[0] = 0
        if not _hamilton_cycle_util(cycle, 1):
            return []

        cycle.append(0)
        return [x+1 for x in cycle]

    def euler_cycle(self) -> list[int]:
        pass
