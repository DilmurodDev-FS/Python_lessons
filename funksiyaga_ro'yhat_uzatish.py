"""

Sana 17:04:2026 yil

Ustoz: Anvar Narzullayev

Mavzu: funksiyaga ro'yhat yuborish

"""

def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism] = baho
    return baholar

talabalar = ['dilmurod', 'otabek', 'sardor', 'xolbekjon']

baholar = bahola(talabalar)
print(baholar)