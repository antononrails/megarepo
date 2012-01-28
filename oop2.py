class Stakan(object):
    Position = [u'shakaf',u'table']
    def __init__(self):
        self.__Water = 0.0
        self.__Milk = 0.0
        self.__Pos = u"shkaf"
    def add_water(self,vol):
        if vol < 0:
            raise ValueError
        self.__Water += vol
    def set_position(self,pos):
        pass
    def add_milk(self,vol):
        if vol < 0:
            raise ValueError
        self.__Milk += vol
    def take(self,vol):
        if vol < 0:
            raise ValueError
        if vol > self.total():
            raise Exception
        p = self.part_milk()
        m = self.part_milk()*vol
        w = vol - m
        self.__Milk -= m
        self.__Water -= w
        return (vol,p)
    @property
    def total(self):
        return St.__Water + St.__Milk
    @property
    def part_milk(self):
        return self.__Milk/self.total()
        return self.__Milk/(self.__Milk+self.__Water)
if __name__ == "__main__":
    St = Stakan()
    #Stakan.add_water(St,5.0)
    St.add_water(5)
    St.add_milk(3)
    print St.total
    print St.part_milk
    