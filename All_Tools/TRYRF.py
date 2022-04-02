import re
xc=re.findall(r'\d+', ' S05         61   762.5%        0     0.0%       61   762.5% ')

xv=xc[1]
print(xc)
print(type(int(xv)))
print(xv)


