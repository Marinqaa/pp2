"""Draw circle - a red ball of size 50 x 50
(radius = 25) on white background.
When user presses Up, Down, Left,Right
arrow keys on keyboard, the ball
should move by 20 pixels in the direction
of pressed key. The ball should not leave the screen,
i.e. user input that leads the ball
to leave of the screen should be ignored"""
import pygame


pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Moving Ball")

ball_color = (255, 0, 0)
ball_radius = 25
ball_position = [200, 200]

def draw_ball():
    pygame.draw.circle(screen, ball_color, ball_position, ball_radius)

def handle_keys():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ball_position[1] -= 20
        if ball_position[1] < ball_radius:
            ball_position[1] = ball_radius
    if keys[pygame.K_DOWN]:
        ball_position[1] += 20
        if ball_position[1] > 400 - ball_radius:
            ball_position[1] = 400 - ball_radius
    if keys[pygame.K_LEFT]:
        ball_position[0] -= 20
        if ball_position[0] < ball_radius:
            ball_position[0] = ball_radius
    if keys[pygame.K_RIGHT]:
        ball_position[0] += 20
        if ball_position[0] > 400 - ball_radius:
            ball_position[0] = 400 - ball_radius


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    handle_keys()
    screen.fill((255, 255, 255))
    draw_ball()
    pygame.display.flip()
    clock.tick(24)

pygame.quit()