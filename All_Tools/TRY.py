#class a:
 #   def __init__(self,x=0):
  #      self.x=x


   # def func1(self):
    #    self.x +=1    

#class b(a):
 #   def __init__(self, y=0):
  #      a.__init__(self,3)
   #     self.y=y

    #def func1(self):
     #     self.y +=1    


#b_1=b()
#b_1.func1()
#print(b_1.x,b_1.y)





from time import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
driver = webdriver.Chrome(executable_path="C:/Users/m.ali/Downloads/chromedriver_win32/chromedriver.exe",port=1234)
driver.get("http://192.168.4.97:8000")   #http://192.168.4.97:8000/#meters_plc
#driver.get("https://login.yahoo.com/")

print(driver.page_source)

print("Sleep..")
time.sleep(8)

print("Wake UP..")


print(driver.page_source)

username_2 = driver.find_element_by_name("username")
username_1= driver.find_element_by_name("password")

username_1.send_keys("admin")
username_2.send_keys("admin")
#button_submit = driver.find_element_by_class_name(".btn").click()
bttn=driver.find_element_by_xpath("//button[@type='submit']")

bttn.click()

#print("Quitttttinggggggggggggggggggggggg")


#Load Pages OF Tasks

time.sleep(5)


list_Meters_1=[    'SEE0000008000'
                ,'SEE0020000002'
                ,'SEE0020210015'
                ,'SEE0050000005'
                ,'SEE0060000006'
                ,'SEE0080000008']




list_Meters=[   'SEE0000000066'
                ,'SEE0000007732'
                ,'SEE0000020029'
                ,'SEE0020000002'
                ,'SEE0020210015'
                ,'SEE0050000005'
                ,'SEE0060000006'
                ,'SEE0080000008'                
                ]




print("Enter 1- Load Profile ")

print("2- Consumption")

#x=input("Enter\n\t1-Load Profile\n\t2-Consumption")
#load Profile
#if x== 1:
 #   obis_1 = "1.0.99.1.0.255"
  #  class_1 = "7"

# Consumtion
#else:
 #   obis_1 = "1.0.1.8.0.255"
  #  class_1 = "3"


num_iter = 1

for meter in list_Meters:
    print(meter)
    #time.sleep(3)
    i=0

    while i < num_iter:
        driver.get("http://192.168.4.97:8000/#dlms_tasks/add")
        time.sleep(2)
        print("Sleeping.............")
        #print(driver.page_source)


        Meters_textBox=driver.find_element_by_name("meters")
        Interface_textBox=driver.find_element_by_name("interfaace")
        Operation_textBox=driver.find_element_by_name("op_type")
        Class_textBox=driver.find_element_by_name("op_iclass") 
        Obis_textBox=driver.find_element_by_name("op_obis")
        Attr_textBox=driver.find_element_by_name("op_attr")

        From_Data_textBox=driver.find_element_by_name("sel_from")
        To_Data_textBox=driver.find_element_by_name("sel_to")
        Button_Click=driver.find_element_by_id("btn_submit_dlms_tasks")

        #btn_submit_dlms_tasks

        #print(ll.parent)
        

        Meters_textBox.send_keys(meter)
        Interface_textBox.send_keys("PLC")
        Operation_textBox.send_keys("GET")
        Class_textBox.send_keys("7")
        Obis_textBox.send_keys("1.0.99.1.0.255")
        Attr_textBox.send_keys("2")
        From_Data_textBox.send_keys("2022-04-13 07:00:00")
        To_Data_textBox.send_keys("2022-04-14 07:00:00")
        #//*[@id="form_dlms_tasks"]/div[1]/div/div/input

        Button_Click.click()
        i +=1
    obis_1 = "1.0.1.8.0.255"
    class_1 = "3"



for meter in list_Meters:
    #print(meter)
    #time.sleep(3)
    i=0

    while i < 3:
        driver.get("http://192.168.4.97:8000/#dlms_tasks/add")
        time.sleep(2)
        print("Sleeping.............")
        #print(driver.page_source)


        Meters_textBox=driver.find_element_by_name("meters")
        Interface_textBox=driver.find_element_by_name("interfaace")
        Operation_textBox=driver.find_element_by_name("op_type")
        Class_textBox=driver.find_element_by_name("op_iclass") 
        Obis_textBox=driver.find_element_by_name("op_obis")
        Attr_textBox=driver.find_element_by_name("op_attr")

        From_Data_textBox=driver.find_element_by_name("sel_from")
        To_Data_textBox=driver.find_element_by_name("sel_to")
        Button_Click=driver.find_element_by_id("btn_submit_dlms_tasks")

        #btn_submit_dlms_tasks

        #print(ll.parent)
        

        Meters_textBox.send_keys(meter)
        Interface_textBox.send_keys("PLC")
        Operation_textBox.send_keys("GET")
        Class_textBox.send_keys("3")
        Obis_textBox.send_keys("1.0.1.8.0.255")
        Attr_textBox.send_keys("2")
        From_Data_textBox.send_keys("2022-04-13 07:00:00")
        To_Data_textBox.send_keys("2022-04-14 07:00:00")
        #//*[@id="form_dlms_tasks"]/div[1]/div/div/input

        Button_Click.click()
        i +=1
    #obis_1 = "1.0.1.8.0.255"
    #class_1 = "3"



for meter in list_Meters:
    #print(meter)
    #time.sleep(2)
    i=0

    while i < 3:
        driver.get("http://192.168.4.97:8000/#dlms_tasks/add")
        time.sleep(2)
        print("Sleeping.............")
        #print(driver.page_source)


        Meters_textBox=driver.find_element_by_name("meters")
        Interface_textBox=driver.find_element_by_name("interfaace")
        Operation_textBox=driver.find_element_by_name("op_type")
        Class_textBox=driver.find_element_by_name("op_iclass") 
        Obis_textBox=driver.find_element_by_name("op_obis")
        Attr_textBox=driver.find_element_by_name("op_attr")

        From_Data_textBox=driver.find_element_by_name("sel_from")
        To_Data_textBox=driver.find_element_by_name("sel_to")
        Button_Click=driver.find_element_by_id("btn_submit_dlms_tasks")

        #btn_submit_dlms_tasks

        #print(ll.parent)
        

        Meters_textBox.send_keys(meter)
        Interface_textBox.send_keys("PLC")
        Operation_textBox.send_keys("GET")
        Class_textBox.send_keys("1")
        Obis_textBox.send_keys("0.0.96.1.4.255")
        Attr_textBox.send_keys("2")
        From_Data_textBox.send_keys("2022-04-13 07:00:00")
        To_Data_textBox.send_keys("2022-04-14 07:00:00")
        #//*[@id="form_dlms_tasks"]/div[1]/div/div/input

        Button_Click.click()
        i +=1
    #obis_1 = "1.0.1.8.0.255"
    #class_1 = "3"





print("Quitttttinggggggggggggggggggggggg")

driver.quit()



























#driver.quit()
































































