import random

def generate_maze_dfs(width, height):
    # Inizializza il labirinto
    maze = [[0 for _ in range(width)] for _ in range(height)]
    
    # Inizializza la pila e il punto di partenza
    stack = [(0, 0)]
    maze[0][0] = 1
    
    while stack:
        x, y = stack[-1]
        neighbors = []
        
        # Aggiungi i vicini non visitati
        if x > 1 and maze[y][x - 2] == 0:
            neighbors.append((x - 2, y))
        if x < width - 2 and maze[y][x + 2] == 0:
            neighbors.append((x + 2, y))
        if y > 1 and maze[y - 2][x] == 0:
            neighbors.append((x, y - 2))
        if y < height - 2 and maze[y + 2][x] == 0:
            neighbors.append((x, y + 2))
        
        if neighbors:
            nx, ny = random.choice(neighbors)
            maze[ny][nx] = 1
            maze[(ny + y) // 2][(nx + x) // 2] = 1
            stack.append((nx, ny))
        else:
            stack.pop()
    
    return maze

def generate_maze_prim(width, height):
    # Inizializza il labirinto
    maze = [[0 for _ in range(width)] for _ in range(height)]
    walls = []
    
    # Inizializza il punto di partenza
    start_x, start_y = 0, 0
    maze[start_y][start_x] = 1
    walls.extend([(start_x, start_y, x, y) for x, y in get_neighbors(start_x, start_y, width, height)])
    
    while walls:
        x1, y1, x2, y2 = random.choice(walls)
        walls.remove((x1, y1, x2, y2))
        
        if maze[y2][x2] == 0:
            maze[y2][x2] = 1
            maze[(y1 + y2) // 2][(x1 + x2) // 2] = 1
            walls.extend([(x2, y2, nx, ny) for nx, ny in get_neighbors(x2, y2, width, height) if maze[ny][nx] == 0])
    
    return maze

def get_neighbors(x, y, width, height):
    neighbors = []
    if x > 1:
        neighbors.append((x - 2, y))
    if x < width - 2:
        neighbors.append((x + 2, y))
    if y > 1:
        neighbors.append((x, y - 2))
    if y < height - 2:
        neighbors.append((x, y + 2))
    return neighbors