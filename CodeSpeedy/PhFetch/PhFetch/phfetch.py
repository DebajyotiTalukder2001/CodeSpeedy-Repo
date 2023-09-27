# pip install phonenumbers

# Importing phonenumbers module  
import phonenumbers as pn  
# Importing geocoder library from the phonenumbers module  
from phonenumbers import geocoder as gc  
# Importing carrier library from the phonenumbers module  
from phonenumbers import carrier as cr  
# Importing timezone library from the phonenumbers module  
from phonenumbers import timezone as tz  

# Parsing a given phone number  
print("\n")
print("Enter Phone Number with CountryCode (eg.+91XXXXXXXXXX):")

ph = pn.parse(input())  

print("\n")

print("The given phone number after parsed will look like as the following format: ")  
print("\n")
print(ph) 
print("\n")


# Using parse phone number for finding region  
regionOfPh = gc.description_for_number(ph, 'en')  
# Printing region as the result  
print("The region of the given phone number is: ", regionOfPh)  
print("\n")


# Using parse phone number for finding the carrier  
carrierOfPh = cr.name_for_number(ph, 'en')  
# Printing carrier as the result  
print("The SIM Card operator or carrier of the given phone number is: ", carrierOfPh)  
print("\n")
 

# Using parse phone number for finding timezone  
timezoneOfPh = tz.time_zones_for_number(ph)  
# Printing carrier as the result  
print("The timezone of the given phone number is: ", timezoneOfPh)  
print("\n")


# Validating the parsed number  
validNumber = pn.is_valid_number(ph)  
# Checking possibility of the number  
possibleNumber = pn.is_possible_number(ph)  
# Printing results in the output  
print("Is the given phone number valid?: ", validNumber)  
print("\n")
print("Is the given phone number possible?: ", possibleNumber)  
print("\n")