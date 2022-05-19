class Singleton:
   __instance = None
   @staticmethod 
   def getInstance():
      """ Static access method. """
      if Singleton.__instance == None:
         Singleton()
      return Singleton.__instance
   def __init__(self):
      """ Virtually private constructor. """
      print (Singleton.__instance)
      if Singleton.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         Singleton.__instance = self
#s = Singleton()
#print (s)

s = Singleton.getInstance()
print (s)
Singleton.__instance=None

print(Singleton.__instance)

#s_2 = Singleton()
s = Singleton.getInstance()
print (s)




















