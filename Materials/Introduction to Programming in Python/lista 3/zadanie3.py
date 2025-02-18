def usun_w_nawiasach(s):
    licznik = 0
    licznik2 = 0
    nawiasy  = []
    for i in range(len(s)):
        licznik = i
        licznik2 = i
        if s[i] == "(":
            while s[licznik2] != ")":
                licznik2 += 1

            nawiasy.append(s[licznik:licznik2+1])

    
    for i in range(len(nawiasy)):
        s = s.replace(nawiasy[i], "")
    
    return s


print(usun_w_nawiasach("ala ma (klota) czarnego"))
print(usun_w_nawiasach("(nie) wiem (co) sie stalo"))
print(usun_w_nawiasach("ala ma (klota) czarnego (ktory) umie chodzic na (rekach)!"))