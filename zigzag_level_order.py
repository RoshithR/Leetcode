

from collections import deque
graph = {2:[1,33],
         33:[25,40],
         25:[11],
         40:[34]}


def zigzag_traversal(graph, root):
    visited, queue = [], deque()
    flag=True
    if root not in visited:
        visited.append(root)
        queue.append(root)
        while queue:
            if flag:
                s = queue.popleft()
            else:
                s = queue.pop()
            flag = not flag
            print(s)
            if s in graph.keys():
                for neighbor in graph[s]:
                    if neighbor not in visited:
                        queue.append(neighbor)


print(zigzag_traversal(graph,2))