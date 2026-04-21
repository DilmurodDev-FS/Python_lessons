# kvadrat = lambda x, y: x**y
#
# print(kvadrat(3,2))

mevalar =['olma', 'anor', 'behi', 'banan', 'qovun']

harf ='o'

# meva_h = list(filter(lambda x:x.startswith(harf), mevalar))
#
# print(meva_h)

meva_len = list(filter(lambda x:(len(x) <= 4 and x.startswith(harf),), mevalar))

print(meva_len)