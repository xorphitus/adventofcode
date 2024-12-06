import sys
from collections import deque

def parse(lines):
    isDependencyPart = True
    deps = []
    pages = []
    for line in lines:
        line = line.strip()
        if isDependencyPart:
            if line == "":
                isDependencyPart = False
                continue
            before, after = line.split("|")
            deps.append([before, after])
        else:
            pages.append(line.split(","))
    return deps, pages

def makeGraph(deps):
    graph = {}
    for dep in deps:
        before, after = dep
        if before not in graph:
            graph[before] = []
        graph[before].append(after)
    return graph

def topologicalSort(graph):
    seen = set()
    order = []
    for val, nexts in graph.items():
        if val in seen:
            continue
        rec(val, graph, seen, order)

    order.reverse()
    return order

def rec(val, graph, seen, order):
    seen.add(val)
    if val in graph:
        for nxt in graph[val]:
            if nxt in seen:
                continue
            rec(nxt, graph, seen, order)

    order.append(val)

def valid(pages, orderedDeps):
    deps = {}
    for i in range(len(orderedDeps)):
        deps[orderedDeps[i]] = i

    last = -1
    for page in pages:
        idx = deps[page]
        if idx < last:
            return False
        last = idx
    return True

def exec(deps, pageSets):
    deps = makeGraph(deps)
    deps = topologicalSort(deps)
    total = 0
    for pages in pageSets:
        if valid(pages, deps):
            middle = pages[len(pages) // 2]
            total += int(middle)
    return total

# cat /path/to/input.txt | python day01.py
if __name__ == '__main__':
    deps, pageSets = parse(sys.stdin)
    answer = exec(deps, pageSets)
    print(answer)
