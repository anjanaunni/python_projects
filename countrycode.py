import phonenumbers
from phonenumbers import geocoder
ph=phonenumbers.parse("phone number with code")
print(geocoder.description_for_number(ph,'en'))
