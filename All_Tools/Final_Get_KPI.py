
import sys
import re
import datetime
import xlsxwriter

if len(sys.argv) == 3:
    print('Only Three Arguments')
    Path_excel='C:/Users/m.ali/Desktop/write_list_6.xlsx'
    path_txt='C:/Users/m.ali/Desktop/Demo.txt'
else:
    print("okay")
    path_txt=sys.argv[4]
    Path_excel=sys.argv[3]



#print(date_generated)

List_File_Location=['C:/Users/m.ali/Zordoky/kpi_rf1_9_3_2022.txt','C:/Users/m.ali/Zordoky/kpi_rf2_9_3_2022.txt'
                   ,'C:/Users/m.ali/Gamal/kpi_rf1_9_3_2022.txt','C:/Users/m.ali/Gamal/kpi_rf2_9_3_2022.txt'
                   ,'C:/Users/m.ali/Crystal/kpi_rf1.txt','C:/Users/m.ali/Crystal/kpi_rf2.txt'
                   ,'C:/Users/m.ali/Ebn Elfared/kpi_rf1.txt','C:/Users/m.ali/Ebn Elfared/kpi_rf2.txt'
                   ,'C:/Users/m.ali/ShaheenPolice/kpi_rf1_9_3_2022.txt','C:/Users/m.ali/ShaheenPolice/kpi_rf2_9_3_2022.txt']











#print("number of arguments=%d"%len(sys.argv))

workbook = xlsxwriter.Workbook(Path_excel)
worksheet = workbook.add_worksheet('Sheet2')

date_format = "%Y-%m-%d"


a = datetime.datetime.strptime(sys.argv[1], date_format)
b = datetime.datetime.strptime(sys.argv[2], date_format)
delta = b - a
print (delta.days) # that's it

date_generated = [a + datetime.timedelta(days=x) for x in range(0, (b-a).days)]

#print(date_generated)



#for i,date in enumerate(date_generated):
    #print (date.strftime("%Y-%m-%d"))
    #worksheet.write(i+1, 0,date.strftime("%Y-%m-%d"))
    #worksheet.write(i+1, 1,'FAIL')

Count_Match=0

f = open(path_txt, "r") # Serial Meters
for index_1,x in enumerate(f):
    print("Look for Serial Meter:")
    print(x)
    Count_Match=0  # init count for new Serial
#Write Serial meter
    worksheet.write(0, index_1+1, x)
    #worksheet.write_column(1,index_1+1,'FAIL')
    #for ind in range(delta.days):
        #print(ind)
        #worksheet.write(ind+1,index_1+1,'FAIL')
    for index_reow,date_1_1 in enumerate(date_generated):
        worksheet.write(index_reow+1,index_1+1,'FAIL')
        pattern = re.compile(date_1_1.strftime("%Y-%m-%d")+" \S* \S*\s*\S* \SDONE\S \S* \S\d* \S*\s"+x)
        print("Pattern:")
        print(pattern)
#Count_All=0;
        
        for i, line in enumerate(open('C:/Users/m.ali/Desktop/kpi_plc_9_3_2022.txt')):
    #Count_All +=1
            for match in re.finditer(pattern, line):
                print ('Found on line %s: %s' % (i+1, match.group()))
                Count_Match+=1
        #worksheet.write(,1,'DONE')
                worksheet.write(index_reow+1,index_1+1,'DONE')

                print('LINE:%s'%(match.group()[:10]))
            
        
        
    print(x)
    print("match count=%d"%Count_Match)
    print("All_count=%d"%delta.days)
    print((Count_Match/delta.days)*100)
    worksheet.write(delta.days+1, index_1+1,(Count_Match/delta.days)*100)

    worksheet.write(delta.days+2, index_1+1,Count_Match)

    worksheet.write(delta.days+3, index_1+1,delta.days)
    

worksheet.write(delta.days+1, 0,'Percentage')
worksheet.write(delta.days+2, 0,'Done_Count')
worksheet.write(delta.days+3, 0,'Total_Count')
workbook.close()
f.close()




