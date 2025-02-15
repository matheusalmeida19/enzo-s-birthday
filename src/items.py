import pygame

class Collectible(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, sound_path=None):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (40, 40))  # Ajustar tamanho se necessário
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.sound_path = sound_path

    def play_sound(self):
        """Toca o som do item se existir."""
        if self.sound_path:
            sound = pygame.mixer.Sound(self.sound_path)
            sound.play()
    
class Balloon(Collectible):
    def __init__(self, x, y, image_path):
        super().__init__(x, y, image_path, "assets/songs/item1.mp3")

class Cake(Collectible):
    def __init__(self, x, y, image_path):
        super().__init__(x, y, image_path, "assets/songs/item1.mp3")
