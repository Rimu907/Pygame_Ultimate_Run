#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 09:24:39 2020
@author: CHAO CUI, HAO WU, NANDI GUO
"""

import pygame,os,random,Game_Modes,Start_Screen,itertools 

# The background of the game
class Game_Map() :
    # Initialise map background and coordinates
    def __init__(self,x,y,Background_Image) :
        self.x = x
        self.y = y
        self.Background_Image = Background_Image

    def Map_Move(self) :
        if self.x < -(Screen_Width-8) :
            # Reload the picture from the beginning after scrolling is complete
            self.x = 0   
        else :
            # The map scrolls forward by 8 units
            self.x -= 8  
        Screen.blit(pygame.image.load(self.Background_Image).convert_alpha(),(self.x, self.y))

# The role of the game
class Game_Role():
    def __init__(self,Role_Image) :  
        # Initialisation of the role rectangle
        self.rect = pygame.Rect(10,Lowest_y,0,0)
        self.Role_Image = Role_Image
        # Highest position for the role jumps
        self.Jump_Height = Highest_y
        # Minimum y-coordinate of the role
        self.Jump_Start_Position = Lowest_y
        # Control whether the role jumps, True for jump
        self.Jump_Control = False
        # Load pictures of the role in six different poses
        self.Image = (pygame.image.load(self.Role_Image[0]).convert_alpha()\
                      ,pygame.image.load(self.Role_Image[1]).convert_alpha()\
                          ,pygame.image.load(self.Role_Image[2]).convert_alpha()\
                              ,pygame.image.load(self.Role_Image[3]).convert_alpha()\
                                  ,pygame.image.load(self.Role_Image[4]).convert_alpha()\
                                     , pygame.image.load(self.Role_Image[5]).convert_alpha())
        # Get the size of the role picture
        self.rect.size = self.Image[0].get_size()
        # Reducing the height and width of the role+ to reduce the collision volume
        self.rect.width -= 30
        self.rect.height -= 30
        # Prevent the role from jumping twice in the air
        self.Jump_Control_Twist = False
    
    # Change the jump state to True
    def Jump(self):
        # Play the music of the jumping
        Jump_Sound.play()
        self.Jump_Control = True

    def Action_Move(self) : 
# If Jump_Control is True and Jump_Control_Twist is True, then Role is displaced upwards at the speed of Jump_Speed and automatically descends to the starting position when Jump_Height is reached.
        if self.Jump_Control == True and self.Jump_Control_Twist == False :
            self.rect.y -= Jump_Speed
            if self.rect.y <= self.Jump_Height :
                self.Jump_Control = False
                self.Jump_Control_Twist = True
        elif self.Jump_Control_Twist == True :
            self.rect.y += (Jump_Speed - 2)
            if self.rect.y >= self.Jump_Start_Position :
                self.Jump_Control_Twist = False
            
    def Draw_Role(self,i) :
        # If the role is not on the ground, draw a jumping form, if on the ground, a running form
        if self.Jump_Start_Position <= self.rect.y :
            Screen.blit(self.Image[i],(self.rect.x, self.rect.y))  
        else  :
            Screen.blit(self.Image[5],(self.rect.x, self.rect.y))
            
# The barriers of the game
class Barriers() :
    def __init__(self,Barriers_Images) :  
        # Initialisation of the barriers rectangle
        self.rect = pygame.Rect(800,0,0,0)
        self.Barriers_Images = Barriers_Images
        # Generate random numbers, different numbers represent different obstacles
        Random_Number =  random.randint(0,3)
        if Random_Number == 0 :   
            # Each obstacle has five different forms
            self.Image = (pygame.image.load(self.Barriers_Images[0][0]).convert_alpha()\
                          ,pygame.image.load(self.Barriers_Images[0][1]).convert_alpha()\
                              ,pygame.image.load(self.Barriers_Images[0][2]).convert_alpha()\
                                  ,pygame.image.load(self.Barriers_Images[0][3]).convert_alpha()\
                                      ,pygame.image.load(self.Barriers_Images[0][4]).convert_alpha())
            self.rect.y = Lowest_y
        elif Random_Number == 1 :
            self.Image = (pygame.image.load(self.Barriers_Images[1][0]).convert_alpha()\
                          ,pygame.image.load(self.Barriers_Images[1][1]).convert_alpha()\
                              ,pygame.image.load(self.Barriers_Images[1][2]).convert_alpha()\
                                  ,pygame.image.load(self.Barriers_Images[1][3]).convert_alpha()\
                                      ,pygame.image.load(self.Barriers_Images[1][4]).convert_alpha())
            self.rect.y = Lowest_y
        elif Random_Number == 2 :
            self.Image = (pygame.image.load(self.Barriers_Images[2][0]).convert_alpha()\
                          ,pygame.image.load(self.Barriers_Images[2][1]).convert_alpha()\
                              ,pygame.image.load(self.Barriers_Images[2][2]).convert_alpha()\
                                  ,pygame.image.load(self.Barriers_Images[2][3]).convert_alpha()\
                                      ,pygame.image.load(self.Barriers_Images[2][4]).convert_alpha())
            self.rect.y = Highest_y 
        elif Random_Number == 3 :
            self.Image = (pygame.image.load(self.Barriers_Images[3][0]).convert_alpha()\
                          ,pygame.image.load(self.Barriers_Images[3][1]).convert_alpha()\
                              ,pygame.image.load(self.Barriers_Images[3][2]).convert_alpha()\
                                  ,pygame.image.load(self.Barriers_Images[3][3]).convert_alpha()\
                                      ,pygame.image.load(self.Barriers_Images[3][4]).convert_alpha())
            self.rect.y = Highest_y 
        # Get the size of the barriers picture
        self.rect.size = self.Image[0].get_size()
        # Reducing the height and width of the role+ to reduce the collision volume
        self.rect.width -= 50
        self.rect.height -= 40
        # Set the index value of the obstacle in order to allow the obstacle to move
        self.Barriers_Index = itertools.cycle([0,1,2,3,4])
 
    # The movement of barriers 
    def Move(self) :
        self.rect.x -= 8
        
    def Draw_Barriers(self) :
        # Load the next picture from the obstacle list
        Index = next(self.Barriers_Index)
        Screen.blit(self.Image[Index], (self.rect.x, self.rect.y))
    
class Gems():
    def __init__(self,Gems_Images) :   
        # Initialisation of the gems rectangle
        self.rect = pygame.Rect(800,0,0,0)  
        self.Gems_Images = Gems_Images
        # Generate random numbers, different numbers represent different positions of the gem
        Random_Number =  random.randint(0,1)
        if Random_Number == 0 :         
            self.Image = pygame.image.load(self.Gems_Images).convert_alpha()
            self.rect.y = Lowest_y
        elif Random_Number == 1 :
            self.Image = pygame.image.load(self.Gems_Images).convert_alpha()
            self.rect.y = Highest_y + 10
        # Get the size of the gems picture
        self.rect.size = self.Image.get_size()
        self.Score = 1   
            
    # The movement of gems and the painting of the gems
    def Move(self) :
        self.rect.x -= 8
        Screen.blit(self.Image, (self.rect.x, self.rect.y))
    
    def getScore(self) :
        # Gems that have been bumped are replaced by the Nothing_1 image and no points are added if the player bumped this image.
        if self.Gems_Images == "Images/Barriers/Nothing_1.png" :
            return 0
        else :
            # When the player eats a gem, the number of gems is increased by one and Gem + 1 is displayed above the character's head.
            Start_Screen.Show(Screen,"Gem + 1",Role.rect.x + 15 , Role.rect.y - 10)
            Get_Score.play()
            Temporary_Score = self.Score
            self.Score = 0
            return Temporary_Score

# Set a range of parameters to facilitate the selection of game levels.
def Game_Main(P_Fps,P_Screen_Width,P_Screen_Height,P_Highest_y,P_Lowest_y,P_Background,P_Background_Sound,P_Barriers_Images,P_Gems_Images,Mode):
    global  Screen_Width,Screen_Height,Jump_Speed,Highest_y,Lowest_y,Jump_Sound,\
        Game_Run_Sound,Get_Score,Screen,Background_Images,Role
    Screen_Width = P_Screen_Width
    Screen_Height = P_Screen_Height
    Highest_y = P_Highest_y
    Lowest_y = P_Lowest_y    
    Jump_Speed = 8  
    Gems_number = 0
    Distance = 0
    # Time to produce gems
    Gem_Time = 0
    # Store the objects generated for each Gems()
    Gem_Lists = []
    # Time to produce barriers
    Barriers_Time = 0 
    # Store the objects generated for each Barriers()
    Barriers_List = []
    # Easy to load pictures of different role's movements
    Role_Image_Time = -1
    # Initialising pygame
    pygame.init()
    pygame.mixer.init() 
    # The sounds of the game
    Jump_Sound = pygame.mixer.Sound("Sounds/Jump.mp3")
    Game_Run_Sound = pygame.mixer.Sound(P_Background_Sound)
    Get_Score = pygame.mixer.Sound("Sounds/Get_Score.wav")
    Dead_Bgm = pygame.mixer.Sound("Sounds/Dead.mp3")
    # The images of the game
    Role_Image_Action = ["Images/Roles/Role_Run_1.png","Images/Roles/Role_Run_2.png","Images/Roles/Role_Run_3.png"\
                         ,"Images/Roles/Role_Run_4.png","Images/Roles/Role_Run_5.png","Images/Roles/Role_Jump.png"]
    Game_Over_Image = pygame.image.load("Images/Game_Over.png").convert_alpha()
    # Calling the Button class in Start_Screen
    Return_Button = Start_Screen.Button("Play Again", (255,255,255), Screen_Width/2 , Lowest_y)
    # Creat the display with Screen_Width and Screen_Height
    Screen = pygame.display.set_mode((Screen_Width,Screen_Height))
    # Set the title of the game
    pygame.display.set_caption("CWG's Game")   
    # Instantiating the Game_Role()
    Role = Game_Role(Role_Image_Action)
    # Controlling the frame rate
    Fps_Flash = pygame.time.Clock()
    # Instantiating the Game_Map()
    Bg = Game_Map(0,0,P_Background)
    # Setting the music loop
    Game_Run_Sound.play(-1,0)
    # Determines if the game is over, True is the end of the game
    Game_Over = False  
    while True : 
        if Game_Over == False : 
            Distance += 1
            Role_Image_Time += 1
            Bg.Map_Move()
            Role.Action_Move()  
            # Make the role move by loading different pictures
            if Role_Image_Time == 0 :
                Role.Draw_Role(0)
            elif Role_Image_Time == 1 :
                Role.Draw_Role(1)
            elif Role_Image_Time == 2 :
                Role.Draw_Role(2)
            elif Role_Image_Time == 3 :
                Role.Draw_Role(3)
            elif Role_Image_Time == 4 :
                Role.Draw_Role(4)
                Role_Image_Time = -1         
###############################################################################       
            # Gems generation 
            if Gem_Time >= 800 :
                r=random.randint(0,100)
                if r <= 10 :
                    Gem = Gems(P_Gems_Images)
                    Gem_Lists += [Gem]
                    Gem_Time = 0
            for i in range(len(Gem_Lists)) :
                Gem_Lists[i].Move() 
                # Determine if there is an overlap between the position where the gems are generated and the obstacle and if so, make the picture of the gems change to Nothing_1
                for j in range(len(Barriers_List)) :
                    if pygame.sprite.collide_rect(Barriers_List[j],Gem_Lists[i]) :
                        Gem_Lists[i] = Gems("Images/Barriers/Nothing_1.png") 
                # If a character collides with a gem, it gets a point and replaces the gem object with Gems("Images/Barriers/Nothing_1.png")
                if pygame.sprite.collide_rect(Role,Gem_Lists[i]) :   
                    Gems_number += Gem_Lists[i].getScore()
                    Gem_Lists[i] = Gems("Images/Barriers/Nothing_1.png") 
###############################################################################  
            # Barriers generation       
            if Barriers_Time >= 1000 :
                r=random.randint(0,100)
                if r <= 40 :
                    Barrier = Barriers(P_Barriers_Images)
                    Barriers_List += [Barrier]
                    Barriers_Time = 0                     
            for i in range(len(Barriers_List)) :
                Barriers_List[i].Move() 
                Barriers_List[i].Draw_Barriers()  
                # If a character collides with a gem, the game is over
                if pygame.sprite.collide_rect(Role,Barriers_List[i]) :
                    Game_Over = True
                    Game_Run_Sound.stop()
                    Dead_Bgm.play()
                    # Display the final overall results
                    Start_Screen.Show(Screen,f"You ran {Distance} meters and got {Gems_number} gems",0,0)
                    # The number of gems obtained for the different difficulty levels is transferred to the Game_Modes file.
                    if Mode == 0 :
                        Game_Modes.Gem_easy += Gems_number
                    elif Mode == 1 :
                        Game_Modes.Gem_normal += Gems_number
                    elif Mode == 2 :
                        Game_Modes.Gem_hard += Gems_number
                    elif Mode == 3 :
                        Game_Modes.Gem_ultimate += Gems_number
                    Screen.blit(Game_Over_Image,((Screen_Width/2 - Game_Over_Image.get_width()/2),(Screen_Height/2 - Game_Over_Image.get_height()/2)))
                    pygame.draw.rect(Screen, (0,0,0),[Screen_Width/2, Lowest_y, 130, 40])
                    Return_Button.display()
                    break    
###############################################################################            
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit() # For the rest of the people with windows or Linux
                os._exit(0) # For Mac users.
            elif event.type == pygame.KEYDOWN :
                # When the player enters the up, W and space keyboard keys, it causes the character to jump!
                if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_SPACE :
                    Role.Jump()                   
############################################################################### 
        # Monitor mouse click events, and end the game if you click to exit
        if pygame.mouse.get_pressed()[0] :            
            if Return_Button.check_click(pygame.mouse.get_pos()):
                Game_Run_Sound.stop()
                Game_Modes.Modes_Screen()
                pygame.quit()                
                os._exit(0)    
        Barriers_Time += 20
        Gem_Time += 30            
        pygame.display.flip()      
        Fps_Flash.tick(P_Fps)
        
