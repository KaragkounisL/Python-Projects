import pygame
import numpy as np

pygame.init()

# Define colors
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)

# Screen dimensions
WIDTH, HEIGHT = 900, 900

# Size of each cell
CELL_SIZE = 5

# Number of cells in the grid
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# Frames per second
FPS = 5

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

def generate_random_initial_state():
    """Generate a random initial state."""
    return np.random.choice([0, 1], size=(GRID_WIDTH, GRID_HEIGHT), p=[0.7, 0.3])

def draw_grid(grid):
    """Draw the grid based on the current state."""
    screen.fill(WHITE)
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if grid[x, y] == 1:
                pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else:
                pygame.draw.rect(screen, GREY, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

def update_grid(grid):
    """Update the grid based on Conway's rules."""
    new_grid = np.copy(grid)
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            neighbors = grid[max(0, x - 1):min(x + 2, GRID_WIDTH), max(0, y - 1):min(y + 2, GRID_HEIGHT)]
            num_neighbors = np.sum(neighbors) - grid[x, y]
            if grid[x, y] == 1 and (num_neighbors < 2 or num_neighbors > 3):
                new_grid[x, y] = 0
            elif grid[x, y] == 0 and num_neighbors == 3:
                new_grid[x, y] = 1
    return new_grid

def main():
    """Main function to run the simulation."""
    running = True
    playing = False
    grid = generate_random_initial_state()

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Space key pauses the simulation
                if event.key == pygame.K_SPACE:
                    playing = not playing
                # R key sets a new random state     
                elif event.key == pygame.K_r:
                    grid = generate_random_initial_state()
                    playing = False

        if playing:
            grid = update_grid(grid)

        draw_grid(grid)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()