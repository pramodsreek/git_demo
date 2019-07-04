#!/usr/bin/python3
"""
Author: Pramod S
Contact: @coderacademy.edu.au
Date: 2019/06/29
Licence: GPLv3
Version: 0.1
"""

import argparse
import os
import csv
import datetime as dt
from yahoo_fin import stock_info as si
import collections as collection
from colored import fg, bg, attr, stylize


def write_to_file(result, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['TICKER', 'Date of Purchase', 'Units', 'Cost Base', 'Unit Price', 'Value', 
'Capital Gain Non Discounted', 'Capital Gain Discounted', 'Capital Loss', 'Capital Gain Percentage', 'Capital Loss Percentage']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for x in range(len(result)): 
            writer.writerow(result[x])

def print_to_console(result):
    print("'TICKER', 'Date of Purchase', 'Units', 'Cost Base', 'Unit Price', 'Value', " + 
"'Capital Gain Non Discounted', 'Capital Gain Discounted', 'Capital Loss', 'Capital Gain Percentage', 'Capital Loss Percentage'")
    for x in range(len(result)): 
        row = ''
        for _, v in result[x].items():
            if (row == ''):
                row += v
            else:
                row = row + ',' + str(v)
        print(row)
#def add_unit_price(ticker):



def validate_price_file(reader):
    prices = {}
    ticker = ''
    price = 0.0
    for raw in reader:
        for k, v in raw.items():
            if (k is None) or (str(k).strip()=="") or (v is None) or (str(v).strip()==""): 
                raise Exception("Data in the price file is not valid! None of the values in the header or price data can be empty!")
            elif (k.lower() not in ('ticker','date','unit price')):
                raise Exception("Data in the price file is not valid! Please make sure the first row or header is correct. The header in the csv file should have 'ticker','date','unit price'")
            elif (k.lower() == 'ticker'):
                ticker = v
            elif (k.lower() == 'date'):
                try:
                    dt.datetime.strptime(v, '%d/%m/%Y')
                except ValueError:
                    raise Exception("Incorrect date format, should be DD/MM/YYYY")
            elif (k.lower() == 'unit price'):
                price = v
                try:
                    float(v)
                except ValueError:
                    raise Exception("Cost base should be float!")
        prices[ticker] = price
    return prices

def convert_price_file_to_dict(filename):
    exists = os.path.isfile(filename)
    if exists:
        reader = csv.DictReader(open(filename))
        return validate_price_file(reader)
    else:
        raise Exception(f'The file {filename} does not exist.')


def validate_share_file_data(reader):

    #fmt = ('%d/%m/%Y')
    for raw in reader:
        
        for k, v in raw.items():
            if (k is None) or (str(k).strip()=="") or (v is None) or (str(v).strip()==""): 
                raise Exception("Data in the share file is not valid! None of the values in the header or share data can be empty!")
            elif (k.lower() not in ('ticker','date of purchase','units','cost base')):
                raise Exception("Data in the share file is not valid! Please make sure the first row or header is correct. The header in the csv file should have 'ticker','date of purchase','units','cost base'")
            elif (k.lower() == 'date of purchase'):
                try:
                    dt.datetime.strptime(v, '%d/%m/%Y')
                except ValueError:
                    raise Exception("Incorrect data format, should be DD/MM/YYYY")
            elif (k.lower() == 'cost base'):
                try:
                    float(v)
                except ValueError:
                    raise Exception("Cost base should be float!")
            elif (k.lower() == 'Units'):
                try:
                    int(v)
                except ValueError:
                    raise Exception("Units should be int!")
    return True

def get_most_recent_share_price(ticker):
    # get Apple's live quote price
    try:
        
        price = si.get_live_price(ticker)
        #price = si.get_live_price("ANZ.AX")
        
        return price
    except ValueError:
        raise Exception("Error retrieving data from ASX. Please check the file to check errors with data. If unit prices can be retrieved manually, Please provide it in a file.")

def get_recent_share_price(ticker, pricereader):
    # get Apple's live quote price
    try:
        price = 0
        print("adfffffffffffffffffffffffffffffffffffff")
        print(type(pricereader))
        for raw in pricereader:
            print("adfffffffffffffffffffffffffffffffffffff")
            print(type(raw))
            for k, v in raw.items():
                if (k.lower() == 'ticker' and v.lower() != ticker.lower()):
                    pass

                if (k.lower() == 'unit price'):
                    price = v
        return price
    except ValueError:
        raise Exception("Error retrieving data from csv price file. Please check the files to validate data. Please provide it in a file with corrected data.")



def convert_share_file_to_dict(filename):
    exists = os.path.isfile(filename)
    if exists:
        print("The file exists")
        reader = csv.DictReader(open(filename))
        #validate_share_file_data(reader)
        return reader
    else:
        raise Exception(f'The file {filename} does not exist.')

def add_live_unit_price_share_hold(reader, price_file = None):
    #Calculate the capital gains discounted, capital gains non-discounted and loses. Discounts are calculated based on the date of purchase and based on Australian Taxation Offices capital gains discounting process.
    #Calculate the percentage gains or loses based on the ticker + Date of purchase + Units. There will be option of writing the output to a file.
    
    #pricereader = ""
    
    
    print(price_file)

    all_units_with_calculations = []
    for raw in reader:
        new_dict_values = collection.OrderedDict()
       
        
        unit_price = 0
        number_of_units = 0
        cost_base = 0
        capital_gain_discounted = 0
        capital_gain_nondiscounted = 0
        capital_loss = 0
        todays_date = dt.datetime.now()
        date_of_purchase = dt.datetime.strptime('04/07/2019', '%d/%m/%Y')
        capital_gain_percentage = 0
        capital_loss_percentage = 0
        for k, v in raw.items():
            
            new_dict_values[k]=v
            if (k.lower() == 'ticker'):
                try:
                    if (price_file != None):
                        for p,r in price_file.items():
                            if(p.lower() == v.lower()):
                                unit_price = float(r)
                    else:
                        unit_price = get_most_recent_share_price(v+'.AX')
                except Exception as e:
                    raise e
                
                
                
            elif (k.lower() == 'units'):
                number_of_units = float(v)   
            elif (k.lower() == 'cost base'):
                cost_base = float(v)
            elif (k.lower() == 'date of purchase'):
                date_of_purchase = dt.datetime.strptime(v, '%d/%m/%Y')
            else:
                continue
        
        new_dict_values['Unit Price'] = round(unit_price,3)
        new_dict_values['Value'] = round(unit_price * number_of_units, 3)
        capital_gain_loss = (unit_price * number_of_units) -  cost_base
        days_held = (todays_date - date_of_purchase).days
        if (capital_gain_loss >= 0):
            capital_gain_nondiscounted = capital_gain_loss
            capital_gain_percentage = (capital_gain_nondiscounted/cost_base)*100
            capital_loss_percentage = 0
            capital_loss = 0
            if (days_held > 365):
                capital_gain_discounted = capital_gain_loss/2
            else:
                capital_gain_discounted = 0
        else:
            capital_loss = capital_gain_loss
            capital_gain_discounted = 0
            capital_gain_nondiscounted = 0
            capital_loss_percentage = (capital_loss/cost_base)*100
        new_dict_values['Capital Gain Non Discounted'] = round(capital_gain_nondiscounted,3)
        new_dict_values['Capital Gain Discounted'] = round(capital_gain_discounted,3)
        new_dict_values['Capital Loss'] = round(capital_loss,3)   
        new_dict_values['Capital Gain Percentage'] = round(capital_gain_percentage,3)
        new_dict_values['Capital Loss Percentage'] = round(capital_loss_percentage,3)
        #new_dict_values.update(raw)
        all_units_with_calculations.append(new_dict_values)
    return all_units_with_calculations



    


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Personal Shareholding Performance')
    parser.add_argument('-i','--input', help='Input file name that contains a persons shareholding.The file should be in CSV format.', required=True)
    parser.add_argument('-o','--output', help='Output file name where the performance data should be stored. If this option is not used, performance data will be printed on console.', default="stdout")
    parser.add_argument('-p','--price', help='If a specific unit price should be used for understanding performance, it can be provided as input. This option can also be used if recent unit price cannot be retrieved from internet.')
    args = parser.parse_args()

    

    try:
        share_file = convert_share_file_to_dict(args.input)
        price_file = convert_price_file_to_dict(args.price)
        result = add_live_unit_price_share_hold(share_file, price_file)
        write_to_file(result, args.output)
        print_to_console(result)
    except Exception as err:
        #print(str(err))
        error_text_format = fg("white") + attr("bold") + bg("red")
        print(stylize(str(err), error_text_format))
    
    
    

