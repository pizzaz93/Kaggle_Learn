def is_valid_zip(zip_code):
    """
    There is a saying that "Data scientists spend 80% of their time cleaning data, and 20% of their time complaining about cleaning data." 
    Let's see if you can write a function to help clean US zip code data. Given a string, it should return whether or not that string represents
    a valid zip code. For our purposes, a valid zip code is any string consisting of exactly 5 digits.
    Returns whether the input string is a valid (5 digit) zip code
    """
    return len(zip_code) == 5 and zip_code.isdigit()
