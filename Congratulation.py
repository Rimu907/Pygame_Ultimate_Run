# -*- coding: utf-8 -*-
"""
Created on Fri Dec 4 22:09:30 2020

@author: CHAO CUI, HAO WU, NANDI GUO
"""
import pygame,os

                        
Orange = (119,0,255)                                                           # Button colors, RGB
White = (255,255,255)
Blue = (0,238,255)
Width,Height = (781,482)                                                       # window size


def Con_Screen():
    global screen,font
    pygame.init()
    screen = pygame.display.set_mode((Width, Height))  
    pygame.display.set_caption("Congratulation!")                              # window title
    background = pygame.image.load("Images/Backgrounds/Congratulation_1.png")
    screen.blit(background, (0,0))                                             # display background
    cong = pygame.mixer.Sound("Sounds/happy.mp3")
    cong.play()                                                                # play the sister's whisper
    
    while True:                    
        pygame.display.update()                                                # quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                os._exit(0)

       
