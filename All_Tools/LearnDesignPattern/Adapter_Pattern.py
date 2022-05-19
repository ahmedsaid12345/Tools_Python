from abc import ABC,abstractmethod



#define interface Itarget
class Itarget(ABC):
    @abstractmethod
    def Request_Func(self):
        pass






class ConceretAdapter(Itarget):
    def __init__(self,Adaptee_var):
        self.adaptee=Adaptee_var
    
    def Request_Func(self):
        self.adaptee.Specific_Operation()

        


class Adaptee:
    def Specific_Operation(self):
        print("specific opration")



def main():
    adaptee_1=Adaptee()
    target_1=ConceretAdapter(adaptee_1)
    target_1.Request_Func()
    







if __name__=="__main__":
    main()