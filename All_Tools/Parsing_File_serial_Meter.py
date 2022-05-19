import re
import datetime
import sys

##sys.argv[1]=start date

##sys.argv[2]=end date
##sys.argv[3]= meter Serial 
##

if len(sys.argv) == 4:
    print('Only Three Arguments')
    Kpi_File_Path='C:/Users/m.ali/All_Sites/Shaheen_Elsour/kpi_plc_1.txt'
    output_file='C:/Users/m.ali/Desktop/output.txt'

else:
    print("Error")
    sys.exit(1)


OUTPUT_STR=[]
date_format = "%Y-%m-%d"
a = datetime.datetime.strptime(sys.argv[1], date_format)
b = datetime.datetime.strptime(sys.argv[2], date_format)
delta = b - a
print (delta.days) # that's it
date_generated = [a + datetime.timedelta(days=x) for x in range(0, delta.days)]
for index_reow,date_1_1 in enumerate(date_generated):
        #worksheet.write(index_reow+1 +offset_try,index_1+1,'FAIL')
        pattern = re.compile(date_1_1.strftime("%Y-%m-%d")+" [^!]* "+sys.argv[3]+"[^!]*")
        print("Pattern:")
        print(pattern)
        #with open(output_file, 'a') as output_1:
    #f.writelines(lines)
        for i, line in enumerate(open(Kpi_File_Path)):
        #Count_All +=1
            for match in re.finditer(pattern, line):
                print ('Found on line %s: %s' % (i+1, match.group()))
                    #output_1.write(match.group())
                OUTPUT_STR.append(match.group())
                #OUTPUT_STR.append(match.end())



print(OUTPUT_STR)

with open(output_file, 'w') as f_1_1:
    f_1_1.write('\n'.join(OUTPUT_STR))





def main():
    pass



if __name__=="main":
    main()
