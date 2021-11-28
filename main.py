def calc(a,b,c):
    if a == 1:
        print(f"Wynik dodawania to: {b+c}")
    elif a == 2:
        print(f"Wynik odejmowania to: {b-c}")
    elif a == 3:
        print(f"Wynik mnożenia to: {b*c}")
    elif a == 4:
        print(f"Wynik dzielenia to: {b/c}")
    else:
        print("Nie ma takiego działania")


if __name__ == "__main__":
    print("Witaj w kalkulatorze! \nZa chwilę poprosze Cię o podanie paramerów obliczeń. Powodzenia!")
    action = int(input("Podaj proszę działanie posługując się odpowiednią liczbą:\n[1] - dodawanie\n[2] - odejmowanie\n[3] - mnożenie\n[4] - dzielenie\nTwój wybrót to: "))
    numbers = input("Teraz podaj dwie liczby, które chcesz poddać działaniu (oddziel liczby przecinkiem): ")
    liczby = numbers.split(',')
    liczba1 = int(liczby[0])
    liczba2 = int(liczby[1])

calc(action,liczba1,liczba2)