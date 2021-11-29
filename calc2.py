def calc(a,b,c,*arg):
    if a == 1:
        return b+c
    elif a == 2:
        return b-c
    elif a == 3:
        return b*c
    elif a == 4:
        return b/c

print("***Kalkulator***")
con = "t"
while con == "t" or con == "T":
    action = int(input("Wybierz działanie:\n [1] - dodawanie\n [2] - odejmowanie\n [3] - mnożenie\n [4] - dzielenie\nTwój wybór: "))
    liczba1 = int(input("Podaj pierwszą liczbę: "))
    liczba2 = int(input("Podaj drugą liczbę: "))
    print(f"Wynik: {calc(action,liczba1,liczba2)}")
    con = input("Kontynuować? [T] - tak, [N] - nie: ")
