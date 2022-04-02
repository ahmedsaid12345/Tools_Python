from datetime import datetime
date_format = "%Y-%m-%d"
a = datetime.strptime('2008-08-18', date_format)
b = datetime.strptime('2008-09-26', date_format)
delta = b - a
print (delta.days) # that's it