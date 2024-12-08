import sys
from collections import defaultdict

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
            pre, post = line.split("|")
            deps.append([pre, post])
        else:
            pages.append(line.split(","))
    return deps, pages

def makeGraph(deps, pages):
    pageSet = set()
    for page in pages:
        pageSet.add(page)

    graph = defaultdict(list)
    for pre, post in deps:
        if pre in pageSet and post in pageSet:
            graph[pre].append(post)
    return graph

def topologicalSort(graph):
    indigree = defaultdict(int)
    for pre, posts in graph.items():
        if pre not in indigree:
            indigree[pre] = 0
        for post in posts:
            indigree[post] += 1

    sorted = []
    while len(indigree) > 0:
        group = set()
        for page, count in indigree.items():
            if count > 0:
                continue
            group.add(page)
        sorted.append(group)
        for page in group:
            for post in graph[page]:
                indigree[post] -= 1
            del indigree[page]

    return sorted

def valid(pages, orderedDeps):
    idx = 0
    for page in pages:
        found = False
        while idx < len(orderedDeps):
            layer = orderedDeps[idx]
            if page in layer:
                found = True
                break
            idx += 1
        if not found:
            return False
    return True

def exec(deps, pageSets):
    total = 0
    for pages in pageSets:
        graph = makeGraph(deps, pages)
        sortedDeps = topologicalSort(graph)
        if valid(pages, sortedDeps):
            middle = pages[len(pages) // 2]
            total += int(middle)
    return total

# cat /path/to/input.txt | python day01.py
if __name__ == '__main__':
    deps, pageSets = parse(sys.stdin)
    answer = exec(deps, pageSets)
    print(answer)
