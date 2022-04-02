import requests
import hashlib
import sys
def request_api_data(pass_char):
    url="https://api.pwnedpasswords.com/range/"+pass_char
    status_req =requests.get(url)
    if status_req.status_code != 200:
       # print('Bad Request')
        raise RuntimeError(f'Pls Check Your Url: Code {status_req.status_code} ')
    return status_req


def Get_Pass_Leak_Count(hashs,chech_my_pass):
    hashes = (line.split(':') for line in hashs.text.splitlines())
    #print(type(hashes))
    for h,c in hashes:
        if chech_my_pass == h :
            #print(c)
            return c
    return 0 
        #print(h,c)
    #print(count_leaks)




def pwn_check_pass(pass_char_real):
     #print(pass_char_real.encode('utf-8'))
     pass_hash=hashlib.sha1(pass_char_real.encode('utf-8')).hexdigest().upper()
     first_five_char,tail = pass_hash[:5] , pass_hash[5:]
     rsponse = request_api_data(first_five_char)
     return Get_Pass_Leak_Count(rsponse,tail)
     #return rsponse


#request_api_data("123")


#print(pwn_check_pass('1234#'))



def main(args):
    for passes in  args:
        response=pwn_check_pass(passes)
        if response == 0:
            print(f"Good Pass :{response}")
        else:
            print(f"Try to Change it: {response}")    



if __name__ == '__main__':
    print("hi main code")
    main(sys.argv[1:])


#main()