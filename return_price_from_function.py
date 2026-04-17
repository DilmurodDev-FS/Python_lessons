"""



"""
#
# def toliq_ism_yasa(ism="anvar", familiya="narzullayev"):
#
#     toliq_ism = F"{ism.title()} {familiya.title()}"
#
#     return toliq_ism
#
# talaba = toliq_ism_yasa('anvar', 'narzullayev')
#
# print(talaba)

# def ism_familiya(name, surname, birth):
#     """ Foydlaanuvchi ismi va familiyasini qabul qilib chiqaruvchi funksiya """
#
#     print(f"Foydalanuvchi Ismi: {name.title()}\n"
#           f"Foydalanuvchi Familiyasi: {surname.title()}\n"
#           f"Foydalanuvchi yoshi: {2026 - birth}\n")
#
# ism_familiya("dilmurod", "ravshanov", birth = 2005)

"""

17:04:2026 yil

Ustoz: Anvar Narzullayev 

Mavzu: Funksiyadan qiymat qaytarish

"""

# def unite_name_surname (name, surname, middle_name = ""):
#
#     if middle_name:
#         unite_name = f"{name} {middle_name} {surname}"
#     else:
#         unite_name = f"{name} {surname}"
#
#     return(unite_name.title())
#
# print(unite_name_surname(name = "dilmurod", surname = "ravshanov", middle_name = ""))
#
# talaba = unite_name_surname("dilmurod", "ravshanov")
#
# talaba1 = unite_name_surname("otabek", "latipov")
#
# talaba2 = unite_name_surname("sardor", "jo'rayev")
#
# print(f"Darsga kelmagan talabar {talaba},{talaba1},{talaba2}")
#
# print(f"{talaba.title()} darsga kechikib keldi")

# def avto_info(kompaniya, model, rangi, karobka, yili, narhi=None ):
#
#     avto = {
#         "kompaniya": kompaniya,
#         "model": model,
#         "rangi": rangi,
#         "karobka": karobka,
#         "yili": yili,
#         "narhi": narhi
#     }
#     return avto
#
# avto1= avto_info( kompaniya = "chevrolet", model = "BMW", rangi = "qora", karobka = "avtomat", yili=2026 )
#
# avto2 = avto_info("gm", "Tahoe", "oq", "avtomat", "2025", 120000)
#
# avtolar= [avto1, avto2]
#
# print(f"Online bozordagi mavjud avtomashinalar:")
# for avto in avtolar:
#     if avto["narhi"]:
#         narhi = avto["narhi"]
#     else:
#         narhi = "Kelishiladi"
#     print(f" {avto["rangi"]} {avto["model"]}, Narhi {narhi} ")

def oraliq(min,max,step):

    sonlar = []

    while min<max:
        sonlar.append(min)
        min += step

    return sonlar

print(oraliq(0,11, step=2))
