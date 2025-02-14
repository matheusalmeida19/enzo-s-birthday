import pygame
from level_data import world_data  # ✅ Importar os dados do mapa
from player import Player

pygame.init()

# Configurações da tela
screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Plataformer')

# Define o tamanho dos tiles
tile_size = 50

# Carregar imagens
sun_img = pygame.image.load('assets/img/sun.png')
bg_img = pygame.image.load('assets/img/bg.png')
lava_img = pygame.image.load('assets/img/lava.png')

bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height))
sun_img = pygame.transform.scale(sun_img, (170, 170))


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
player = Player(100, screen_height - 130, screen)  # ✅ Agora passando a screen corretamente

run = True
clock = pygame.time.Clock()

while run:
    screen.blit(bg_img, (0, 0))
    screen.blit(sun_img, (-10, -10))

    world.draw()
    player.update(world)  # ✅ Player agora atualiza corretamente

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
