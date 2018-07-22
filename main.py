from functions import draw_grid, a_star_search, reconstruct_path
from GridWithWeights import GridWithWeights

if __name__ == "__main__" or "__android__":
    grid = GridWithWeights(5, 5)
    grid.walls = [(1, 1), (2, 1), (3, 1), (3, 3)]

    start, finish = (1, 4), (4, 0)
    came_from, cost_so_far = a_star_search(grid, start, finish)
    # draw_grid(grid, width=2, point_to=came_from, start=start, finish=finish)
    # print()
    # draw_grid(grid, width=2, number=cost_so_far, start=start, finish=finish)
    # print()
    draw_grid(grid, width=3, path=reconstruct_path(came_from, start=start, finish=finish), start=start, finish=finish)
