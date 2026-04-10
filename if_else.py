""" 
Sana 02:03:26 yil

Ustoz: Anvar Narzullayev 

Mavzu: If-Else Shartli tarmoqlanish

"""

cars = ["bmw", "volsvagen", "mers", "damas", "neksiya"]

for avto in cars:


    if avto=="bmw":

        print(avto.upper())

    else:

        print(avto.title())
ism = input("Ismingizni kiriting:")

if ism.lower() != "ali":


       print(f"Uzr, {ism.title()} biz Alini kutyapmiz: ")

else:

    print("Assalomu aleykum Ali:")

javob = float(input("12*6 nechichi bo'ladi ? >>>"))

if javob !=72:

    print("Javob xato")

else:

    print("Javob to'g'ri:")

yosh = int(input("yoshingizni kiriting: "))

if yosh >=18:
    
    print("kirishingiz mumkin 18+ yoshda  ekansiz:")
  
else:
    print("bu kod kattalar uchun:")
       