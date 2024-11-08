# attack.py

import pygame

class Attack(pygame.sprite.Sprite):
    def __init__(self, rect, flip, damage=1):
        super().__init__()
        # Setup the attack sprite's rect and position
        self.image = pygame.Surface((rect.width, rect.height))
        self.image.fill((255, 0, 0))  # Fill with a visible color (red)
        self.rect = rect
        self.flip = flip
        self.damage = damage

    def update(self):
        # Move the attack hitbox depending on the direction the player is facing
        # (right or left)
        if self.flip:  # if flip is True, move left
            self.rect.x -= 5
        else:  # otherwise move right
            self.rect.x += 5

        # You can add other update logic if necessary, like removing the attack hitbox
        # after a certain duration or distance
