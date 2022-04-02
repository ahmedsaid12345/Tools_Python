
import sys
import re
import datetime
import xlsxwriter


Path_excel='C:/Users/m.ali/Desktop/Hybrid_Status_20_3_2022_2.xlsx'
path_txt='C:/Users/m.ali/Desktop/Serial_Hybrid.txt' #File Contain Serial meter




#print("number of arguments=%d"%len(sys.argv))

workbook = xlsxwriter.Workbook(Path_excel)

worksheet_1 = workbook.get_worksheet_by_name('Sheet2')
worksheet_1.write_row(0,0,'xyz')
#worksheet_1.write(20,2,100)

