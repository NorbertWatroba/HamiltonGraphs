class Graph:
    def __init__(self, data: list[list[bool]]):
        self.matrix = data

    def __str__(self):
        size = len(self.matrix)
        representation = ''
        # header
        representation += (f'   | {"  ".join(str(i) for i in range(1, min(size+1, 10)))}  '
                           f'{" ".join(str(i) for i in range(10, size+1))}\n')
        representation += f'---+{"---" * size}\n'
        # body
        for i in range(size):
            row = [str(int(cell)) for cell in self.matrix[i]]
            representation += f'{i + 1:2} | {"  ".join(row)}\n'
        return representation

    def hamilton_cycle(self) -> list[int]:
        pass

    def euler_cycle(self) -> list[int]:
        pass
