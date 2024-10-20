import numpy as np
import math

# normal_round: Rounds a number to a specified number of decimal places
def normal_round(arr, decimals=0):
    factor = 10 ** decimals
    return np.floor(arr * factor + 0.5) / factor

# vectorized version of normal_round
normal_round_vec = np.vectorize(normal_round)

# round_numpy_arr: Rounds a numpy array 
# to a specified number of decimal places
def round_numpy_arr(arr, decimals):
    return normal_round_vec(arr, decimals)

def first_meaningful_digit(num):
    # Convert to positive if it's negative
    num = abs(num)
    
    if num == 0:
        return 0  # Special case for 0

    # Find the order of magnitude (the exponent in scientific notation)
    exponent = math.floor(math.log10(num))

    # Scale the number to bring the first digit to the units place
    scaled_num = num / (10 ** exponent)

    # Extract the first digit
    return int(scaled_num)

def get_exp(num):
    if num == 0:
        return 0
    return math.floor(math.log10(num))



def ceil_by_first_digit(num):
    is_one = first_meaningful_digit(num) == 1
    exp = get_exp(num)
    
    places = 1 if is_one else 0
    dec_pow = math.pow(10, -exp + places)
    
    result = math.ceil(num * dec_pow) / dec_pow
    return result

def round_by_error(num, error):
    is_one = first_meaningful_digit(error) == 1
    fract_digits = -get_exp(error) + (1 if is_one else 0)
    result = round(num, fract_digits)
    print(num, error, fract_digits, result)
    return result
    
    


