import sys
import heapq

INF = sys.maxsize


def main():
    n, m, x = map(int, sys.stdin.readline().split())
    graph = {i + 1: {} for i in range(n)}  # 원래 그래프 -> 돌아갈 때의 최단 경로 알 수 있음.
    reverse_graph = {i + 1: {} for i in range(n)}  # 뒤집힌 그래프 -> 각 노드에서 목적지까지의 최단 경로 알 수 있음.
    make_graph(graph, reverse_graph, m)
    root = dijkstra(graph, x)
    reverse_root = dijkstra(reverse_graph, x)
    result = [root[i + 1] + reverse_root[i + 1] for i in range(n)]
    print(max(result))


def make_graph(graph, reverse_graph, m):
    for i in range(m):
        x1, x2, x3 = map(int, sys.stdin.readline().split())
        graph[x1][x2] = x3
        reverse_graph[x2][x1] = x3


def dijkstra(graph, target):
    d = {n: INF for n in graph}
    d[target] = 0
    queue = []
    heapq.heappush(queue, [d[target], target])
    while queue:
        distance, node = heapq.heappop(queue)
        if d[node] < distance:
            continue
        for next_node, weight in graph[node].items():
            total_distance = distance + weight
            if total_distance < d[next_node]:
                d[next_node] = total_distance
                heapq.heappush(queue, [total_distance, next_node])
    return d


main()