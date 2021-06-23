graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}
#
# visited = [] # List to keep track of visited nodes.
# queue = []     #Initialize a queue
#
# def bfs(visited, graph, node):
#   visited.append(node)
#   queue.append(node)
#
#   while queue:
#     s = queue.pop(0)
#     print (s, end = " ")
#
#     for neighbour in graph[s]:
#       if neighbour not in visited:
#         visited.append(neighbour)
#         queue.append(neighbour)

# Driver Code
import heapq
def bfs(graph, node):
    visited, queue = [],[]
    visited.append(node)
    queue.append(node)
    # heapq.heapify(queue)
    while queue:
        s = queue.pop(0)
        # s = heapq.heappop(queue)
        print(s,end=" ")
        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                # heapq.heappush(queue,neighbor)
                queue.append(neighbor)

bfs(graph, 'A')