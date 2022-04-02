
import sys
import re
import datetime
import xlsxwriter





#print(date_generated)




Count_Match=0
print("Look for Serial Meter:")
#print(x)
Count_Match=0  # init count for new Serial
Count_Next=0
pattern = re.compile("2022-03-01 \S* \S*\s*\S*\sstarting task\s\S*\s\S*\s\S* \S* \S*\sSEE0031014870[^!]*")
print("Pattern:")
print(pattern)
#Count_All=0;
Line_Count=0        
for i, line in enumerate(open('C:/Users/m.ali/Desktop/Count_Next_Finished.txt')):
    #Count_All +=1
    for match in re.finditer(pattern, line):
        
        print ('Found on line %s: %s' % (i+1, match.group()))
        Count_Match+=1
        pattern_count= re.compile("2022-03-01 \S* DEBUG \S*\s\S* GET-NEXT\S 0x\S*")
        Line_Count=i+1
        for match_count in re.finditer(pattern_count,Line_Count):
            
            print ('Found on line %s: %s' % ( match_count.group()))
            print('Find Count')
            Count_Match+=1
        
        #worksheet.write(,1,'DONE')
            #    worksheet.write(index_reow+1,index_1+1,'DONE')

        #print('LINE:%s'%(match.group()[:10]))
            
        
print("Count_Match:")        
print(Count_Match)

print("Line_Count:")        
print(Line_Count)