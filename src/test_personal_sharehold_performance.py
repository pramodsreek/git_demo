#!/usr/bin/python3
"""
    The test cases do not connect to external interface provide by yahoo finance.
"""
import collections as collection
import csv
from os import remove as delete_file
from personal_sharehold_performance import add_live_unit_price_share_hold
from personal_sharehold_performance import write_to_file
from personal_sharehold_performance import convert_share_file_to_dict
from personal_sharehold_performance import convert_price_file_to_dict
from personal_sharehold_performance import ShareCalculationException


def test_unit_price_and_calculate_test_exception():
    """
        Test to make sure that exception is raised. 
        (The function to create file is below)
    """
    TEST_FILENAME_SHARE = "share.csv"

    create_share_file(TEST_FILENAME_SHARE)

    TEST_FILENAME_PRICE = "price.csv"

    create_price_file_bad(TEST_FILENAME_PRICE)

    SHARE = convert_share_file_to_dict(TEST_FILENAME_SHARE)
    PRICE = convert_price_file_to_dict(TEST_FILENAME_PRICE)
    
    try:
        _, _, _, _, _, _, _ = add_live_unit_price_share_hold(SHARE, PRICE)
    except ShareCalculationException as err:
        assert str(err) == 'Unit price not available to continue calculation!'
    else:
        assert 1 == 2,'Expected ShareCalculationException but was not raised!'
    finally:
        delete_file(TEST_FILENAME_SHARE)
        delete_file(TEST_FILENAME_PRICE)



def test_unit_price_and_calculate_check_output():
    """
        The test case writes the output to a file and checks if the file content has the expected calculations.
    """
    TEST_TEXT_SHARE = "ALX,15/12/2008,10,88.87\n"
    TEST_FILENAME_SHARE = "share.csv"

    create_share_file(TEST_FILENAME_SHARE)

    with open(TEST_FILENAME_SHARE) as file_share:
        lines_share = file_share.readlines()
        final_line_share = lines_share[-1]

    assert final_line_share == TEST_TEXT_SHARE

    TEST_TEXT_PRICE = "ALX,1/07/2019,38.887\n"
    TEST_FILENAME_PRICE = "price.csv"

    create_price_file(TEST_FILENAME_PRICE)

    with open(TEST_FILENAME_PRICE) as file:
        lines = file.readlines()
        final_line = lines[-1]

    assert final_line == TEST_TEXT_PRICE    

    SHARE = convert_share_file_to_dict(TEST_FILENAME_SHARE)
    PRICE = convert_price_file_to_dict(TEST_FILENAME_PRICE)

    TEST_FILENAME_OUTPUT = "test_output.csv"
    PROCESSED_DATA, _, _, _, _, _, _ = add_live_unit_price_share_hold(SHARE, PRICE)

    write_to_file(PROCESSED_DATA, TEST_FILENAME_OUTPUT)

    with open(TEST_FILENAME_OUTPUT) as file:
        lines = file.readlines()
        final_line = lines[-1]

    assert final_line == "Total,,30.0,656.58,,856.58,400.0,150.0,-200.0,,\n" 

    delete_file(TEST_FILENAME_SHARE)
    delete_file(TEST_FILENAME_PRICE)
    delete_file(TEST_FILENAME_OUTPUT)

def test_unit_price_and_calculate_check_summary():

    TEST_TEXT_SHARE = "ALX,15/12/2008,10,88.87\n"
    TEST_FILENAME_SHARE = "share.csv"

    create_share_file(TEST_FILENAME_SHARE)

    with open(TEST_FILENAME_SHARE) as file_share:
        lines_share = file_share.readlines()
        final_line_share = lines_share[-1]

    assert final_line_share == TEST_TEXT_SHARE

    TEST_TEXT_PRICE = "ALX,1/07/2019,38.887\n"
    TEST_FILENAME_PRICE = "price.csv"

    create_price_file(TEST_FILENAME_PRICE)

    with open(TEST_FILENAME_PRICE) as file:
        lines = file.readlines()
        final_line = lines[-1]

    assert final_line == TEST_TEXT_PRICE    

    SHARE = convert_share_file_to_dict(TEST_FILENAME_SHARE)
    PRICE = convert_price_file_to_dict(TEST_FILENAME_PRICE)

    _, TOTAL_CST_BASE, TOTAL_VLUE, TOTAL_UNTS, TOTAL_CAPTAL_GAIN_NONDISCOUNTED, TOTAL_CAPTAL_GAIN_DISCOUNTED, TOTAL_CAPTAL_LOSS = add_live_unit_price_share_hold(SHARE, PRICE)


    assert TOTAL_CST_BASE == 656.58
    assert TOTAL_VLUE == 856.58
    assert TOTAL_UNTS == 30.0
    assert TOTAL_CAPTAL_GAIN_NONDISCOUNTED == 400.0
    assert TOTAL_CAPTAL_GAIN_DISCOUNTED == 150.0
    assert TOTAL_CAPTAL_LOSS == -200.0


    delete_file(TEST_FILENAME_SHARE)
    delete_file(TEST_FILENAME_PRICE)




    

        

    

def create_share_file(filename):
    #not a test case file but used to create data for testing.
    all_units_with_calculations = []

    new_dict_values = collection.OrderedDict()
    new_dict_values['TICKER'] = 'ALQ'
    new_dict_values['Date of Purchase'] = '13/12/2018'
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
    #not a test case file, but used to create data for testing.
    all_units_with_calculations = []

    new_dict_values = collection.OrderedDict()
    new_dict_values['TICKER'] = 'ALQ'
    new_dict_values['Date'] = '1/07/2019'
    new_dict_values['Unit Price'] = '29.071'

    all_units_with_calculations.append(new_dict_values)

    new_dict_values = collection.OrderedDict()
    new_dict_values['TICKER'] = 'ALU'
    new_dict_values['Date'] = '1/07/2019'
    new_dict_values['Unit Price'] = '17.7'

    all_units_with_calculations.append(new_dict_values)

    new_dict_values = collection.OrderedDict()
    new_dict_values['TICKER'] = 'ALX'
    new_dict_values['Date'] = '1/07/2019'
    new_dict_values['Unit Price'] = '38.887'

    all_units_with_calculations.append(new_dict_values)

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = [
            'TICKER', 'Date', 'Unit Price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row_cal in range(len(all_units_with_calculations)):
            writer.writerow(all_units_with_calculations[row_cal])

def create_price_file_bad(filename):
    #not a test case file, but used to create data for testing.
    all_units_with_calculations = []

    new_dict_values = collection.OrderedDict()
    new_dict_values['TICKER'] = 'ALQ1'
    new_dict_values['Date'] = '1/07/2019'
    new_dict_values['Unit Price'] = '29.071'

    all_units_with_calculations.append(new_dict_values)

    new_dict_values = collection.OrderedDict()
    new_dict_values['TICKER'] = 'ALU'
    new_dict_values['Date'] = '1/07/2019'
    new_dict_values['Unit Price'] = '17.7'

    all_units_with_calculations.append(new_dict_values)

    new_dict_values = collection.OrderedDict()
    new_dict_values['TICKER'] = 'ALX'
    new_dict_values['Date'] = '1/07/2019'
    new_dict_values['Unit Price'] = '38.887'

    all_units_with_calculations.append(new_dict_values)

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = [
            'TICKER', 'Date', 'Unit Price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row_cal in range(len(all_units_with_calculations)):
            writer.writerow(all_units_with_calculations[row_cal])