infov = 1.44
amountsheet = 100
amountlines = 50
amountsymbols = 25
symv = 4

c1 = symv * amountsymbols * amountlines * amountsheet
infovinb = infov * 1024 * 1024
c2 = round((infovinb//c1))
print("Количество книг, помещающихся на дискету:", c2)