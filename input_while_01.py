"""
Sana 06:03:26 yil 01:01pm

Ustoz: Anvar Narzullayev

Mazvu: Input va While sikli

"""
# son = 1
#
# while son <= 10:
#
#     print(son**2,"\n")
#
#     son+=1
#
# # Foydalanuvchi kiritgan sonni kvadratini chiqaradigan dastur
#
# print("Kiritgan soningizni kvadratini chiqarib beradigan dasturga xush kelibsiz")
#
# savol = "Istalgan son kiriting:"
#
# savol += " ( Dasturni to'xtatish uchun exit deb yozing ) "
#
# i = ""
#
# while i !="exit":
#
#     i = input(savol)
#
#     if i !="exit":
#
#        print(float(i)**2)
#
# print("Dastur tugadi.")
#
# # Foydalanuvchi kiritgan sonni kvadratini chiqaradigan dastur
#
# print("Kiritgan soningizni kvadratini chiqarib beradigan dasturga xush kelibsiz")
#
# savol = "Istalgan son kiriting:"
#
# savol += "( Dasturni to'xtatish uchun exit deb yozing )"
#
# i = True
#
# while i:
#
#     i = input(savol)
#
#     if i =="exit":
#
#        i = False
#
#     else:
#
#        print(float(i)**2)
#
# print("Dastur tugadi.")
#
#          # break-Bu siklni to'xtatadigan buyruq
#
# print("Kiritgan soningizni kvadratini chiqarib beradigan dasturga xush kelibsiz")
#
# savol = "Istalgan son kiriting:"
#
# savol += "( Dasturni to'xtatish uchun exit deb yozing )"
#
# i = ""
#
# while True:
#
#     i = input(savol)
#
#     if i =="exit":
#
#         break
#
#     else:
#
#         print(float(i)**2)
#
# print("Dastur tugadi.")
#
#         # for siklida breakni qo'llash
#
# num = list(range(0,11))
#
# for i in num:
#
#     if i == 5:
#
#         break
#
#     else:
#
#         print(i, "sonining kvadrati ", i**2)
#
#         # continue - bu siklda 1ta qadam tashlab ketish operatori
#
# num = list(range(0,11))
#
# for i in num:
#
#      if i == 5:
#
#          continue
#
#      else:
#
#          print(i, "sonining kvadrati ", i**2)
#
# #Input
#
# num = list(range(0, 11))
#
# for i in num:
#
#     if i == 5:
#
#         continue
#
#     else:
#
#         print(i, "sonining kvadrati ", i ** 2)
"""

Sana 01:04:26 yil 07:04am

Ustoz: Anvar Narzullayev 

Mazvu: Input va While sikli

"""
# input

name = input("Ismingizni kiriting:\n")

question = f"Assalomu aleykum {name.title()} yoshingiz nechchida ?\n"

age = input(question)

age = int(age)

user_data = f"Ismingiz: {name.title()},\nYoshingiz: {age}"

print(user_data)




        