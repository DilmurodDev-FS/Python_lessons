def toliq_ism_yasa(ism="anvar", familiya="narzullayev"):
    toliq_ism = F"{ism.title()} {familiya.title()}"

    return toliq_ism


talaba = toliq_ism_yasa('anvar', 'narzullayev')

print(talaba) 