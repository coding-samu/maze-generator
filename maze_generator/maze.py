import argparse
import os
from algorithms import generate_maze_dfs, generate_maze_prim

def print_maze(maze):
    for row in maze:
        print(''.join(['#' if cell else ' ' for cell in row]))

def save_maze(maze, filename):
    with open(filename, 'w') as f:
        for row in maze:
            f.write(''.join(['#' if cell else ' ' for cell in row]) + '\n')

def main():
    parser = argparse.ArgumentParser(description='Generatore di Labirinti')
    parser.add_argument('--width', type=int, default=10, help='Larghezza del labirinto')
    parser.add_argument('--height', type=int, default=10, help='Altezza del labirinto')
    parser.add_argument('--algorithm', choices=['dfs', 'prim'], default='dfs', help='Algoritmo da usare')
    parser.add_argument('--output', type=str, help='File di output per salvare il labirinto')
    args = parser.parse_args()
    
    if args.algorithm == 'dfs':
        maze = generate_maze_dfs(args.width, args.height)
    else:
        maze = generate_maze_prim(args.width, args.height)
    
    print_maze(maze)
    
    if args.output:
        save_maze(maze, args.output)

if __name__ == '__main__':
    main()
