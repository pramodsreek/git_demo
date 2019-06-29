import pandas as pd
import xlrd
from colored import fg, bg, attr
# load the stock_info module from yahoo_fin
from yahoo_fin import stock_info as si

# get Apple's live quote price
try:
    price = si.get_live_price("ANsZ.AX")
    print (f'The price is {price}')
except ValueError as err:
    pass




#data = pd.read_excel ('ClientCapitalGainsRealised.xls') #for an earlier version of Excel, you may need to use the file extension of 'xls'
#df = pd.DataFrame(data, columns= ['Gain'])
#print (type(df))


ExcelFileName= 'ClientCapitalGainsRealised_24062019.xls'
workbook = xlrd.open_workbook(ExcelFileName)
worksheet = workbook.sheet_by_name("Details") # We need to read the data 
#from the Excel sheet named "Sheet1"
num_rows = worksheet.nrows #Number of Rows
num_cols = worksheet.ncols #Number of Columns
result_data =[]
#for curr_row in range(0, num_rows, 1):
for curr_row in range(0, num_rows):
    row_data = []
    #for curr_col in range(0, num_cols, 1):
    for curr_col in range(0, num_cols):
        data = worksheet.cell_value(curr_row, curr_col) # Read the data in the current cell
        #print(type(data))
        print(data)
        row_data.append(data.replace('$','').replace('(','-').replace(')',''))
    result_data.append(row_data)

total_discounted_realised = 0.0
total_discounted_discount_realised = 0.0
total_non_discounted_realised = 0.0
total_losses_realised = 0.0

total_discounted_unrealised = 0.0
total_discounted_discount_unrealised = 0.0
total_non_discounted_unrealised = 0.0
total_losses_unrealised = 0.0

#print("The type of result: ", type(result_data))

try:
    if (os.fileexists)

    else:
        print file doesn't exist
except expression as identifier:
    print there was file reading error

for company in result_data:
    #print('Company')
    #print (company)
    try:
        if company[-1] == 'R':
            if company[-2] == 'L':
                #print(company[0])
                total_losses_realised += float(company[1])
            elif company[-2] == 'D':
                total_discounted_realised += float(company[1])
                total_discounted_discount_realised += float(company[2])
            elif company[-2] == 'ND':
                total_non_discounted_realised += float(company[1])
        elif company[-1] == 'U':
            if company[-2] == 'L':
                #print(company[0])
                total_losses_unrealised += float(company[1])
            elif company[-2] == 'D':
                total_discounted_unrealised += float(company[1])
                total_discounted_discount_unrealised += float(company[2])
            elif company[-2] == 'ND':
                total_non_discounted_unrealised += float(company[1])
    except ValueError as identifier:
        pass
    

print (f'Realised Discounted Capital gains = {total_discounted_realised}')

print (f'Realised Discounted with discount (Taxable amount) = {total_discounted_discount_realised}')
print (total_discounted_discount_realised*2)
print (f'Realised Non Discounted Capital Gains Taxable = {total_non_discounted_realised}')
print (f'Realised Capital Losses to Offset = {total_losses_realised}')

#print (result_data)

print (f'Un Realised Discounted Capital gains = {total_discounted_unrealised}')

print (f'Un Realised Discounted with discount (Taxable amount) = {total_discounted_discount_unrealised}')
print (total_discounted_discount_unrealised*2)
print (f'Un Realised Non Discounted Capital Gains Taxable = {total_non_discounted_unrealised}')
print (f'Un Realised Capital Losses to Offset = {total_losses_unrealised}')

print ('%s Hello World !!! %s' % (fg(1), attr(0)))


print ('%s%s Hello World !!! %s' % (fg(1), bg(15), attr(0)))
