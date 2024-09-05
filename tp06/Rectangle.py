


class Rectangle:
    __slots__ = ('__longueur','__largeur')
    __cpt = 0
    
    instance = None       # Attribut statique de classe
    
    def __new__(cls): 
        "méthode de construction standard en Python"
        if cls.instance is None:
            cls.instance = object.__new__(cls)
        return cls.instance
        
    def __init__(self,lng=0,lrg=0):
        self.__longueur = lng
        self.__largeur = lrg
        Rectangle.__cpt+=1

    @classmethod
    def buildFromStr(cls,value):
        lng,lrg = [int(v) for v in value.split(";")]
        return cls(lng,lrg)

    @property
    def longueur(self):
        return self.__longueur

    @longueur.setter
    def longueur(self,lng):
        if lng<=0:
            raise Exception("Hoooooo")

        self.__longueur=lng

    @property
    def largeur(self):
        return self.__largeur
    
    @largeur.setter
    def largeur(self,lrg):
        if lrg<=0:
            raise Exception("Hoooooo")

        self.__largeur=lrg
    
    @staticmethod
    def get_cpt():
        return Rectangle.__cpt

    @property
    def surface(self):
        return self.longueur*self.largeur


    def __str__(self):
        return f"{__class__.__name__} {self.longueur=}, {self.largeur=}"

    def __eq__(self, o):
        return self.longueur == o.longueur and self.largeur == o.largeur
        

    def __del__(self):
        print("def __del__(self)")
        Rectangle.__cpt-=1
    
    # longueur = property(get_longueur,set_longueur,doc="longueur property")
    # largeur = property(get_largeur,set_largeur,doc="largeur property")
