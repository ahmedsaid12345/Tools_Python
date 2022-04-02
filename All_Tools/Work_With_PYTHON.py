import xlsxwriter

workbook = xlsxwriter.Workbook('C:/Users/m.ali/Desktop/write_list.xlsx')
worksheet = workbook.add_worksheet('Sheet1')

#my_list = [[1, 1, 1, 1, 1],
 #          [2, 2, 2, 2, 1],
  #         [3, 3, 3, 3, 1],
   #        [4, 4, 4, 4, 1],
    #       [5, 5, 5, 5, 1]]

#for row_num, row_data in enumerate(my_list):
 #   for col_num, col_data in enumerate(row_data):
#worksheet.write(0, 1, "ldsfjvhewrkjherkg")
#DATA_TUPLE=('FAIL')
for i in range(10):
    worksheet.write(i,1,'FAIL')


workbook.close()