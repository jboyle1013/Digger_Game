import pygame

scoreIncrement = 5
class Score(pygame.sprite.Sprite):
    """ to keep track of the score.
    """
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(None, 40)
        self.font.set_italic(1)
        self.font1 = pygame.font.Font(None, 40)
        self.font1.set_italic(1)
        self.color = pygame.Color("white")
        self.scoreIncrement = 5
        self.lastscore = -1
        self.SCORE = 0
        self.NAME = ''
        self.update()
        self.rect = self.image.get_rect().move(10, 30)

    def update(self):
        """ We only update the score in update() when it has changed.
        """
        if self.SCORE != self.lastscore:
            self.lastscore = self.SCORE
            self.SCORE = self.SCORE + scoreIncrement
            msg = "Score: %d" % self.SCORE
            self.image = self.font.render(msg, 0, self.color)

    def changeIncrement(self, multiFactor):
        self.scoreIncrement = self.scoreIncrement * multiFactor

    def revertIncrement(self):
        self.scoreIncrement = 5

    def setName(self, name):
        self.NAME = name

    def getName(self):
        return self.NAME[:-1]

    def getScore(self):
        return self.SCORE



