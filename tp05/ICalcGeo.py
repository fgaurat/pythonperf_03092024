from abc import ABC,abstractmethod,ABCMeta


class ICalcGeo(metaclass=ABCMeta):

    @property
    @abstractmethod
    def surface(self):
        pass