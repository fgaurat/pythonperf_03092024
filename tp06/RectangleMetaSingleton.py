 # Metaclass
class Singleton(type):
    instance = None       # Attribut statique de classe

    def __call__(self,*args,**kwargs): 
        if self.instance is None:
            self.instance = super().__call__(*args,**kwargs)
        else:
            self.instance.__init__(*args,**kwargs)
        
        return self.instance

class RectangleMetaSingleton(metaclass=Singleton):
    __slots__ = ('__longueur','__largeur')
    __cpt = 0
    
        
    def __init__(self,lng=0,lrg=0):
        self.__longueur = lng
        self.__largeur = lrg
        RectangleMetaSingleton.__cpt+=1

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
        return RectangleMetaSingleton.__cpt

    @property
    def surface(self):
        return self.longueur*self.largeur


    def __str__(self):
        return f"{__class__.__name__} {self.longueur=}, {self.largeur=}"

    def __eq__(self, o):
        return self.longueur == o.longueur and self.largeur == o.largeur
        
    def __del__(self):
        print("def __del__(self)")
        RectangleMetaSingleton.__cpt-=1

