#!/usr/bin/python3
"""
Author: Pramod S
Contact: @coderacademy.edu.au
Date: 2019/06/29
Licence: GPLv3
Version: 0.1
"""

import argparse

def sum(a, b):
    return a + b

def multi(a, b):
    return a * b

def sub(a, b):
    return a - b

def write_to_file(result, filename):
    with open(filename, "w+") as file:
        file.write(result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Personal Shareholding Performance')
    parser.add_argument('-i','--input', help='Input file name that contains a persons shareholding.The file should be in CSV format.', required=True)
    parser.add_argument('-o','--output', help='Output file name where the performance data should be stored. If this option is not used, performance data will be printed on console.', default="stdout")
    parser.add_argument('-p','--price', help='If a specific unit price should be used for understanding performance, it can be provided as input. This option can also be used if recent unit price cannot be retrieved from internet.')
    args = parser.parse_args()
    print ("Input file: %s" % args.input )
    print ("Output file: %s" % args.output )
#
#if __name__ == "__main__":
#    parser = argparse.ArgumentParser()
#    parser.add_argument('-ps', '--output', help="Name of the output file where the performance of shares will be #stored. This is Optional.")
#    parser.add_argument('-p', '--price', help="Name of the output file where the unit price of shares will be stored. #This is Optional.")
#    parser.add_argument('a', help='The first number')
#    parser.add_argument('b', help='The second number')
#    parser.add_argument('--add', help='Add the two numbers together',
#                        action='store_true')
#    parser.add_argument('--multiply', help='multiply the two numbers together',
#                        action='store_true')
#    parser.add_argument('--subtract', help='subtract second number from first',
#                        action='store_true')
#    
#    args = parser.parse_args()
#    try:
#        a = int(args.a)
#        b = int(args.b)
#    except ValueError as err:
#        print('Make sure a and b are both whole numbers')
#        quit()
#    result = ''
#    if args.add:
#        result += f'The sum of {a} and {b} is {sum(a,b)}\n'
#    if args.multiply:
#        result += f'The multiplication of {a} and {b} is {multi(a,b)}\n'
#    if args.subtract:
#        result += f'The {a} - {b} is {sub(a,b)}\n'
#    if args.output:
#        write_to_file(result, args.output) 
#        quit()
#    print(result)
