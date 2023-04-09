import pygame
import sys
pygame.init()

width = 500
height = 500
screen = pygame.display.set_mode((width, height))
surface = pygame.Surface((width, height), pygame.SRCALPHA)
pygame.display.set_caption("Marina's player")
playlist = pygame.image.load("C:\\Users\\nurma\\Downloads\\pp2\\labs\\lab7\\playlist.jpg")

def draw(screen):
    body_rect = playlist.get_rect(center=(width / 2, height / 2.5))
    screen.blit(playlist, body_rect)

clock = pygame.time.Clock()
musics = ["instasamka1.mp3", "instasamka2.mp3", "instasamka3.mp3", "instasamka4.mp3"]
a = 0
l = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()




    pressed = pygame.key.get_pressed()
    print(a)
    if pressed[pygame.K_LEFT]:
        if a != 0:
            a -=1

        pygame.mixer.music.load(musics[a])
        pygame.mixer.music.play()
    if pressed[pygame.K_RIGHT]:
        if a != len(musics)-1:
            a +=1
        pygame.mixer.music.load(musics[a])
        pygame.mixer.music.play()
    draw(screen)
    pygame.display.flip()
    clock.tick(5)
