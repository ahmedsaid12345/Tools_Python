#from lib2to3.pgen2.driver import Driver
from time import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
driver = webdriver.Chrome(executable_path="C:/Users/m.ali/Downloads/chromedriver_win32/chromedriver.exe",port=1234)
driver.get("http://192.168.4.97:8000")   #http://192.168.4.97:8000/#meters_plc
#driver.get("https://login.yahoo.com/")

#print(driver.page_source)
print("Session id"+driver.session_id)
#print("port"+driver.po)

url="http://192.168.4.97:8000/#dlms_tasks/add"
session_id=driver.session_id

print("Before Sleep")


time.sleep(20)

print("Wake UP")

driver.get("http://192.168.4.97:8000/#dlms_tasks")

#driver.get("http://192.168.4.97:8000/#dlms_tasks")


i=0
list_Meters=[    'SEE0000008000'
                ,'SEE0020000002'
                ,'SEE0020210015'
                ,'SEE0050000005'
                ,'SEE0060000006'
                ,'SEE0080000008']
for meter in list_Meters:

    while i < sys.argv[1]:
        driver.get("http://192.168.4.97:8000/#dlms_tasks/add")
        time.sleep(3)
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
        #with open(pathe_file,'r+') as f:
        Meters_textBox.send_keys(meter)
        Interface_textBox.send_keys("PLC")
        Operation_textBox.send_keys("GET")
        Class_textBox.send_keys("7")
        Obis_textBox.send_keys("1.0.99.1.0.255")
        Attr_textBox.send_keys("2")
        From_Data_textBox.send_keys("2022-04-12 07:00:00")
        To_Data_textBox.send_keys("2022-04-13 07:00:00")
        #//*[@id="form_dlms_tasks"]/div[1]/div/div/input

        Button_Click.click()
        i +=1



#login_1=driver.find_element_by_id("frmLogin_login")
#username_2 = login_1.find_element_by_name("username")
#username_1=login_1.find_element_by_name("password")

#username_1=driver.find_element_by_xpath(xpath="//form[@id='frmLogin_login']/div[1]/input")

#username_1=driver.find_element_by_xpath(xpath="//form[@id='frmLogin_login']/div[1]/input")
#username_1 =driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div[2]/form/div[1]/input")
#/html/body/div/div/div/div[2]/div/div/div[2]/form/div[1]/input
#frmLogin_login > div.form-group.mb-2 > input
#frmLogin_login > div.form-group.mb-2 > input
#frmLogin_login > div.form-group.mb-2 > input
#username_1.send_keys("admin")
#username_2.send_keys("admin")
#username_2.send_keys("admin")
#button_submit = login_1.find_element_by_class_name(".btn.btn-light.btn-sm.float-right.font-weight-bold").click()
#login_1.find_element_by_css_selector("button[type='submit']").click()


#upload_field = driver.find_element_by_xpath("//input[@type='file']")
#upload_field = driver.find_element_by_css_selector("input[name='filePath'][type='file']")
#login_1=driver.find_element_by_id("login-username")
#l=driver.find_element_by_class_name("form-control")


#login_1.send_keys("tbrt@admin")

#l=driver.find_element_by_name("password")
#driver.find_element_by_i
#l.send_keys("admin")
#driver.get("https://www.facebook.com/")
#l = driver.find_element_by_class_name("form-control")
#send input
#l.send_keys("Selenium")

#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service


#s=Service()




#driver.get()


#driver.get("http://selenium.dev")

print("Quitttttinggggggggggggggggggggggg")

driver.quit()




