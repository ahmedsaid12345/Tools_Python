
import sys
import re
import datetime
import xlsxwriter





#print(date_generated)




Count_Match=0
print("Look for Serial Meter:")
#print(x)
Count_Match=0  # init count for new Serial

pattern = re.compile("SEE0031006665")
print("Pattern:")
print(pattern)
#Count_All=0;
        
for i, line in enumerate(open('C:/Users/m.ali/Desktop/plc_interface.txt')):
    #Count_All +=1
    for match in re.finditer(pattern, line):
        print ('Found on line %s: %s' % (i+1, match.group()))
        Count_Match+=1
        #worksheet.write(,1,'DONE')
            #    worksheet.write(index_reow+1,index_1+1,'DONE')

        print('LINE:%s'%(match.group()[:10]))
            
        
print("Count_Match:")        
print(Count_Match)