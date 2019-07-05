#!/usr/bin/python3
import collections as collection
import csv
from os import remove as delete_file
from personal_sharehold_performance import add_live_unit_price_share_hold

def test_unit_price_and_calculate():

    TEST_TEXT_SHARE = "ALX,15/12/2008,10,88.87\n"
    TEST_FILENAME_SHARE = "share.csv"

    create_share_file(TEST_FILENAME_SHARE)

    with open(TEST_FILENAME_SHARE) as file_share:
        lines_share = file_share.readlines()
        final_line_share = lines_share[-1]

    assert final_line_share == TEST_TEXT_SHARE

    TEST_TEXT_PRICE = "ALX,1/07/2019,8.887\n"
    TEST_FILENAME_PRICE = "price.csv"

    create_price_file(TEST_FILENAME_PRICE)

    with open(TEST_FILENAME_PRICE) as file:
        lines = file.readlines()
        final_line = lines[-1]

    assert final_line == TEST_TEXT_PRICE    

    delete_file(TEST_FILENAME_SHARE)
    delete_file(TEST_FILENAME_PRICE)







def test_unit_price_and_calculate1():

    TEST_TEXT_SHARE = "ALX,15/12/2008,10,88.87\n"
    TEST_FILENAME_SHARE = "share.csv"

    create_share_file(TEST_FILENAME_SHARE)

    with open(TEST_FILENAME_SHARE) as file_share:
        lines_share = file_share.readlines()
        final_line_share = lines_share[-1]

    assert final_line_share == TEST_TEXT_SHARE

    TEST_TEXT_PRICE = "ALX,1/07/2019,8.887\n"
    TEST_FILENAME_PRICE = "price.csv"

    create_price_file(TEST_FILENAME_PRICE)

    with open(TEST_FILENAME_PRICE) as file:
        lines = file.readlines()
        final_line = lines[-1]

    assert final_line == TEST_TEXT_PRICE    

    delete_file(TEST_FILENAME_SHARE)
    delete_file(TEST_FILENAME_PRICE)

def test_unit_price_and_calculate2():

    TEST_TEXT_SHARE = "ALX,15/12/2008,10,88.87\n"
    TEST_FILENAME_SHARE = "share.csv"

    create_share_file(TEST_FILENAME_SHARE)

    with open(TEST_FILENAME_SHARE) as file_share:
        lines_share = file_share.readlines()
        final_line_share = lines_share[-1]

    assert final_line_share == TEST_TEXT_SHARE

    TEST_TEXT_PRICE = "ALX,1/07/2019,8.887\n"
    TEST_FILENAME_PRICE = "price.csv"

    create_price_file(TEST_FILENAME_PRICE)

    with open(TEST_FILENAME_PRICE) as file:
        lines = file.readlines()
        final_line = lines[-1]

    assert final_line == TEST_TEXT_PRICE    

    delete_file(TEST_FILENAME_SHARE)
    delete_file(TEST_FILENAME_PRICE)

def create_share_file(filename):

    all_units_with_calculations = []

    new_dict_values = collection.OrderedDict()
    new_dict_values['TICKER'] = 'ALQ'
    new_dict_values['Date of Purchase'] = '13/12/2008'
    new_dict_values['Units'] = '10'
    new_dict_values['Cost Base'] = '190.71'

    all_units_with_calculations.append(new_dict_values)

    new_dict_values = collection.OrderedDict()
    new_dict_values['TICKER'] = 'ALU'
    new_dict_values['Date of Purchase'] = '14/12/2008'
    new_dict_values['Units'] = '10'
    new_dict_values['Cost Base'] = '377'

    all_units_with_calculations.append(new_dict_values)

    new_dict_values = collection.OrderedDict()
    new_dict_values['TICKER'] = 'ALX'
    new_dict_values['Date of Purchase'] = '15/12/2008'
    new_dict_values['Units'] = '10'
    new_dict_values['Cost Base'] = '88.87'

    all_units_with_calculations.append(new_dict_values)

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = [
            'TICKER', 'Date of Purchase', 'Units', 'Cost Base']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row_cal in range(len(all_units_with_calculations)):
            writer.writerow(all_units_with_calculations[row_cal])

def create_price_file(filename):

    all_units_with_calculations = []

    new_dict_values = collection.OrderedDict()
    new_dict_values['TICKER'] = 'ALQ'
    new_dict_values['Date'] = '1/07/2019'
    new_dict_values['Unit Price'] = '19.071'

    all_units_with_calculations.append(new_dict_values)

    new_dict_values = collection.OrderedDict()
    new_dict_values['TICKER'] = 'ALU'
    new_dict_values['Date'] = '1/07/2019'
    new_dict_values['Unit Price'] = '37.7'

    all_units_with_calculations.append(new_dict_values)

    new_dict_values = collection.OrderedDict()
    new_dict_values['TICKER'] = 'ALX'
    new_dict_values['Date'] = '1/07/2019'
    new_dict_values['Unit Price'] = '8.887'

    all_units_with_calculations.append(new_dict_values)

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = [
            'TICKER', 'Date', 'Unit Price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row_cal in range(len(all_units_with_calculations)):
            writer.writerow(all_units_with_calculations[row_cal])