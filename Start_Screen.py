import pygame,os,Game_Modes,How_to_play

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 09:24:39 2020
@author: CHAO CUI, HAO WU, NANDI GUO
"""

pygame.init()                                                                  # pygame initialization
Width,Height = (780,366)                                                       # window size
Orange = (255,145,0)                                                           # Button colors, RGB
White = (255,255,255)
Blue = (0,238,255)

pygame.display.set_caption("Start Screen")                                     # window title, images of several windows, font                         
background = pygame.image.load("Images/Backgrounds/Start1_Background.png")
how_to_play = pygame.image.load("Images/Backgrounds/how.png")
font = pygame.font.SysFont("Verdana",25)                                        
bgm_sound = pygame.mixer.Sound("Sounds/Start_Bgm.mp3")                         # Starting_Screen Bgm loaded

class Button():                                                                # Button class, **kwargs ready to receive more parameters
    def __init__(self, text, color, x=None, y=None, **kwargs):  
        self.surf = font.render(text, True, color)                             # Button width,height 
        self.WIDTH = self.surf.get_width()
        self.HEIGHT = self.surf.get_height()
        self.x = x                                                             # (x,y) is coodinate of button
        self.y = y

    def display(self):
    	screen.blit(self.surf, (self.x, self.y))

    def check_click(self, position):                                           # if coordinate of mouse is in the range of button
        x_match = position[0] > self.x and position[0] < self.x + self.WIDTH   # left x, mouse ,right x
        y_match = position[1] > self.y and position[1] < self.y + self.HEIGHT  # up y, mouse ,down y

        if (x_match) and (y_match):                                            # check if in                 
            return True
        else:
            return False

def Show(screen,Text,x,y) :                                                    # display and font
    score_font = pygame.font.SysFont("Verdana",15)
    surf = score_font.render(Text,False,(255,255,255))
    screen.blit(surf,(x,y))
    
def Firstscreen():                                                             # the first window display function
    bgm_sound.play()
    global screen
    screen = pygame.display.set_mode((Width, Height))
    b1x,b1y=360,100                                                            # Buttons coordinates
    b2x,b2y=360,160     
    b3x,b3y=310,220  
    screen.blit(background, (0,0))
    pygame.mixer.music.load('Sounds/Button_Click.mp3')
    title = font.render('CWG-Ultimate Warrior', True, White)
    screen.blit(title, (Width//2 - title.get_width()//2, 40))
    play_button = Button('Play', Orange, b1x, b1y)                             # buttons text and original color, coordinates
    exit_button = Button('Quit', Orange, b2x, b2y)
    introduction_button = Button('How to play', Orange, b3x, b3y)
    play_button.display()
    exit_button.display()
    introduction_button.display()                                              #  display button 
    
    
    Show(screen," Creators: CHAO CUI, NANDI GUO, HAO WU          \                                                        \
    Version 1.0",0, Height-30)
    Show(screen,f"Green gem = {Game_Modes.Gem_easy}, Red gem = {Game_Modes.Gem_normal}, Yellow gem = {Game_Modes.Gem_hard}, Blue gem = {Game_Modes.Gem_ultimate}",0,0) 
    while True:
        pygame.display.update()
        if not (play_button.check_click(pygame.mouse.get_pos()) or\
            exit_button.check_click(pygame.mouse.get_pos()) or\
            introduction_button.check_click(pygame.mouse.get_pos())):
                pygame.mixer.music.play()                                      # when mouse is moving on the buttons, play the click sound

        if play_button.check_click(pygame.mouse.get_pos()):                    # when mouse is moving on the buttons, change the colors of button
            play_button = Button('Play', Blue, b1x, b1y)                        
        else:            
            play_button = Button('Play', Orange, b1x, b1y)
            
        if exit_button.check_click(pygame.mouse.get_pos()):
            exit_button = Button('Quit', Blue, b2x, b2y)
        else:           
            exit_button = Button('Quit', Orange, b2x, b2y)

        if introduction_button.check_click(pygame.mouse.get_pos()):
            introduction_button = Button('How to play', Blue, b3x, b3y)                        
        else:            
            introduction_button = Button('How to play', Orange, b3x, b3y)

        play_button.display()                                                  # refresh display
        exit_button.display()
        introduction_button.display()
        pygame.display.update()

        for event in pygame.event.get():                                       # Quit the game
            if event.type == pygame.QUIT:
                pygame.quit()
                os._exit(0)
                
        if pygame.mouse.get_pressed()[0]:                           
            if play_button.check_click(pygame.mouse.get_pos()):                #click play, stop current bgm, go to modes screen
                bgm_sound.stop()
                Game_Modes.Modes_Screen()
                pygame.quit()
                os._exit(0)
                break

            if exit_button.check_click(pygame.mouse.get_pos()):                #click quit, quit the game
                bgm_sound.stop()
                pygame.quit()
                os._exit(0)
                break

            if introduction_button.check_click(pygame.mouse.get_pos()):        #click how to play, stop current bgm, go to how_to_play screen
                bgm_sound.stop()
                How_to_play.How_screen()
                os._exit(0)
                break            

