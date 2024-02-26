import phonenumbers
from phonenumbers import timezone,geocoder,carrier
number = input("enter your phone number:")
phone = phonenumbers.parse(number)
print(type(phone))
time = timezone.time_zones_for_number(phone)
sim_deatails = carrier.name_for_number(phone,"en")
rgister = geocoder.description_for_number(phone,"en")

print(number)
print(phone)
print(time)
print(sim_deatails)
print(rgister)
