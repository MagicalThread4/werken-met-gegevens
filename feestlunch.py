# 17 croissantjes van elk 39 eurocent
# 2 stokbroden van elk 2,78
# 3 kortingsbonnen van 50 eurocent

prijscroissantjes = 0.39
prijsstokbroden = 2.78
waardenkortingsbonnen = 0.5

hoeveelcroissantjes = 17
hoeveelstokbroden = 2
hoeveelkortingsbonnen = 3



bedrag1 = hoeveelcroissantjes * prijscroissantjes 
bedrag2 = hoeveelstokbroden * prijsstokbroden 
korting = waardenkortingsbonnen * hoeveelkortingsbonnen 

total = bedrag1 + bedrag2 - korting 

print(total)