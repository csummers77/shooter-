class Arrow(object):
    def __init__(self,player):
        self.x = player.x
        self.y = player.y
        self.speed = 25
    def update_me(self):
        self.x += self.speed