
#from fbchat import Client
#from fbchat.models import *
#client = Client('e620158@nwytg.net', 'سشي1234567')








#client.send(Message(text='الووووووووووووووو'), thread_id='100075903229701', thread_type=ThreadType.USER)
#client.send(Message(text='<message>'), thread_id='<group id>', thread_type=ThreadType.GROUP)





from fbchat import Client
from fbchat.models import *


print('dfgjrtukyrukryuk')
client = Client('mahmoudalihack.0000@gmail.com','Sad1234567')
print('dfgjrtukyrukryuk')
print("Own id: {}".format(client.uid))

client.send(Message(text="Hi me!"), thread_id=client.uid, thread_type=ThreadType.USER)

client.logout()









