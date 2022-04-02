""" tuple_1=((1,2,3),4)
tuple_2=tuple_1
ele_1,*other=tuple_1
ele_2,ele_3,*other_1=ele_1

print(ele_1,other,tuple_2)
print(ele_2,ele_3,other_1)
print(type(ele_2),type(other))

#############################################
#Ternay operator
#if-condition_True if Condition else_Condition_true


#list_1=[1,2,3,4,5]
#print(3 in list_1)
####################################
#*args **kwargs


dict_1={ k: (v := k*2) for k in [1,2,3,4]}
print(dict_1)




 """


""" def Hello():
    print("Hellloooooooo")

greet = Hello

Hello()
greet()
del Hello
greet()
Hello()
 """
#######################
# Higher Order Function   HOF 
#Any function that accept Function in it's parameter or return function is called HOF

""" 
def func_1(wrape_func):
    def func_2():
        print("***************************")
        wrape_func()
        print("*****************************")
    return func_2    


@func_1
def Hello():
    print("Hellllloooooooooooooo")


#Hello()

func_1(Hello)
#s() """

""" def enternum():
    x=int(input("Enter Integar"))
    return x
while True :
    try:
        r = enternum()
        print(r)
    except:
        print("pls enter int number")
    else:
        break    
 
print("Finally we get exception Concept")
   
 """

# to define generator we must use yield and range.

""" 
def  Generator_Func(item):
    for i in range(item):
        yield(i)


g=Generator_Func(7)

try:
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
except:
    print("End of iterator dude")
 """
""" 
for i in Generator_Func(10):
    print(i)        
 """

############ Create for Loop #################
""" 
def Special_For(iterable_1):
    iter_1=iter(iterable_1)
    while True:
        try:
            print(iter_1)
            print(next(iter_1))
        except StopIteration:
            print("End of iteration")
            break


Special_For([1,2,3])


class Implement_Range():
    current = 0
    def __init__(self,first_ele,last_ele):
        self.first_ele = first_ele
        self.last_ele = last_ele 
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if   self.current < self.last_ele:
            num_1 = self.current
            Implement_Range.current +=1
            return num_1
        raise StopIteration    



r=Implement_Range(0,7)
for i in r:
    print(i)

print(__name__) """

import sys

first_name=sys.argv[1]
sec_name=sys.argv[2]
print("hi")
print(f'HI {first_name} {sec_name}')












































































