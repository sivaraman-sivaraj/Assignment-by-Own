
"""
Created on Tue Jul 14 10:53:07 2020

@author: Sivaraman Sivaraj
"""

import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

# Entering the phone number with country code.
phone_number = phonenumbers.parse("+919944244734")

#printing the country name
print(geocoder.description_for_number(phone_number,'en'))
#printing the service provider
print(carrier.name_for_number(phone_number,'en'))



