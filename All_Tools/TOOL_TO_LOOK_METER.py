
import sys
import re
import datetime
import xlsxwriter

if len(sys.argv) == 3:
    print('Only Three Arguments')
    Path_excel='C:/Users/m.ali/Desktop/write_list_2.xlsx'
    path_txt='C:/Users/m.ali/Desktop/Demo.txt'
else:
    print("okay")
    path_txt=sys.argv[4]
    Path_excel=sys.argv[3]



#print("number of arguments=%d"%len(sys.argv))

workbook = xlsxwriter.Workbook(Path_excel)
worksheet = workbook.add_worksheet('Sheet2')

date_format = "%Y-%m-%d"


a = datetime.datetime.strptime(sys.argv[1], date_format)
b = datetime.datetime.strptime(sys.argv[2], date_format)
delta = b - a
print (delta.days) # that's it

date_generated = [a + datetime.timedelta(days=x) for x in range(0, (b-a).days)]





for i,date in enumerate(date_generated):
    print (date.strftime("%Y-%m-%d"))
    worksheet.write(i+1, 0,date.strftime("%Y-%m-%d"))
    #worksheet.write(i+1, 1,'FAIL')



f = open(path_txt, "r") # Serial Meters
for index_1,x in enumerate(f):
    print("Look for Serial Meter:")
    print(x)
#Write Serial meter
    worksheet.write(0, index_1+1, x)
    #worksheet.write_column(1,index_1+1,'FAIL')
    for ind in range(delta.days):
        print(ind)
        worksheet.write(ind+1,index_1+1,'FAIL')
    
    
    
    
    
    pattern = re.compile("\S* \S* \S*\s*\S* \SDONE\S \S* \S\d* \S*\s"+x)
    print("Pattern:")
    print(pattern)


#Count_All=0;
    Count_Match=0
    for i, line in enumerate(open('C:/Users/m.ali/Desktop/kpi_plc.txt')):
    #Count_All +=1
        for match in re.finditer(pattern, line):
            print ('Found on line %s: %s' % (i+1, match.group()))
            Count_Match+=1
        #worksheet.write(,1,'DONE')

            for i,date in enumerate(date_generated):
                if date.strftime("%Y-%m-%d") == match.group()[:10]:
                    print("found one at:%s"%date.strftime("%Y-%m-%d"))
                    print("I=%d"%i)
                    worksheet.write(i+1, index_1+1,'DONE')
                    
                    break

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




