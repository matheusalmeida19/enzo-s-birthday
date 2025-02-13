import pygame

pygame.init()

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Plataformer')

#define game variables
title_size = 200

#load images
sun_img = pygame.image.load('assets/img/sun.png')
bg_img = pygame.image.load('assets/img/bg.png')

bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height))

sun_size= (150,150)
sun_img = pygame.transform.scale(sun_img, sun_size)

def draw_grid():
	for line in range(0, 20):
		pygame.draw.line(screen, (255, 255, 255), (0, line * title_size), (screen_width, line * title_size))
		pygame.draw.line(screen, (255, 255, 255), (line * title_size, 0), (line * title_size, screen_height))

run = True 
while run == True:
    
    screen.blit(bg_img, (0, 0 )) 
    screen.blit(sun_img, (-20, -20))

    draw_grid()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()
            
pygame.quit()        