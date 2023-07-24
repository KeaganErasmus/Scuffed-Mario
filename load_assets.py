import os, pygame

class Load_assets:
    def __init__(self, filename: str) -> any:
        self.filename = os.path.join(filename)
        self.sheet = pygame.image.load("data/"+filename)

    def get_sprites(self, frame: int, w: int, h: int, scale: int, colorkey=None) -> pygame.Surface:
        """Load sprite sheets so that we can do animations"""
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey(colorkey)
        sprite.blit(self.sheet, (0,0), ((frame*w), 0, w, h))
        sprite = pygame.transform.scale(sprite, (w * scale, h * scale))
        return sprite
    
    def load_image(self, path):
        """Load full images usefull for backgrounds"""
        image = pygame.image.load(path)
        return image
