
class Button(object):
   html = ""
   def get_html(self):
      return self.html

class Image(Button):
   html = "<img></img>"
   
   def get_html(self):
      return Image.html
   
   def try_1(self):
        print("HACK ALL...")  

   

class Input(Button):
   html = "<input></input>"

class Flash(Button):
   html = "<obj></obj>"

class ButtonFactory():
   def create_button(self, typ):
      targetclass = typ.capitalize()
      return globals()[targetclass]()

button_obj = ButtonFactory()
button = ['image', 'input', 'flash']
for b in button:
   print (button_obj.create_button(b).get_html())
   new_obj=button_obj.create_button(b)
   #new_obj.try_1()










