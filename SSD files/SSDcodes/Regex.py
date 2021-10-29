import re
"""
An exercise on Regular Expressions

To check UK postcode validity
"""
try:
    s = input("Enter your postcode: ")
    r = re.search(r'[a-zA-Z][a-zA-Z]?\d[\da-zA-Z]?\s\d[abd-hjlnp-uw-zABD-HJLNP-UW-Z][abd-hjlnp-uw-zABD-HJLNP-UW-Z]', s)
    print(r.group())
except:
    print('Invalid Postcode')




