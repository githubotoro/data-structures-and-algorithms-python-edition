import sys
import pprint

infile = open("input.txt", "r")
outfile = open("output.txt", "w")

sys.stdin = infile
sys.stdout = outfile

pp = pprint.PrettyPrinter(depth=float("inf"))


class Solution:
    def __init__(self) -> None:
        pass

    def getEdges(self) -> list:
        edges = []

        while True:
            try:
                src_vertex, dst_vertex = input().split()
                edges.append([src_vertex, dst_vertex])
            except EOFError:
                break

        return edges

    def createAdjList(self, edges: list) -> dict:
        adj_list = {}

        for edge in edges:
            src_vertex, dst_vertex = edge

            adj_list[src_vertex] = adj_list.get(src_vertex, [])
            adj_list[dst_vertex] = adj_list.get(dst_vertex, [])

            adj_list[src_vertex].append(dst_vertex)

        return adj_list

    def bfs(self, adj_list: dict, node: int, visited: set, cycle: set) -> bool:
        if node in cycle:
            return True
        elif node in visited:
            return False

        cycle.add(node)
        neighbors = adj_list[node]

        for neighbor in neighbors:
            if self.bfs(adj_list, neighbor, visited, cycle):
                return True

        cycle.remove(node)
        visited.add(node)

        return False

    def isCyclePresent(self, adj_list: dict) -> bool:
        visited, cycle = set(), set()

        for node in adj_list.keys():
            if self.bfs(adj_list, node, visited, cycle):
                return True

        return False


def main():
    S = Solution()

    edges = S.getEdges()
    adj_list = S.createAdjList(edges)
    isCyclePresent = S.isCyclePresent(adj_list)

    print(isCyclePresent)


if __name__ == "__main__":
    main()


infile.close()
outfile.close()
