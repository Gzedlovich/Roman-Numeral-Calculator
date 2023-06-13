Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32

print('This program converts a positive integer up to 3,999 into the')
print('Roman number system. Enter a positive integer:', end=' ')
number = int(input())

# PROCESSING SECTION
if number >= 0 and number < 4000:
    roman_numeral = ()

    # TODO: Complete the processing of the 4 digit number
    th_dig = number // 1000    # Get the thousands digit
    

    if th_dig == 3:
      RN_TH = 'MMM'
    elif th_dig == 2:
      RN_TH = 'MM'
    elif th_dig == 1:
      RN_TH = 'M'
    else: RN_TH = ''# Convert the thousands digit into Roman numerals and concatenate it with roman_numeral
     

    h_dig = (number % 1000) // 100 # Get the hundreds digit	
    

    if h_dig == 9:
      RN_H = 'CM'
    elif h_dig == 8:
      RN_H = 'DCCC'
    elif h_dig == 7:
      RN_H = 'DCC'
    elif h_dig == 6:
      RN_H = 'DC'
    elif h_dig == 5:
      RN_H = 'D'
    elif h_dig == 4:
      RN_H = 'CD'
    elif h_dig == 3:
      RN_H = 'CCC'
    elif h_dig == 2:
      RN_H = 'CC'
    elif h_dig == 1:
      RN_H = 'C'
    else: RN_H = ''
     # Convert the hundreds digit into Roman numerals and concatenate it with roman_numeral
    

    t_dig = (number % 100) // 10 # Get the tens digit
    

    if t_dig == 9:
      RN_T = 'XC'
    elif t_dig == 8:
      RN_T = 'LXXX'
    elif t_dig == 7:
      RN_T = 'LXX'
    elif t_dig == 6:
      RN_T = 'LX'
    elif t_dig == 5:
      RN_T = 'L'
    elif t_dig == 4:
      RN_T = 'XL'
    elif t_dig == 3:
      RN_T = 'XXX'
    elif t_dig == 2:
      RN_T = 'XX'
    elif t_dig == 1:
      RN_T = 'X'
    else: RN_T = ''# Convert the tens digit into Roman numerals and concatenate it with roman_numeral
    

    o_dig = (number % 10)# Get the ones digit
    
    
    if o_dig == 9:
      RN_O = 'IX'
    elif o_dig == 8:
      RN_O = 'VIII'
    elif o_dig == 7:
      RN_O = 'VII'
    elif o_dig == 6:
      RN_O = 'VI'
    elif o_dig == 5:
      RN_O = 'V'
    elif o_dig == 4:
      RN_O = 'IV'
    elif o_dig == 3:
      RN_O = 'III'
    elif o_dig == 2:
      RN_O = 'II'
    elif o_dig == 1:
      RN_O = 'I'
    else: RN_O = ''# Convert the ones digit into Roman numerals and concatenate it with roman_numeral	
    roman_numeral = (RN_TH + RN_H + RN_T + RN_O) 

    # OUTPUT SECTION
    print()
    print('{} written in roman numerals is {}.'.format(number, roman_numeral))
    print()
else:
    print()	
    print('Invalid input!! Input must be a positive integer less than 4,000.')
