import pygame

from game_vals.game_vals import *

scoreIncrement = 5


class Score( object ):
    """ to keep track of the score.
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__( self )
        self.font = pygame.font.Font( None, 40 )
        self.font.set_italic( 1 )
        self.font1 = pygame.font.Font( None, 40 )
        self.font1.set_italic( 1 )
        self.color = pygame.Color( "white" )
        self.scoreIncrement = 100
        self.lastscore = -1
        self.SCORE = TOTAL_POINTS
        self.NAME = ''

    def scoreupdate(self):
        """ We only update the score in update() when it has changed.
        """
        if self.SCORE != self.lastscore:
            self.lastscore = self.SCORE
            self.SCORE = self.SCORE + self.scoreIncrement
        return self.SCORE

    def changeIncrement(self, multiFactor):
        self.scoreIncrement = self.scoreIncrement * multiFactor

    def revertIncrement(self):
        self.scoreIncrement = 100

    def setName(self, name):
        self.NAME = name

    def getName(self):
        return self.NAME[:-1]

    def getScore(self):
        return self.SCORE



