class Solution:
    def dfs(self, adj_list: dict, node: int, visited: set, cycle: set) -> bool:
        if node in cycle:
            return False
        elif node in visited:
            return True

        cycle.add(node)

        for neighbor in adj_list[node]:
            if not self.dfs(adj_list, neighbor, visited, cycle):
                return False

        cycle.remove(node)
        visited.add(node)

        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {node: [] for node in range(0, numCourses)}

        for row, col in prerequisites:
            adj_list[row].append(col)

        visited, cycle = set(), set()

        for node in range(0, numCourses):
            if not self.dfs(adj_list, node, visited, cycle):
                return False

        return True
