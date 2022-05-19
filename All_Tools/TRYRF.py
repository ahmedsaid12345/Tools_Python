import re

#from jmespath import search
#xc=re.findall(r'\d+', ' S05         61   762.5%        0     0.0%       61   762.5% ')

#xv=xc[1]
#print(xc)
#print(type(int(xv)))
#print(xv)
x = 'SEE0031003493\n'
search_pattern="2022-04-20 02:03:25,234 INFO  [plc] (DONE) task S05 for SEE0031003493"

pat_1 = re.compile('2022-04-20'+" \S* \S*\s*\S* \S\\b(?:DONE|FAILED)\\b\S \S* \S\d* \S*\s"+x.rstrip('\n'))
print(pat_1)      
for match in re.finditer(pat_1,search_pattern):
     print ('Found on line %s' %(match.group()))

     if "FAILED" in match.group() :
        print("Dude found it")

     else:
        print(" May be this Done")


print("not exist")









