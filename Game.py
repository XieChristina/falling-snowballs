# Game.py
# Christina Xie
# December 2020
# Falling Snowballs!

import pygame
from random import randint
pygame.init()  # initializes the pygame

#variables
WIDTH = 800
HEIGHT = 600

gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Snowballs") # title of game window

font1 = pygame.font.SysFont("Courier New Bold", 36)# assign font information

RED = (255, 0, 0)
GREEN =(0, 255, 0)
BLUE =( 204, 255, 255 )
CYAN =(0, 255, 255)
WHITE =(255, 255, 255)
BLACK =(0, 0, 0)
GREY = (128, 128, 128)

#main program

gameWindow.fill(BLUE)
RADIUS = 30
ballX = 35  
ballY = 470
xFactor = 0
collision = False

enemyX = randint(0, WIDTH)
enemyY = -100  #so appears off line before it falls

while (collision == False): 
  
    #game play message ===============================================================
    message = font1.render("How to play", 0, BLACK)
    gameWindow.blit(message, (50, 40) )
    rule1 = font1.render("- Press 'd' to move right", 0, BLACK)
    gameWindow.blit(rule1, (50, 70) )
    rule2 = font1.render("- Press 'a' to move left", 0, BLACK)
    gameWindow.blit(rule2, (50, 90) )
    rule3 = font1.render("- Avoid the falling snowballs", 0, BLACK)
    gameWindow.blit(rule3, (50, 110) )
    rule3 = font1.render("- Game over when you hit a snowball!", 0, BLACK)
    gameWindow.blit(rule3, (50, 130) )
    #=========================================================== game play message ====
    
    
    #draw ground
    pygame.draw.rect(gameWindow, GREEN, (0, 500, WIDTH, HEIGHT), 0)

    # draw ball
    pygame.draw.circle(gameWindow, BLACK,  (ballX, ballY), RADIUS, 0)

    #display object/enemy
    pygame.draw.circle(gameWindow, WHITE, (enemyX, enemyY), 15, 0) #object/enemy
    
    pygame.display.update()   #display must be updated to show what you are drawing
    pygame.time.delay(15)  # millisecond
    
    pygame.draw.circle(gameWindow, BLUE,  (ballX, ballY), RADIUS, 0)  #make ball #dissappear,so it can be displayed in another location
    pygame.display.update()
    
    pygame.draw.circle(gameWindow, BLUE, (enemyX, enemyY), 15, 0) #object/enemy disappears for next movement
    pygame.display.update()
  
    # ball movement
    pygame.event.get() # poll the keyboard for events/keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] and ballX<= WIDTH: #move player right
      ballX = ballX + 3      
    elif keys[pygame.K_a] and ballX>=0: #move player left
      ballX = ballX - 3
    #end if
    
    #enemy movement
    enemyY = enemyY + 5
    if enemyY > HEIGHT + 50:
      enemyX = randint(0, WIDTH)
      enemyY = -100 
    #end if 

    #collisions
    if ballX+RADIUS-10 >= enemyX and ballX-RADIUS+10 <=enemyX+50 and enemyY+50-10> ballY-RADIUS and enemyY-10 < ballY+RADIUS:#collision with enemy MORE EFFECTIVE    
        collision = True
    #end if 
    
#end while loop 

#game over
gameWindow.fill(BLACK)
graphics = font1.render("Oh no!", 0, RED) #define what to display
gameWindow.blit(graphics, (WIDTH//2, HEIGHT//2-40) ) # display in centre of window
pygame.display.update()
graphics = font1.render("GAME OVER :(", 0, WHITE) #define what to display
gameWindow.blit(graphics, (WIDTH//2 - 100, HEIGHT//2) ) # display in centre of window

pygame.display.update()   #display must be updated to show "GAME OVER" screen
pygame.time.delay(5000)  # 5000 millisecond = 5 seconds
pygame.quit()  # must put in quit, so you don't get an NO-responding window

