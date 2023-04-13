import pygame
import sys
import os

pygame.init()

WIDTH, HEIGHT = 640, 480
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def drawLineBetween(screen, element1, element2):
    start, color, mode, width = element1
    end = element2[0]

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    if mode == 0:
        for i in range(iterations):
            progress = 1.0 * i / iterations
            aprogress = 1 - progress
            x = int(aprogress * start[0] + progress * end[0])
            y = int(aprogress * start[1] + progress * end[1])
            pygame.draw.circle(screen, color, (x, y), width)

    elif mode == 2:
        drawCircleBetween(screen, element1, element2)  # to keep old drawings unchanged
    elif mode == 1:
        drawRectBetween(screen, element1, element2)


def drawRectBetween(screen, element1, element2):
    start, color, mode, width = element1
    end = element2[0]

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    if mode == 1:
        for i in range(iterations):
            if i % 7 == 0:
                progress = 4.0 * i / iterations
                aprogress = 1 - progress
                x = int(aprogress * start[0] + progress * end[0])
                y = int(aprogress * start[1] + progress * end[1])
                pygame.draw.rect(screen, color, pygame.rect.Rect(x, y, width, width), width // 9)

    elif mode == 2:
        drawCircleBetween(screen, element1, element2)  # to keep old drawings unchanged
    elif mode == 0:
        drawLineBetween(screen, element1, element2)


def drawCircleBetween(screen, element1, element2):
    start, color, mode, radius = element1
    end = element2[0]

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    if mode == 2:
        for i in range(iterations):
            if i % 7 == 0:
                progress = 4.0 * i / iterations
                aprogress = 1 - progress
                x = int(aprogress * start[0] + progress * end[0])
                y = int(aprogress * start[1] + progress * end[1])
                pygame.draw.circle(screen, color, (x, y), radius, radius // 9)

    elif mode == 1:
        drawRectBetween(screen, element1, element2)  # to keep old drawings unchanged
    elif mode == 0:
        drawLineBetween(screen, element1, element2)


def main():
    radius = 15
    points = []
    color_mode = BLUE
    draw_object = 0  # 0 - line, 1 - rect, 2 - circle
    running = True

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                points = points + [(position, color_mode, draw_object, radius)]
                # keeping all states of every element in one tuple so that changing states won't affect already drawn objects

        # draw all points
        if draw_object == 0:
            i = 0
            while i < len(points) - 1:
                drawLineBetween(screen, points[i], points[i + 1])
                i += 1

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
