"""
Sana 20:05:2026 yil

Ustoz: Anvar Narzullayev

Mavzu: Pythonda modullar

"""
def avto_info(kompaniya, model, rangi, karobka, yili, narhi=None ):

    avto = {
        "kompaniya": kompaniya,
        "model": model,
        "rangi": rangi,
        "karobka": karobka,
        "yili": yili,
        "narhi": narhi
    }
    return avto
print("Saytimizdagi avtolar ro'yhatini shakllantiramiz.")

avtolar = []

while True:
    print("\nQuyidagi ma'lumotlarni kiriting:", end="" )

    kompaniya = input("Ishlab chiqaruvchi: ")

    model = input("Model: ")

    rangi = input("Rangi: ")

    karobka = input("Karobka: ")

    yili = input("Yili: ")

    narhi = input("Narhi: ")

    avtolar.append(avto_info(kompaniya, model, rangi, karobka, yili, narhi))

    javob =input("Yana avto qo'shasizmi? (yes/no kiritng): ")

    if javob == "no":

     break

print("\nSalonimizdagi avtolar:")

for avto in avtolar:

    if avto["narhi"]:

       narhi = avto["narhi"]

    else:
       narhi ="No'malum"

    print(f"{avto['rangi'].title()} {avto['model'].title()}, {karobka} karobka. Narhi: {narhi}")



