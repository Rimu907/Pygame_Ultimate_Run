# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 22:09:30 2020

@author: CHAO CUI, HAO WU, NANDI GUO
"""

import pygame,os,Game_Modes,Start_Screen


Width,Height = (813,409)
Orange = (119,0,255)
White = (255,255,255)
Blue = (0,238,255)
        
def How_screen():                                                              # how_to_play window initialization
    global screen,font
    pygame.init()
    screen = pygame.display.set_mode((Width, Height))
    
    pygame.display.set_caption("How_to_play")
    background = pygame.image.load("Images/Backgrounds/how.png")
    
    screen.blit(background, (0,0))
    pygame.display.update()
    
    bgm2_sound = pygame.mixer.Sound("Sounds/Modes_Bgm.mp3")                    # bgm load
    bgm2_sound.play()
    b1x,b1y=670,370                                                            # buttons positions
    b2x,b2y=15,375

    screen.blit(background, (0,0))
    pygame.mixer.music.load('Sounds/Button_Click.mp3')
    
    play_button = Start_Screen.Button('Play Game', Orange, b1x, b1y)           # call Button function
    back_button = Start_Screen.Button('Back', Orange, b2x, b2y)
    play_button.display()
    back_button.display()                                                      # display buttons
    pygame.display.update() 
       
    while True:       
        if not (play_button.check_click(pygame.mouse.get_pos()) or\
                back_button.check_click(pygame.mouse.get_pos())):                
            pygame.mixer.music.play()                                          # when mouse is moving on the buttons, play the click sound
            
        if play_button.check_click(pygame.mouse.get_pos()):                    # when mouse is moving on the buttons, change button colors
            play_button = Start_Screen.Button('Play Game', Blue, b1x, b1y)                        
        else:            
            play_button = Start_Screen.Button('Play Game', Orange, b1x, b1y)
        
        if back_button.check_click(pygame.mouse.get_pos()):              
            back_button = Start_Screen.Button('Back', Blue, b2x, b2y)                        
        else:            
            back_button = Start_Screen.Button('Back', Orange, b2x, b2y)
            
        play_button.display()
        back_button.display()
        pygame.display.update()
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:                                  # quit game
                    pygame.quit()
                    os._exit(0)
                            
        if pygame.mouse.get_pressed()[0]:            
            if play_button.check_click(pygame.mouse.get_pos()):                # click play, stop current bgm, go to modes screen
                bgm2_sound.stop()
                Game_Modes.Modes_Screen()
                pygame.quit()                
                os._exit(0)
                break
                         
            if back_button.check_click(pygame.mouse.get_pos()):                # click back, stop current bgm, go to Start_Screen
                bgm2_sound.stop()
                Start_Screen.Firstscreen()
                pygame.quit()                
                os._exit(0)
                break

