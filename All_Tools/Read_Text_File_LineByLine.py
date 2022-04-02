f = open("C:/Users/m.ali/Desktop/Demo.txt", "r")
count_l=0
for x in f:
  print(x)
  count_l+=1
f.close()

print(count_l)