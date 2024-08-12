import unittest
from algorithms import generate_maze_dfs, generate_maze_prim

class TestMazeGeneration(unittest.TestCase):
    def test_maze_dfs_size(self):
        width, height = 10, 10
        maze = generate_maze_dfs(width, height)
        self.assertEqual(len(maze), height)
        self.assertTrue(all(len(row) == width for row in maze))

    def test_maze_dfs_no_walls(self):
        width, height = 10, 10
        maze = generate_maze_dfs(width, height)
        self.assertTrue(any(cell == 1 for row in maze for cell in row))
        self.assertTrue(any(cell == 0 for row in maze for cell in row))

    def test_maze_prim_size(self):
        width, height = 10, 10
        maze = generate_maze_prim(width, height)
        self.assertEqual(len(maze), height)
        self.assertTrue(all(len(row) == width for row in maze))

    def test_maze_prim_no_walls(self):
        width, height = 10, 10
        maze = generate_maze_prim(width, height)
        self.assertTrue(any(cell == 1 for row in maze for cell in row))
        self.assertTrue(any(cell == 0 for row in maze for cell in row))

    def test_maze_dimensions(self):
        # Test per dimensioni variabili
        for width, height in [(5, 5), (20, 15), (100, 50)]:
            with self.subTest(width=width, height=height):
                maze_dfs = generate_maze_dfs(width, height)
                maze_prim = generate_maze_prim(width, height)
                self.assertEqual(len(maze_dfs), height)
                self.assertEqual(len(maze_prim), height)
                self.assertTrue(all(len(row) == width for row in maze_dfs))
                self.assertTrue(all(len(row) == width for row in maze_prim))

if __name__ == '__main__':
    unittest.main()
