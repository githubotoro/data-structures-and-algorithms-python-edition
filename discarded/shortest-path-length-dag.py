import sys
import json
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
                src_vertex, dst_vertex, wt = input().split()
                edges.append([src_vertex, dst_vertex, wt])
            except EOFError:
                break

        return edges

    def createAdjList(self, edges: list) -> tuple[int, dict]:
        adj_list = {}
        vertex_set = set()
        vertices = 0

        for edge in edges:
            src_vertex, dst_vertex, wt = edge

            adj_list[src_vertex] = adj_list.get(src_vertex, [])

            if src_vertex not in vertex_set:
                vertices += 1
                vertex_set.add(src_vertex)

            if dst_vertex not in vertex_set:
                vertices += 1
                vertex_set.add(dst_vertex)

            adj_list[src_vertex].append([dst_vertex, int(wt)])

        return vertices, adj_list

    def findPathLength(
        self, vertices: int, adj_list: dict, start: str, end: str
    ) -> int:
        shortest_dist = {}

        vertex_list = []
        vertex_set = set()

        vertex_list.append(start)
        vertex_set.add(start)
        shortest_dist[start] = 0

        for vertex in adj_list:
            if vertex not in vertex_set:
                vertex_list.append(vertex)
                vertex_set.add(vertex)

        for vertex in vertex_list:
            neighbors = adj_list[vertex]
            dst_till_here = shortest_dist[vertex]

            for neighbor in neighbors:
                dst_vertex, wt = neighbor

                curr_dst = shortest_dist.get(dst_vertex, float("inf"))
                shortest_dist[dst_vertex] = min(dst_till_here + wt, curr_dst)

        return shortest_dist[end]


def main():
    S = Solution()

    edges = S.getEdges()
    vertices, adj_list = S.createAdjList(edges)

    shortest_dst = S.findPathLength(vertices, adj_list, "A", "H")

    print(shortest_dst)


if __name__ == "__main__":
    main()


infile.close()
outfile.close()
