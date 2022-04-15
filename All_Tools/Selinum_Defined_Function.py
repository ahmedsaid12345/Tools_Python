from logging import exception
from time import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

from sqlalchemy import false, true


i=0
list_Meters=[    'SEE0000008000'
                ,'SEE0020000002'
                ,'SEE0020210015'
                ,'SEE0050000005'
                ,'SEE0060000006'
                ,'SEE0080000008']



date_from =   "2022-04-13 07:00:00"
date_to   =   "2022-04-14 07:00:00"



def Login_Function():
    global driver
    driver = webdriver.Chrome(executable_path="C:/Users/m.ali/Downloads/chromedriver_win32/chromedriver.exe",port=1234)
    driver.get("http://192.168.4.97:8000")  
    print(driver.page_source)
    print("Sleep..")
    time.sleep(5) #time to sleep 5 SEC to Load Page
    print("Wake UP..")
    print(driver.page_source)
    try:
        username_2 = driver.find_element_by_name("username")
        username_1= driver.find_element_by_name("password")
        bttn=driver.find_element_by_xpath("//button[@type='submit']")
   
    except Exception as e :
        print("No such element Found"+e.__str__())
        return false

    username_1.send_keys("admin")
    username_2.send_keys("admin")
    
    bttn.click()
    return true



def Core_Algo_Function(Obis_Code,Class_Code,Attr_Code="2",from_date="2022-04-13 07:00:00",to_date="2022-04-14 07:00:00",num_iter=5):
    i=0
    while i < num_iter:
    #for meter in list_Meters:
        #print(meter)
        
        #i=0
        for meter in list_Meters:
            print(meter)
        
        #while i < num_iter:
            driver.get("http://192.168.4.97:8000/#dlms_tasks/add")
            time.sleep(2) #wait 2 SEC To Load All Elements
            print("Sleeping.............")
            # Find All Elements
            Meters_textBox=driver.find_element_by_name("meters")
            Interface_textBox=driver.find_element_by_name("interfaace")
            Operation_textBox=driver.find_element_by_name("op_type")
            Class_textBox=driver.find_element_by_name("op_iclass") 
            Obis_textBox=driver.find_element_by_name("op_obis")
            Attr_textBox=driver.find_element_by_name("op_attr")
            From_Data_textBox=driver.find_element_by_name("sel_from")
            To_Data_textBox=driver.find_element_by_name("sel_to")
            Button_Click=driver.find_element_by_id("btn_submit_dlms_tasks")

            #Send Elements to Text Box
            Meters_textBox.send_keys(meter)
            Interface_textBox.send_keys("PLC")
            Operation_textBox.send_keys("GET")
            Class_textBox.send_keys(Class_Code)
            Obis_textBox.send_keys(Obis_Code)
            Attr_textBox.send_keys(Attr_Code)
            From_Data_textBox.send_keys(from_date)
            To_Data_textBox.send_keys(to_date)
            print("Start to see")
            time.sleep(5)            ######### Used for Debugging 
            Button_Click.click()

        i +=1 #Next Iteration


##############################################
  #Profile Generic 1
  #class: 7
  #obis: 1.0.99.1.0.255
    #attr: 2
#################################################    
def Get_Load_Profile(numiter=5):
    Core_Algo_Function("1.0.99.1.0.255","7","2",date_from,date_to,numiter)


##################################33
#serial
#class: 1
#obis: 0.0.96.1.4.255
#attr: 2
#################################################3

def Get_Serial_Meter(num_iter=5):
    Core_Algo_Function("0.0.96.1.4.255","1","2",date_from,date_to,num_iter)


##################################33
#Comsumption
#class: 3
#obis: 1.0.1.8.0.255
#attr: 2
#################################################3

def Get_Consumption(num_iter=5):
    Core_Algo_Function("1.0.1.8.0.255","3","2",date_from,date_to,num_iter)


def Start_Operation():
    Login_Function()
    Get_Load_Profile(10)
    Get_Serial_Meter(2)
    Get_Consumption(2)

   
    
if __name__=="main":
    Start_Operation()
    print("..........QUITTing.......")
    driver.quit()
    print("***************************************************")
    print("                  DONE                             ")
    print("***************************************************")

