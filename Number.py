#code by cy king
import phonenumbers 
import time
import os
import colorama
from colorama import Fore,Style

os.system('apt update && apt upgrade -y')
os.system('pip install phonenumbers ')
os.system('pip install colorama')


print(Fore.RED+Style.BRIGHT+''' 



███╗░░██╗██╗░░░██╗███╗░░░███╗██████╗░███████╗██████╗░
████╗░██║██║░░░██║████╗░████║██╔══██╗██╔════╝██╔══██╗
██╔██╗██║██║░░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝
██║╚████║██║░░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗
██║░╚███║╚██████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║
╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝
BY CY KING

''')

  
# geocoder: to know the specific  
# location to that phone number 

from phonenumbers import geocoder 

  
Z =  input("Enter Number with country code:--")
   

phone_number = phonenumbers.parse(Z)  
# Indian phone number example: +91********** 
# Nepali phone number example: +977**********  

   

      
# this will print the country name 

print('Country:-',geocoder.description_for_number(phone_number, 'en'))


from phonenumbers import carrier 

  

   

service_provider = phonenumbers.parse(Z) 
# Indian phone number example: +91********** 
# Nepali phone number example: +977********** 

   

      
# this will print the service provider name 
time.sleep(0.9)
print('service:-',carrier.name_for_number(service_provider, 

                              'en')) 