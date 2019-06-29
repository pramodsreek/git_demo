# load the stock_info module from yahoo_fin
from yahoo_fin import stock_info as si

# get Apple's live quote price
price = si.get_live_price("ANZ.AX")


print (price)