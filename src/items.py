import pygame

class Collectible(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (40, 40))  # Ajustar tamanho se necessário
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Balloon(Collectible):
    def __init__(self, x, y, image_path):
        super().__init__(x, y, image_path)

class Cake(Collectible):
    def __init__(self, x, y, image_path):
        super().__init__(x, y, image_path)
