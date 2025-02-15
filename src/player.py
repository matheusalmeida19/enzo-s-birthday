import pygame

class Player():
    def __init__(self, x, y, screen):
        self.screen = screen  

        
        self.walk_frames = [
            pygame.image.load(f'assets/img/p1_walk{str(i).zfill(2)}.png') for i in range(1, 12)
        ]
        self.walk_frames = [pygame.transform.scale(img, (30, 60)) for img in self.walk_frames]

        
        self.image = pygame.image.load('assets/img/p1_front.png')
        self.image = pygame.transform.scale(self.image, (30, 60))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False
        self.facing_right = True
        
        self.current_frame = 0
        self.animation_speed = 5
        self.frame_counter = 0
        
        self.jump_sound = pygame.mixer.Sound("assets/songs/jump.mp3")
        self.jump_sound.set_volume(0.1)
        
        
        
    def update(self, world):
        self.vel_y += 0.8
        if self.vel_y > 10:
            self.vel_y = 10

        key = pygame.key.get_pressed()
        moving = False

        if key[pygame.K_LEFT]:
            self.vel_x = -3
            self.facing_right = False
            moving = True
        elif key[pygame.K_RIGHT]:
            self.vel_x = 3
            self.facing_right = True
            moving = True
        else:
            self.vel_x = 0

        if key[pygame.K_SPACE] and self.on_ground:
            self.vel_y = -16
            self.on_ground = False
            self.jump_sound.play()

        self.rect.x += self.vel_x
        for tile in world.tile_list:
            if self.rect.colliderect(tile[1]) and tile[2] in ["ground", "grass"]:
                if self.vel_x > 0:
                    self.rect.right = tile[1].left
                elif self.vel_x < 0:
                    self.rect.left = tile[1].right

        self.rect.y += self.vel_y
        self.on_ground = False
        for tile in world.tile_list:
            if self.rect.colliderect(tile[1]):
                if tile[2] == "lava":
                    print("🔥 Você caiu na lava! Game Over! 🔥")
                    pygame.quit()
                    exit()

                if tile[2] in ["ground", "grass"]:
                    if self.vel_y > 0:
                        self.rect.bottom = tile[1].top
                        self.vel_y = 0
                        self.on_ground = True
                    elif self.vel_y < 0:
                        self.rect.top = tile[1].bottom
                        self.vel_y = 0

        if self.rect.y > 600:
            print("🔥 Você caiu fora do mapa! Game Over! 🔥")
            pygame.quit()
            exit()
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 600 - self.rect.width:
            self.rect.x = 600 - self.rect.width

        
        if moving:
            self.frame_counter += 1
            if self.frame_counter >= self.animation_speed:
                self.frame_counter = 0
                self.current_frame = (self.current_frame + 1) % len(self.walk_frames)
                self.image = self.walk_frames[self.current_frame]
        else:
            self.image = pygame.image.load('assets/img/p1_front.png')
            self.image = pygame.transform.scale(self.image, (30, 60))

        if not self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)

        self.screen.blit(self.image, self.rect)
