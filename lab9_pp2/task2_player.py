import pygame 
import os
import sys

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Ganeka's favorite songs)")
"""photo=pygame.image.load('/Users/ganiya/Downloads/Unknown.jpg').convert_alpha()"""
purpur = (255, 0, 255)
black = (0, 0, 0)
font=pygame.font.SysFont(None, 40)
lybrary = ['/Users/ganiya/lab/lab9_pp2/Liz Callaway - Once upon a December.mp3', 
           '/Users/ganiya/lab/lab9_pp2/Abba - Dancing queen.mp3', 
           '/Users/ganiya/lab/lab9_pp2/Дождь (Sefon.me).mp3']
current_track = 0
running = True
running_song = True

def start_music(track):
    pygame.mixer.music.load(lybrary[track])
    pygame.mixer.music.play()

def play_music(running_song):
    if running_song:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()
    # pygame.mixer.music.play()

start_music(current_track)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running_song = not running_song
                play_music(running_song)
            elif event.key==pygame.K_RIGHT:
                current_track+=1
                if current_track==len(lybrary):
                    current_track=0
                start_music(current_track)
            elif event.key==pygame.K_LEFT:
                current_track-=1
                if current_track<0:
                    current_track=len(lybrary)-1
                start_music(current_track)
               

    """screen.blit(photo,(0,0))"""
    my_text=font.render("Player is working", True, purpur)
    screen.blit(my_text, (15,5))
    pygame.display.flip()

pygame.quit()

