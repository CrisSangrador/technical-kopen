# Technical Assesment for Kopen 👩🏻‍💻

### Project description:

This project aims to calculate the amortization table for a mortgage, considering a monthly payment, interest rate, and additional payments made annually. 

### Contents:

This repository contains:

- A folder named `src`, where there's a file called `support.py` which contains the function designed to calculate the amortization of a mortgage.

- A file named `main.py`, where we import the function from `support.py` so we can use the mortgage amortization calculation in our main program. It also generates a `.csv` file with the amortization table data.

- A `.csv` file, which records the amortization calculation of our mortgage. 

### Technical stack

This project was developed in [Python 3.10](https://docs.python.org/3.10/).

It also uses the module [`csv`](https://docs.python.org/3/library/csv.html) to create and record info into `.csv` files.

### Usage

To calculate the amortization table for a mortage, simply run the `main.py` script. You can either:

- Modify the default variables included in the `main.py` script to get the results to your liking. 
- Write 'yes' when the script asks you if you want to define your own parameters. It will ask you to introduce your desired parameters. 

The expected output will be:

`Month 1, interest: ___, due: ___, due + interest: ___, to pay: ___`

`Month 2, interest: ___, due: ___, due + interest: ___, to pay: ___`

... until the mortgage is fully paid off. 