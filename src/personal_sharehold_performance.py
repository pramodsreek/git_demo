#!/usr/bin/python3
"""
Module: Personal Share Holding Performance Check
Author: Pramod S
Contact: coderacademy
Date: 2019/06/29
Licence: GPLv3
Version: 0.1

Personal Share Holding Performance is a tool that can summarise the value of share portfolio
for a single user.
The user should provide a file input with all the shares that user holds. The csv(comma
separated file) file should contain the following data in the format below.

TICKER,Date of Purchase,Units,Cost Base
ALQ,13/12/2008,10,190.71
ALU,14/12/2008,10,377
ALX,15/12/2008,10,88.87

If the user wishes to calculate the total value of share holding based on a price, then a
price file should be provided in the following format.

TICKER,Date,Unit Price
ALQ,1/07/2019,19.071
ALU,1/07/2019,37.7
ALX,1/07/2019,8.887

All the file should be in the current folder and should have permissions to read.

If the user wishes to write the output to a file, then the output filename should be provided.

The arguments should be passed in the following format. The output file is written to current
directory and permission to write file is required.

python3 personal_sharehold_performance.py -i Capitalgains.csv -p Shareprice.csv -o output.csv

If no price file is provided, the price will be retrieved using yahoo finance. This can only
work for ASX shares.

The summary of output will have the following details.
****** Summary of Share Holding - These are unrealised values ******
Total Cost Base of Share Holding : 1617.21
Total Value of Share Holding : 2100.4
Total Units of Share Holding : 150.0
Total Capital Gain that is not Discounted : 1164.59
Total Capital Gain that is Discounted : 582.295
Total Capital Losses : -681.4



"""

import argparse
import os
import csv
import datetime as dt
import collections as collection
from yahoo_fin import stock_info as si
from colored import fg, bg, attr, stylize

class ShareCalculationException(Exception):
    """
    Defining a customised exception
    """
    #pass

def write_to_file(calculations, filename):
    """
        Writes output to a file. (An Ordered Dictionary data structure is used.)

        Keyword arguments:
        calculations -- an ordered dictionary of each share details as a row
        filename -- The output file

    """
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = [
            'TICKER', 'Date of Purchase', 'Units', 'Cost Base', 'Unit Price', 'Value',
            'Capital Gain Non Discounted', 'Capital Gain Discounted', 'Capital Loss',
            'Capital Gain Percentage', 'Capital Loss Percentage']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row_cal in range(len(calculations)):
            writer.writerow(calculations[row_cal])

def print_to_console(display_rows):
    """
        Writes output to a console.

        Keyword arguments:
        display_rows -- an ordered dictionary of each share details as a row

    """
    print('*************************************')
    head_er = (
        "'TICKER', 'Date of Purchase', 'Units', 'Cost Base', 'Unit Price', 'Value', " +
        "'Capital Gain Non Discounted', 'Capital Gain Discounted', 'Capital Loss', " +
        "'Capital Gain Percentage', 'Capital Loss Percentage'")
    print(head_er)
    for csv_row_index in range(len(display_rows)):
        row = ''
        for _, row_line in display_rows[csv_row_index].items():
            if row == '':
                row += row_line
            else:
                row = row + ',' + str(row_line)
        print(row)
    print('*************************************')



def validate_price_file_ret_dict(reader):
    """
        Validate input price file and if valid return dictionary of all prices. A dictionary is
        used to store the prices to avoid reading the file multiple time. This does not have to
        be ordered, as the output is not used for writing to a file or console. This method is
        used to validate the contents of input file to avoid unnecessary calls to external
        finance interfaces. If there is an issue with the content, an exception will be thrown
        and the calling module should handle the exception.

        Keyword arguments:
        reader -- A Ordered Dictionary reader was used, as it provided the functionality to load
        contents of csv file and maintain the order.

    """
    prices = {}
    ticker = ''
    price = 0.0
    for raw in reader:
        for tick, pric in raw.items():
            if (tick is None) or (str(tick).strip() == "") or (pric is None) or (str(pric).strip() == ""):
                raise ShareCalculationException(
                    "Data in the price file is not valid! None of the values in " +
                    "the header or price data can be empty!")
            elif tick.lower() not in ('ticker', 'date', 'unit price'):
                raise ShareCalculationException(
                    "Data in the price file is not valid! Please make sure the " +
                    "first row or header is correct. The header in the csv file " +
                    "should have 'ticker','date','unit price'")
            elif tick.lower() == 'ticker':
                ticker = pric
            elif tick.lower() == 'date':
                try:
                    dt.datetime.strptime(pric, '%d/%m/%Y')
                except ValueError:
                    raise ShareCalculationException("Incorrect date format, should be DD/MM/YYYY")
            elif tick.lower() == 'unit price':
                price = pric
                try:
                    float(pric)
                except ValueError:
                    raise ShareCalculationException("Cost base should be float!")
        prices[ticker] = price
    return prices

def convert_price_file_to_dict(filename):
    """
        Converts the input price file to a dictionary. The order is not important, but DictReader
        was used, as it is a superior utility to read a csv file.

        Keyword arguments:
        file -- Name of the share price file provided by the user.
    """
    exists = os.path.isfile(filename)
    if exists:
        reader = csv.DictReader(open(filename))
    else:
        raise ShareCalculationException(f'The file {filename} does not exist.')
    return validate_price_file_ret_dict(reader)

def get_most_recent_share_price(ticker):
    """
        Gets the most recent share price using yahoo finance. Only ASX shares are checked.
        If there is an issue with the ticker or fetching the data, an exception is thrown.
        #price = si.get_live_price("ANZ.AX")

        Keyword arguments:
        ticker -- Ticker is the short code for ASX listed company.
    """

    try:
        price = si.get_live_price(ticker)
        return price
    except ValueError:
        raise ShareCalculationException(
            "Error retrieving data from ASX. Please check the file to find errors with data. " +
            "If unit prices can be retrieved manually, Please provide it in a file.")



def print_to_console_summary(t_cost_base, t_value, t_units, t_capital_gain_ndiscounted, t_capital_gain_discounted, t_capital_loss):
    """
        Prints summary of share portfolio of the user to console.

        Keyword arguments:
        t_cost_base -- Total Cost Base of Share Holding
        t_value -- Total Value of Share Holding
        t_units -- Total Units of Share Holding
        t_capital_gain_ndiscounted -- Total Capital Gain that is not Discounted
        t_capital_gain_discounted -- Total Capital Gain that is Discounted
        t_capital_loss -- Total Capital Losses

    """
    print('\n')
    summary_text_format = fg("white") + attr("bold") + bg("blue")
    print_text = "****** Summary of Share Holding - These are unrealised values ******"
    print(stylize(print_text, summary_text_format))
    summary_text_format = fg("white") + attr("bold") + bg("green")
    print(stylize("Total Cost Base of Share Holding : " + str(t_cost_base), summary_text_format))
    print(stylize("Total Value of Share Holding : " + str(t_value), summary_text_format))
    print(stylize("Total Units of Share Holding : " + str(t_units), summary_text_format))
    print_text = "Total Capital Gain that is not Discounted : " + str(t_capital_gain_ndiscounted)
    print(stylize(print_text, summary_text_format))
    print_text = "Total Capital Gain that is Discounted : " + str(t_capital_gain_discounted)
    print(stylize(print_text, summary_text_format))
    summary_text_format = fg("white") + attr("bold") + bg("red")
    print(stylize("Total Capital Losses : " + str(t_capital_loss), summary_text_format))
    print('\n')


def convert_share_file_to_dict(filename):
    """
        Converts the share portfolio file to a Ordered Dictionary.
        It maintains the order of rows and columns. The Reader is the
        handle to Ordered dictionary and is used to go through rows
        and columns. An exception is thrown if there is an issue with
        the conversion.

        Keyword arguments:
        filename -- Filename of the share file. The file is in the same
        directory as the code. Placing the file in other directories is
        not tested for this release.

    """
    exists = os.path.isfile(filename)
    if not exists:
        raise ShareCalculationException(f'The file {filename} does not exist.')
    if exists:
        reader = csv.DictReader(open(filename))
        return reader


def add_live_unit_price_share_hold(share_dict, price_dict=None):
    """
    The most important function to go through the share portfolio and calculate
    the capital gains discounted, capital gains non-discounted and loses.
    Discounts are calculated based on the date of purchase and based on Australian
    Taxation Offices capital gains discounting process.
    Calculates the percentage gains or loses based on the ticker +
    Date of purchase + Units. Dates in future is not validated in
    this release. The calculations can be done based on the price
    file provided as input or from yahoo finance interface.

    Keyword arguments:
        share_dict -- Handle to ordered dictionary of the share portfolio created
        from the input csv file.
        price_dict -- Optional dictionary of share prices, only required if user
        wants to calculate the value of share portfolio based on a price.
    """

    # a lot of variables are used, it should be cleaned up in future releases.

    all_units_with_calculations = []
    total_capital_gain_discounted = 0
    total_capital_gain_nondiscounted = 0
    total_capital_loss = 0
    total_units = 0
    total_value = 0
    total_cost_base = 0
    for raw in share_dict:
        new_dict_values = collection.OrderedDict()
        value = 0
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
        for key_sh, value_sh in raw.items():
            new_dict_values[key_sh] = value_sh
            if key_sh.lower() == 'ticker':
                try:
                    if price_dict is not None:
                        for name_sh, pr_ice in price_dict.items():
                            if name_sh.lower() == value_sh.lower():
                                unit_price = float(pr_ice)
                    else:
                        unit_price = get_most_recent_share_price(value_sh.upper()+'.AX')
                    if unit_price == 0:
                        raise ShareCalculationException(
                            'Unit price not available to continue calculation!')
                except ShareCalculationException as price_excep:
                    raise price_excep
            elif key_sh.lower() == 'units':
                number_of_units = float(value_sh)
            elif key_sh.lower() == 'cost base':
                cost_base = float(value_sh)
            elif key_sh.lower() == 'date of purchase':
                date_of_purchase = dt.datetime.strptime(value_sh, '%d/%m/%Y')
            else:
                continue

        new_dict_values['Unit Price'] = round(unit_price, 3)
        value = unit_price * number_of_units
        total_value += value
        total_units += number_of_units
        total_cost_base += cost_base
        new_dict_values['Value'] = round(value, 3)
        capital_gain_loss = (unit_price * number_of_units) -  cost_base
        days_held = (todays_date - date_of_purchase).days
        if capital_gain_loss >= 0:
            capital_gain_nondiscounted = capital_gain_loss
            capital_gain_percentage = (capital_gain_nondiscounted/cost_base)*100
            capital_loss_percentage = 0
            capital_loss = 0
            if days_held > 365:
                capital_gain_discounted = capital_gain_loss/2
            else:
                capital_gain_discounted = 0
        else:
            capital_loss = capital_gain_loss
            capital_gain_discounted = 0
            capital_gain_nondiscounted = 0
            capital_loss_percentage = (capital_loss/cost_base)*100
        total_capital_gain_discounted += capital_gain_discounted
        total_capital_gain_nondiscounted += capital_gain_nondiscounted
        total_capital_loss += capital_loss
        new_dict_values['Capital Gain Non Discounted'] = round(capital_gain_nondiscounted, 3)
        new_dict_values['Capital Gain Discounted'] = round(capital_gain_discounted, 3)
        new_dict_values['Capital Loss'] = round(capital_loss, 3)
        new_dict_values['Capital Gain Percentage'] = round(capital_gain_percentage, 3)
        new_dict_values['Capital Loss Percentage'] = round(capital_loss_percentage, 3)

        all_units_with_calculations.append(new_dict_values)

    # adding the sum or total columns to last line. It is ordered, so
    # that it appears properly on excel file
    new_dict_values = collection.OrderedDict()
    new_dict_values['TICKER'] = 'Total'
    new_dict_values['Date of Purchase'] = ''
    new_dict_values['Units'] = str(round(total_units, 0))
    new_dict_values['Cost Base'] = str(round(total_cost_base, 3))
    new_dict_values['Unit Price'] = ''
    new_dict_values['Value'] = str(round(total_value, 3))
    new_dict_values['Capital Gain Non Discounted'] = str(round(total_capital_gain_nondiscounted, 3))
    new_dict_values['Capital Gain Discounted'] = str(round(total_capital_gain_discounted, 3))
    new_dict_values['Capital Loss'] = str(round(total_capital_loss, 3))
    all_units_with_calculations.append(new_dict_values)
    return all_units_with_calculations, round(total_cost_base, 3), round(total_value, 3), round(total_units, 3), round(total_capital_gain_nondiscounted, 3), round(total_capital_gain_discounted, 3), round(total_capital_loss, 3)


# Main function equivalent to run it as a terminal app.
if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(
        description='Personal Shareholding Performance')
    PARSER.add_argument(
        '-i', '--input', help='Input file name that contains a persons shareholding.' +
        'The file should be in CSV format.', required=True)
    PARSER.add_argument(
        '-o', '--output', help='Output file name where the performance ' +
        'data should be stored. If this option is not used, performance data will be ' +
        'printed on console.', default="stdout")
    PARSER.add_argument(
        '-p', '--price', help='If a specific unit price should be used ' +
        'for understanding performance, it can be provided as input. This option can also ' +
        'be used if recent unit price cannot be retrieved from internet.')
    ARGS = PARSER.parse_args()

    try:
        SHARE_DICT = convert_share_file_to_dict(ARGS.input)
        PRICE_DICT = None
        if ARGS.price is not None:
            PRICE_DICT = convert_price_file_to_dict(ARGS.price)

        WAIT_STRING = "Please be patient while your share holding value is calculated!"
        WAIT_TEXT_FORMAT = fg("white") + attr("bold") + bg("black")
        print('\n')
        print(stylize(WAIT_STRING, WAIT_TEXT_FORMAT))
        print('\n')

        PROCESSED_DATA, TOTAL_CST_BASE, TOTAL_VLUE, TOTAL_UNTS, TOTAL_CAPTAL_GAIN_NONDISCOUNTED, TOTAL_CAPTAL_GAIN_DISCOUNTED, TOTAL_CAPTAL_LOSS = add_live_unit_price_share_hold(SHARE_DICT, PRICE_DICT)

        write_to_file(PROCESSED_DATA, ARGS.output)
        print_to_console(PROCESSED_DATA)

        print_to_console_summary(
            TOTAL_CST_BASE, TOTAL_VLUE, TOTAL_UNTS, TOTAL_CAPTAL_GAIN_NONDISCOUNTED,
            TOTAL_CAPTAL_GAIN_DISCOUNTED, TOTAL_CAPTAL_LOSS)

    except ShareCalculationException as err:
        ERROR_TEXT_FORMAT = fg("white") + attr("bold") + bg("red")
        print(stylize(str(err), ERROR_TEXT_FORMAT))
