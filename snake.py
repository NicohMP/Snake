import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))

WHITE = (255, 255, 255)
TILE_SIZE = 25
CLOCK_FREQUENCY = 10
BACKSCREEN_COLOR = (16, 255, 34)
BODY_COLOR = (0, 0, 255)  # couleur du corps
HEAD_COLOR = (100, 100, 255)


def display(positions):
    for coord in positions[:-1]:
        rect = pygame.Rect(coord[0], coord[1], TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, BODY_COLOR, rect)
    head = pygame.Rect(positions[-1][0], positions[-1][1], TILE_SIZE, TILE_SIZE)
    pygame.draw.rect(screen, HEAD_COLOR, head)


def movement(orientation):
    if orientation == "up":
        new_head = (positions[-1][0], positions[-1][1] - TILE_SIZE)
    if orientation == "down":
        new_head = (positions[-1][0], positions[-1][1] + TILE_SIZE)
    if orientation == "right":
        new_head = (positions[-1][0] + TILE_SIZE, positions[-1][1])
    if orientation == "left":
        new_head = (positions[-1][0] - TILE_SIZE, positions[-1][1])
    positions.append(new_head)
    positions.pop(0)
    display(positions)


positions = [
    (10 * TILE_SIZE, 10 * TILE_SIZE),
    (10 * TILE_SIZE, 11 * TILE_SIZE),
    (10 * TILE_SIZE, 12 * TILE_SIZE),
]

orientation = "up"
while True:
    clock.tick(CLOCK_FREQUENCY)
    screen.fill(BACKSCREEN_COLOR)

    for i in range(0, 500, TILE_SIZE):
        for j in range(i, 500 + i, 2 * TILE_SIZE):
            TILE = pygame.Rect(i, j % 500, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, WHITE, TILE)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pygame.quit()
            elif event.key == pygame.K_z:
                orientation = "up"
            elif event.key == pygame.K_s:
                orientation = "down"
            elif event.key == pygame.K_q:
                orientation = "left"
            elif event.key == pygame.K_d:
                orientation = "right"

    pygame.display.set_caption("Jeu Python")

    movement(orientation)
    pygame.display.update()

    pygame.display.flip()
