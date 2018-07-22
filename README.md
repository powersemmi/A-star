# A * Алгоритм.

## Как его использовать?

Для начала нужно инициировать сетку:
```python
from GridWithWeights import GridWithWeights

grid = GridWithWeights(WITH, HEIGHT)
```
Координаты барьера задаются так:
```python
grid.walls = [(1, 1), (2, 1), (3, 1), (3, 3)]
```
Далее нажно задать координаты начальной и конечной точки для поиска пути:
```python
start, finish = (1, 4), (4, 0)
```
Функция a_star_search возвращает конечный путь, который получится в итоге.
```python
from functions import a_star_search

came_from = a_star_search(grid, start, finish)
print(came_from)
# output: 
# {(4, 0): None, (4, 1): (4, 0), (3, 0): (4, 0), (2, 0): (3, 0), (1, 0): (2, 0), (0, 0): (1, 0), (4, 2): (4, 1), 
# (4, 3): (4, 2), (3, 2): (4, 2), (2, 2): (3, 2), (2, 3): (2, 2), (1, 2): (2, 2), (0, 2): (1, 2), (1, 3): (1, 2), 
# (1, 4): (1, 3), (0, 3): (1, 3)}

```
Далее Функция draw_grid отрисовывает полученные данные (несколько примеров с разными стилями отрисовки):
```python
from functions import draw_grid, reconstruct_path

draw_grid(grid, width=3, point_to=came_from, start=start, finish=finish)
print()
draw_grid(grid, width=3, number=cost_so_far, start=start, finish=finish)
print()
draw_grid(grid, width=3, path=reconstruct_path(came_from, start=start, finish=finish), start=start, finish=finish)
# output:
'''
>  >  >  >  B
.  #  #  #  ^
>  >  >  >  ^
>  ^  ^  #  ^
.  A  .  .  .

4  3  2  1  B
.  #  #  #  1
6  5  4  3  2
7  6  5  #  3
.  A  .  .  .

.  .  .  .  B
.  #  #  #  *
.  *  *  *  *
.  *  .  #  .
.  A  .  .  .
''' 

```