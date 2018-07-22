from PriorityQueue import PriorityQueue


# функции полезности для работы с сетками
def from_id_width(id, width):
    return id % width, id // width


def draw_tile(graph, id, style, width):
    r = "."
    if 'number' in style and id in style['number']: r = "%d" % style['number'][id]
    if 'point_to' in style and style['point_to'].get(id, None) is not None:
        (x1, y1) = id
        (x2, y2) = style['point_to'][id]
        if x2 == x1 - 1: r = "<"
        if x2 == x1 + 1: r = ">"
        if y2 == y1 - 1: r = "^"
        if y2 == y1 + 1: r = "v"
    if 'path' in style and id in style['path']:
        r = "*"
    if 'start' in style and id == style['start']:
        r = "A"
    if 'finish' in style and id == style['finish']:
        r = "B"
    if id in graph.walls:
        r = "#"
    return r


def draw_grid(graph, width=2, **style):
    for y in range(graph.height):
        for x in range(graph.width):
            print("%%-%ds" % width % draw_tile(graph, (x, y), style, width), end="")
        print()


def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(graph, start, finish):
    frontier = PriorityQueue()
    frontier.put(finish, 0)
    came_from = {}
    cost_so_far = {}
    came_from[finish] = None
    cost_so_far[finish] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == start:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(start, next)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far


def reconstruct_path(came_from, start, finish):
    current = start
    path = []
    while current != finish:
        path.append(current)
        current = came_from[current]
    path.append(start)  # optional
    path.reverse()  # optional
    # path.remove(start)
    # path.remove(finish)
    return path
