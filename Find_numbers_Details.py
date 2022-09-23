import phonenumbers
from phonenumbers import timezone,geocoder,carrier #timezone time btayega or geocoder area btaiyega or carrier area btaiyega
num = input("Enter your no with +__: ")
phone = phonenumbers.parse(num) #yha hamne phonenumbers ko as a function use kiya h or parse humko phone number ki puri jankari de dega
time = timezone.time_zones_for_number(phone)
cr = carrier.name_for_number(phone,"en") #cr variable h carrier ko variable bnaya phir phone number liya or usko english me print kraya
reg =geocoder.description_for_number(phone,"en")

print(phone)
print(time)
print(cr)
print(reg)