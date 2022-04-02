# Demonstration of MRO

class X:
    def __init__(self) -> None:
         print("X class")
     #print("B class")
    #pass


class Y:
    def __init__(self) -> None:
         print("Y class")
     #print("Y class")
    #pass


class Z:
    def __init__(self) -> None:
        #pass
         print("Z class")
    


class A(X, Y):
    def __init__(self) -> None:
         print("A class")
         super().__init__()
    pass


class B(Y, Z):
    def __init__(self) -> None:
        print("B class")
        super().__init__()
    pass


class M(B, A, Z):
    pass

# Output:
# [<class '__main__.M'>, <class '__main__.B'>,
#  <class '__main__.A'>, <class '__main__.X'>,
#  <class '__main__.Y'>, <class '__main__.Z'>,
#  <class 'object'>]
m_1=M()
print(M.mro()) #method Resolution Order