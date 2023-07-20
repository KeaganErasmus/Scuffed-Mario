import os, pygame

class Load_assets:
    def __init__(self, filename: str) -> any:
        self.filename = os.path.join(filename)
        self.sheet = pygame.image.load("data/"+filename)

    def get_sprites(self, frame: int, w: int, h: int, scale: int) -> pygame.Surface:
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.sheet, (0,0), ((frame*w), 0, w, h))
        sprite = pygame.transform.scale(sprite, (w * scale, h * scale))
        return sprite
