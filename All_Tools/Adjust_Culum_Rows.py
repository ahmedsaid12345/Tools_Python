import sys
import re
import datetime
import xlsxwriter
import time




#print(date_generated)

List_File_Location=['C:/Users/m.ali/Zordoky/kpi_rf1.txt','C:/Users/m.ali/Zordoky/kpi_rf2.txt']
                  # ,'C:/Users/m.ali/Gamal/kpi_rf1.txt','C:/Users/m.ali/Gamal/kpi_rf2.txt'
                  # ,'C:/Users/m.ali/Crystal/kpi_rf1.txt','C:/Users/m.ali/Crystal/kpi_rf2.txt'
                  # ,'C:/Users/m.ali/Ebn Elfared/kpi_rf1.txt'
                  # ,'C:/Users/m.ali/ShaheenPolice/kpi_rf1.txt','C:/Users/m.ali/ShaheenPolice/kpi_rf2.txt']

Names_OF_SITES=['Zordozy_RF1','Zordozy_RF2']
                #,'GAMAL_RF1','GAMAL_RF2'
                #,'Crstal_RF1','Crystal_RF2'
                #,'Ebn_Elfared_RF1'
                #,'Shaheen_Police_RF1','Shaheen_Police_RF2']

workbook = xlsxwriter.Workbook('C:/Users/m.ali/Desktop/write_list_8.xlsx')
worksheet = workbook.add_worksheet('Sheet1')



date_format = "%Y-%m-%d"


a = datetime.datetime.strptime(sys.argv[1], date_format)
b = datetime.datetime.strptime(sys.argv[2], date_format)
delta = b - a
print (delta.days) # that's it

date_generated = [a + datetime.timedelta(days=x) for x in range(0, (b-a).days)]







Count_Match=0
#print("Look for Serial Meter:")
#print(x)
Count_Match=0  # init count for new Serial
Count_Next=0
#Adjust Date

#Count_All=0;
Last_Active=0
Last_KPI=0
Line_Count=0
offset_1=0
Off_Set_Btw=0

for i_1,date_1 in enumerate(date_generated):
    i_13=i_1+1+offset_1+Off_Set_Btw
    worksheet.write(i_13, 0,date_1.strftime("%Y-%m-%d"))
    worksheet.write(i_13, 1,"ACTIVE")
    worksheet.write(i_13, 2,"KPI")
    

    i_2=i_13
    for pathe_file,name_location in zip(List_File_Location,Names_OF_SITES):
        offset_1+=1
        print("File Location:")
        print(pathe_file)
        #time.sleep(2)
        i_2+=1
        worksheet.write(i_2,0,name_location)
        worksheet.write(i_2,1,0)
        worksheet.write(i_2,2,0)

        with open(pathe_file,'r+') as f:
            Last_Active=0
            Last_KPI=0



            for i, line in enumerate(f):
    #Count_All +=1
            #worksheet.write(i_1+2, 0,date_1.strftime("%Y-%m-%d"))
                pattern = re.compile(date_1.strftime("%Y-%m-%d")+" \S* \S*\s*\S* KPI STATS:[\n]")
                #print("Pattern:")
                #print(pattern)
                for match in re.finditer(pattern, line):
        
                    print ('Found on line %s: %s' % (i+1, match.group()))

                    line_1 = f.__next__()

                    print('NEXT Line is %s :%s'%(i+2,line_1))
            #silicing

                    print("Get Active:")
                    #print(line_1[35:37])
                    Last_Active=re.findall(r'\d+', line_1)
                    #print("last_active=")
                    print(Last_Active)
                    print("Number we want:")
                    print(Last_Active[2])
            
                    print('NEXT Line is %s :%s'%(i+3,f.__next__()))
                    line_2=f.__next__()
                    print('NEXT Line is %s :%s'%(i+4,line_2))
                    print("Get Done")
                    print(line_2[16:18])
            #SIlincing
                    #Last_KPI=line_2[16:18]
                    Last_KPI=re.findall(r'\d+', line_2)
                    worksheet.write(i_2,1,int(Last_Active[2]))
                    worksheet.write(i_2,2,int(Last_KPI[1]))
            

                #Count_Match+=1
        print("Count_Match:")        
        print(Count_Match)

        print("Last Kpi:")
        print(Last_KPI)

        print("Last active:")
        #print(Last_Active[])
        
    Off_Set_Btw+=1     
            
        
print("Count_Match:")        
print(Count_Match)

print("Last Kpi:")
print(Last_KPI)

print("Last active:")
print(Last_Active)



workbook.close()

print("..........................................")
print("|                DONE                    |")
print("..........................................")


