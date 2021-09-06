# toegangsticket per persoon van 7,45 euro
# 45 minuten in de VIP-VR-GameSeat. De VIP-VR GameSeat kost per persoon 37 eurocent per 5 minuten
# toegangvr is per 5 minuten


prijsperpersoon = 7.45
toegangvr = 0.37


totaalpersoonen = 4
tijdindevrkamer = 45


vrkamer = tijdindevrkamer / 5 * 0.37
totaalpersoonenkost = prijsperpersoon * totaalpersoonen

totaalprijs = vrkamer + totaalpersoonenkost

print ("Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar " + str(totaalprijs) + " euro ")
