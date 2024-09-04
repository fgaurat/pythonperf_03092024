from Rectangle import Rectangle

class Carre(Rectangle):


    def __init__(self,cote):
        super().__init__(cote,cote)
        self.__cote = cote

    @property
    def cote(self):
        return self.__cote
    
    @cote.setter
    def cote(self,cote):
        self.__cote = cote