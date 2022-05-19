


from prometheus_client import Counter


class try_access_Modifier:
    Counter=0
    public_counter=0
    _protected_counter=1
    __private_counter=2
    def __init__(self,public_c,private_c,protected_c) :
        self.public_counter=public_c
        self.__private_counter=private_c
        self._protected_counter=protected_c

    def Display_all(self):
        print(self.public_counter)
        print(self._protected_counter)
        print(self.__private_counter)
    
    @staticmethod
    def try_StaticMethod(intvar):
        #counter=0
        try_access_Modifier.Counter  +=1
        print("Hello Sattic Method."+str(try_access_Modifier.Counter))     





def main():
    obj1=try_access_Modifier(3,4,5)
    obj1.__private_counter=90
    print("class it self")
    obj1.Display_all()
    print("starting")
    print(obj1.public_counter)
    print(obj1._protected_counter)
    print(obj1.__private_counter)
    
    print ("Try Static Methods from main. ")
    
    try_access_Modifier.try_StaticMethod(34)
    try_access_Modifier.try_StaticMethod(34)
    try_access_Modifier.try_StaticMethod(34)
    obj1.try_StaticMethod(12)






if __name__=="__main__":
    main()
