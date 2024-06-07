from copy import deepcopy


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
        def has_euler_cycle() -> bool:
            if not is_connected():
                return False
            for i in range(self.size):
                if vertex_degree(i) % 2 != 0:
                    return False
            return True

        def is_connected() -> bool:
            def dfs(vertex: int):
                dfs_stack = [vertex]
                while dfs_stack:
                    node = dfs_stack.pop()
                    if not visited[node]:
                        visited[node] = True
                        for i in range(self.size):
                            if self.matrix[node][i] and not visited[i] and i not in dfs_stack:
                                dfs_stack.append(i)

            visited = [False] * self.size
            start_vertex = next((i for i in range(self.size) if vertex_degree(i) > 0), -1)
            if start_vertex == -1:
                return True

            dfs(start_vertex)
            return all(visited[i] or vertex_degree(i) == 0 for i in range(self.size))

        def vertex_degree(vertex: int) -> int:
            return sum(graph[vertex])

        def get_next_edge(vertex: int) -> int:
            for i in range(self.size):
                if graph[vertex][i]:
                    return i
            return -1

        def remove_edge(f: int, t: int) -> None:
            graph[f][t] = False
            graph[t][f] = False

        graph = deepcopy(self.matrix)

        if not has_euler_cycle():
            return []

        cycle = []
        stack = []
        current_vertex = 0
        stack.append(current_vertex)

        while stack:
            if vertex_degree(current_vertex) > 0:
                if current_vertex not in stack:
                    stack.append(current_vertex)
                next_vertex = get_next_edge(current_vertex)
                remove_edge(current_vertex, next_vertex)
                current_vertex = next_vertex

            else:
                cycle.append(current_vertex)
                current_vertex = stack.pop()
        return [i+1 for i in cycle]


