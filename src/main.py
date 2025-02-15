import pygame
from level_data import world_data
from player import Player
from items import Balloon, Cake
from victory_screen import show_victory_screen
from start_screen import show_start_screen

pygame.init()

# Configurações da tela
screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Plataformer')

show_start_screen(screen)

# Define o tamanho dos tiles
tile_size = 50

# Carregar imagens
sun_img = pygame.image.load('assets/img/sun.png')
bg_img = pygame.image.load('assets/img/bg.png')
lava_img = pygame.image.load('assets/img/lava.png')

bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height))
sun_img = pygame.transform.scale(sun_img, (170, 170))

balloons = pygame.sprite.Group()
balloons.add(
    Balloon(50, 100, "assets/img/b1.png"),
    Balloon(300, 100, "assets/img/b2.png"),
    Balloon(350, 400, "assets/img/b3.png"),
)

cake = Cake(500, 100, "assets/img/cake.png")
cake_unlocked = False

class World():
    def __init__(self, data):
        self.tile_list = []

        dirt_img = pygame.image.load('assets/img/dirt.png')
        grass_img = pygame.image.load('assets/img/grass.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    tile_type = "ground"
                elif tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    tile_type = "grass"
                elif tile == 3:
                    img = pygame.transform.scale(lava_img, (tile_size, tile_size))
                    tile_type = "lava"
                else:
                    col_count += 1
                    continue

                img_rect = img.get_rect()
                img_rect.x = col_count * tile_size
                img_rect.y = row_count * tile_size
                self.tile_list.append((img, img_rect, tile_type))
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


world = World(world_data)
player = Player(100, screen_height - 130, screen)

run = True
clock = pygame.time.Clock()

while run:
    screen.blit(bg_img, (0, 0))
    screen.blit(sun_img, (-10, -10))

    world.draw()
    player.update(world)

    balloons.draw(screen)
    
    collected_balloons = pygame.sprite.spritecollide(player, balloons, True)
    for balloon in collected_balloons:
        balloon.play_sound()
    
    
    if len(balloons) == 0:
        cake_unlocked = True

    # Desenhar bolo apenas se desbloqueado
    if cake_unlocked:
        screen.blit(cake.image, cake.rect)
        if player.rect.colliderect(cake.rect):
            cake.play_sound()
            print("🎂 Parabéns! Você coletou o bolo e venceu o jogo! 🎂")
            run = False

    if cake_unlocked:
        screen.blit(cake.image, cake.rect)
        if player.rect.colliderect(cake.rect):
            result = show_victory_screen(screen)  
            if result == "replay":
                # Reinicia o jogo
                player = Player(100, screen_height - 130, screen)
                balloons = pygame.sprite.Group()
                balloons.add(
                    Balloon(50, 100, "assets/img/b1.png"),
                    Balloon(300, 100, "assets/img/b2.png"),
                    Balloon(350, 400, "assets/img/b3.png"),
                )
                cake_unlocked = False
            elif result == "menu":
                show_start_screen(screen)  
                player = Player(100, screen_height - 130, screen) 
                
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
