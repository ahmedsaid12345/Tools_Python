
from abc import ABC, abstractmethod
from multiprocessing import Value
from typing import final
from unicodedata import name


class Builder_Abstarct(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the Product objects.
    
    """
    @property
    @abstractmethod
    def product(self)->None:
        pass


    @abstractmethod
    def part_A():
        pass

    @abstractmethod
    def part_B():
        pass


    @abstractmethod
    def part_C():
        pass






class Concrete_Builder_1(Builder_Abstarct):

    
    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        self._product = product_1()




    def product(self):
        ret_product= self._product
        self.reset()
        return ret_product



    def part_A(self):
        self._product.add("Part A")
        

        


    def part_B(self):
        self._product.add("Part B")
    



    def part_C(self):
        self._product.add("Part C")




class Director_1():

    def __init__(self) -> None:
       # self.builder_ins=Concrete_Builder_1()
        self.builder_ins=None
        
    @property    
    def builder_fun(self):
        return self.builder_ins

    @builder_fun.setter
    def builder_fun(self,builder_ar):
        self.builder_ins = builder_ar




    def Make_BasicParts(self):
        self.builder_ins.part_A()


    def Make_FullParts(self):
        self.builder_ins.part_A()
        self.builder_ins.part_B()
        self.builder_ins.part_C()










class product_1():
    def __init__(self) -> None:
        self.parts = []

    def add(self, part) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")
            




if __name__ =='__main__' :
    director = Director_1()
    builder_ma = Concrete_Builder_1()
    director.builder_fun =builder_ma
    director.Make_FullParts()
    builder_ma.product().list_parts()
    #final_product.list_parts()
    #final_product.add("part vb")
    #final_product.list_parts()


















#def Concrete_Builder_1(Builder_Abstarct):
 #   pass


















