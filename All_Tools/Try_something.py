
import re





file_attr="file_size-rw-r--r--   1 0        0         9565990 30 Mar 11:32 ?"
file_size=re.findall(r'\d+', file_attr)
print(int(file_size[3]))
