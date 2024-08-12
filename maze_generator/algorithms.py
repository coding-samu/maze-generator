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