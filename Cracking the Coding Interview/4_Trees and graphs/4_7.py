# Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of projects,
# where the second project is dependent on the first project).
# All of a project's dependencies must be built before the project is.
# Find a build order that will allow the projects to be built. If there is no valid build order, return an error.

from collections import defaultdict

def topologicalSort(graph, v, visit, stack):
    visit.add(v)
    for node in graph[v]:
        if node not in visit:
            topologicalSort(graph, node, visit, stack)

    stack.append(v)


def BuildOrder(projects, dependencies):

    numProjects = len(projects)

    if numProjects == 0 or len(dependencies) == 0:
        return True

    stack = []
    graph = defaultdict(list)
    visit = set()

    for project in projects:    # makes sense to add all projects as not all of them may have dependencies
        graph[project]

    # initialize graph as dict{project : all dependant projects}
    for edge in dependencies:
        graph[edge[0]].append(edge[1])

    for node in graph:
        if node not in visit:
            topologicalSort(graph, node, visit, stack)

    return stack[::-1]


if __name__ == "__main__":
    #projects = ['a', 'b', 'c', 'd', 'e', 'f']
    #dependencies = [['a', 'd'], ['f', 'b'], ['b', 'd'], ['f', 'a'], ['d', 'c']]

    projects = [1, 2, 3, 4, 5, 6]
    dependencies = [[1, 4], [6, 2], [2, 4], [6, 1], [4, 3]]
    print(BuildOrder(projects, dependencies))
