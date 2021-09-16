import pygame
import time

pygame.init()
pygame.display.init()


width = 800
height = 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Игра змейка. Glo Academy")

green = (0, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)
segment_size = 20
snake_speed = 10

head_x = width // 2
head_y = height // 2

vx = 0
vy = 0

clock = pygame.time.Clock()

while True:
    if head_x < 0 or head_x > width + segment_size or head_y < 0 or head_y > height + segment_size:
        font = pygame.font.SysFont("None", 35)
        message = font.render("Вы проиграли", True, red)
        display.blit(message, [width / 2, height / 2])
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        quit()

    events = pygame.event.get()
    for event in events:
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                vy = segment_size
                vx = 0
            elif event.key == pygame.K_UP:
                vy = -segment_size
                vx = 0
            elif event.key == pygame.K_LEFT:
                vx = -segment_size
                vy = 0
            elif event.key == pygame.K_RIGHT:
                vx = segment_size
                vy = 0

    head_x += vx
    head_y += vy

    display.fill(green)
    pygame.draw.rect(display, black, [head_x, head_y, segment_size, segment_size])

    pygame.display.flip()
    clock.tick(snake_speed)
