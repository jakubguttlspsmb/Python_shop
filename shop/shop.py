cena = int(0)
pocet_polozek = int(0)
i = [0, 0, 0, 0, 0, 0, 0, 0, 0]
j = ["Rohlíky", "Housky", "Bagety", "Šneků", "Koblih", "Taštiček", "Anglických rohlíků", "Pizza šátečků", "Plněných baget"]
control = 0
p = 0
print("Ahoj výtej v naší pekárně můžeš si vybrat ze 3 kategorii")
while p <= 10:
        print(" ")
        kategory = int(input("1:Bíle pečivo 2:Sladké pečivo 3:Slané pečivo 4:Placení "))

        if kategory == 1:
                print(" ")
                white = int(input("1:Rohlík(2Kč) 2:Houska(3Kč) 3:Bageta(12Kč) 4:Zpět "))
                if white == 1:
                        cena += 2
                        i[0] += 1 
                elif white == 2:
                        cena += 3
                        i[1] += 1 
                elif white == 3:
                        cena += 12
                        i[2] += 1 
                else:
                        continue
                
        elif kategory == 2:
                print(" ")
                sweet = int(input("1:šnek(15Kč) 2:kobliha(12Kč) 3:taštička(12Kč) 4:Zpět "))
                if sweet == 1:
                        cena += 15
                        i[3] += 1 
                elif sweet == 2:
                        cena += 12
                        i[4] += 1 
                elif sweet == 3:
                        cena += 12
                        i[5] += 1 
                else:
                        continue
                
        elif kategory == 3:
                print(" ")
                salty = int(input("1:Anglický rohlík(22Kč) 2:Pizza šáteček(15Kč) 3:Plněná bageta(25Kč) 4:Zpět "))
                if salty == 1:
                        cena += 22
                        i[6] += 1 
                elif salty == 2:
                        cena += 15
                        i[7] += 1 
                elif salty == 3:
                        cena += 25
                        i[8] += 1 
                else:
                        continue
                
        elif kategory == 4:
            print("Celková cena:",cena,"Kč")
            while control <= 8:
                if i[control]>0:
                        print (i[control],j[control])
                control += 1
            break
