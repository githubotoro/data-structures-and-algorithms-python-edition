class Solution:
    def dfs(
        self, adj_list: {}, node: int, visited: set, cycle: set, ordering: []
    ) -> bool:
        if node in cycle:
            return False
        elif node in visited:
            return True

        cycle.add(node)

        for neighbor in adj_list[node]:
            if not self.dfs(adj_list, neighbor, visited, cycle, ordering):
                return False

        cycle.remove(node)
        visited.add(node)
        ordering.append(node)

        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {node: [] for node in range(numCourses)}

        for row, col in prerequisites:
            adj_list[row].append(col)

        visited, cycle = set(), set()
        ordering = []

        for node in range(numCourses):
            if not self.dfs(adj_list, node, visited, cycle, ordering):
                return []

        return ordering
