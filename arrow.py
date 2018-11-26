Arrow needs to be a subclass of sprite
so that we can add it to a group
from pygame.sprite import Sprite
class Arrow(object):
    def __init__(self,player):
        self.x = player.x
        self.y = player.y
        self.speed = 25
    def update_me(self):
        self.x += self.speed
