

import sys
import re
import datetime
import xlsxwriter
import time


Shift_day = 0

if len(sys.argv) == 3:
    print('Only Three Arguments')
    #Path_excel='C:/Users/m.ali/Desktop/GAMAL_RF1_Status_22_3_2022_2.xlsx'
    Path_excel='C:/Users/m.ali/Desktop/Hybrid_2271_4244.xlsx'
    #Path_excel_Retry='C:/Users/m.ali/Desktop/Hybrid_2271_5.xlsx'
    path_txt='C:/Users/m.ali/Desktop/Serial_Hybrid.txt' #File Contain Serial meter
    #path_txt='C:/Users/m.ali/Desktop/Gamal_RF1_Serial.txt'
    Kpi_File_Path='C:/Users/m.ali/All_Sites/Shaheen_Elsour/kpi_plc'+ datetime.datetime.strftime(datetime.datetime.now() - datetime.timedelta(Shift_day),'%d-%m-%Y')+'.txt'
   # Kpi_File_Path = 'C:/Users/m.ali/All_Sites/GAMAL/kpi_rf1.txt'
    
else:
    print("okay")
    path_txt=sys.argv[4]
    Path_excel=sys.argv[3]



#print("number of arguments=%d"%len(sys.argv))

workbook = xlsxwriter.Workbook(Path_excel)
#workbook_Retry = xlsxwriter.Workbook(Path_excel_Retry)

worksheet = workbook.add_worksheet('Done OR Failed')
worksheet_Retry = workbook.add_worksheet("NUM OF Retry")
#worksheet_1= workbook.get_worksheet_by_name('Sheet2')
date_format = "%Y-%m-%d"
offset_try = 0
#worksheet_1.write(0,0,1)
#worksheet_1.write(100,1,1000)
a = datetime.datetime.strptime(sys.argv[1], date_format)
b = datetime.datetime.strptime(sys.argv[2], date_format)
delta = b - a
print (delta.days) # that's it

date_generated = [a + datetime.timedelta(days=x) for x in range(0, (b-a).days)]

#print(date_generated)



for i,date in enumerate(date_generated):
    print (date.strftime("%Y-%m-%d"))
    worksheet.write(i+1+offset_try, 0,date.strftime("%Y-%m-%d"))  #######33
    worksheet_Retry.write(i+1+offset_try, 0,date.strftime("%Y-%m-%d"))  #######33
    
    #worksheet.write(i+1, 1,'FAIL')


#workbook.close()
#workbook_Retry.close()
#exit(0)
#Count_Match=0

f = open(path_txt, "r") # Serial Meters
for index_1,x in enumerate(f):
    print("Look for Serial Meter:")
    print(x)
    Count_Match=0  # init count for new Serial
    
#Write Serial meter
    worksheet.write(0+offset_try, index_1+1, x)
    worksheet_Retry.write(0+offset_try, index_1+1, x)
    #worksheet.write_column(1,index_1+1,'FAIL')
    #for ind in range(delta.days):
        #print(ind)
        #worksheet.write(ind+1,index_1+1,'FAIL')
    for index_reow,date_1_1 in enumerate(date_generated):
        num_Retries =0 # Reset init Counter For every meter.
        worksheet.write(index_reow+1 +offset_try,index_1+1,'Not_Exist')
        worksheet_Retry.write(index_reow+1 +offset_try,index_1+1,'Not_Exist')
        pattern = re.compile(date_1_1.strftime("%Y-%m-%d")+" \S* \S*\s*\S* \S\\b(?:DONE|FAILED)\\b\S \S* \S\d* \S*\s"+x.rstrip('\n'))
        print("Pattern:")
        print(pattern)
        #time.sleep(3)
#Count_All=0;
        
        for i, line in enumerate(open(Kpi_File_Path)):
            #print("line in file:"+line)
    #Count_All +=1
            #time.sleep(3)

            for match in re.finditer(pattern, line):
                print ('Found on line %s: %s' % (i+1, match.group()))
                Count_Match+=1
                print("line=")
                print(line)
                #time .sleep(8)
        #worksheet.write(,1,'DONE')

                if "FAILED" in match.group():
                    print("Increase Num of Retries....")
                    
                    num_Retries +=1
                    worksheet.write(index_reow+1+offset_try,index_1+1,'FAILED')
                    worksheet_Retry.write(index_reow+1+offset_try,index_1+1,num_Retries)                
                else:
                    print("Sure it's Done...")
                    worksheet.write(index_reow+1+offset_try,index_1+1,'DONE')
                    worksheet_Retry.write(index_reow+1+offset_try,index_1+1,num_Retries)
                    print('LINE:%s'%(match.group()[:10]))
                    
                    #find Done Task we should Break Here Right.....




               
            
        
        
    print(x)
    print("match count=%d"%Count_Match)
    print("All_count=%d"%delta.days)
    print((Count_Match/delta.days)*100)
    worksheet.write(delta.days+1+offset_try, index_1+1,(Count_Match/delta.days)*100)

    worksheet.write(delta.days+2+offset_try, index_1+1,Count_Match)

    worksheet.write(delta.days+3+offset_try, index_1+1,delta.days)
    

#worksheet.write(delta.days+1 +offset_try, 0,'Percentage')
#worksheet.write(delta.days+2+offset_try, 0,'Done_Count')
#worksheet.write(delta.days+3+offset_try, 0,'Total_Count')
workbook.close()
#workbook_Retry.close()
f.close()




