class Level( object ):
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    def __init__(self, score, lives):
        self.score = score
        self.lives = lives
