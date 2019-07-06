Personal Share Holding Performance is a tool that can summarise the value of share portfolio
for a single user. It will provide a report that lists all the shares, units, cost base (purchase price including the brokerage charges), latest unit price of each share, total value of the units, discounted and non-discounted capital gain for taxation purpose, losses and percentage gains or loses to help with further investigation and decision to sell or hold. 



## Clone

- Clone this repo to your local machine using `https://github.com/pramodsreek/personal_share_holding_performance.git`

## Features

- Get the summary of value of ASX listed share portfolio
- Get the capital gains, discounted capital gains and losses
- Get the latest value of each share holding

## Help File

Dependencies used are:

- Yahoo finance
- Colored 
- Pyinstaller
- Pylint
- Pytest

```
pip3 install yahoo-fin
pip3 install colored --upgrade
pip install PyInstaller
pip install pylint
pip install pytest
```

### **Installation**

Python code can be run on command line if python 3 is installed on the machine. Or the executable can be used to run Personal Share Holding app.

#### Running the executable file

To run the program, find the executable file in the dist folder and double click. This will open and run the program with all dependencies installed.

#### Compiling the program yourself

Downloaded `personal_sharehold_performance.py` to make changes and to make it into an executable program to share, pyinstaller can be used. The following can be used:

```
pyinstaller personal_sharehold_performance.py --clean -F
```

The file will be in the dist folder of the src directory.

#### Editing the file in IDE or terminal

 Run `python3 personal_sharehold_performance.py -i Capitalgains.csv -p Shareprice.csv -o output.csv`in the terminal to execute.

### How to use Personal Sharehold Performance App

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

`python3 personal_sharehold_performance.py -i Capitalgains.csv -p Shareprice.csv -o output.csv`

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



### System requirements

Operating System - Mac OS or Windows 10 OS with Python 3 installed and connection to internet if live data is required.

## FAQ

Capital Gains and Losses - To learn more about Capital gains and loses, please visit the Australian Taxation Office website. Capital gains are discounted if the unit of share is held for more than a year. Capital loses from the past financial years are applied before discounting. Loses can be carried forward.  https://www.ato.gov.au/General/Capital-gains-tax/

Margin Lending - Margin loans are loans that are borrowed to invest and amount of loan that can be borrowed is based on the value of the share holding. If the value of share holding decreases, there is a risk of Margin call. https://www.moneysmart.gov.au/investing/borrowing-to-invest/margin-loans

## Testing

Please use pytest to run. There is a test code in the repository. It can be modified for additional tests.

## Enhancements

Additional information can be added to help make better decisions about selling or retaining shares. 

## License

[![License](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)](http://badges.mit-license.org/)

- **MIT license**

  ©️ Pramod S 2019