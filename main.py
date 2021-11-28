import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s', encoding="UTF-8")

def add(a):
    logging.debug(f"Dodaję argumenty: {a}")
    return sum(a)
def sub(a,b):
    logging.debug(f"Odejmuję {b} od {a}")
    return a - b
def mul(a):
    logging.debug(f"Mnożę argumenty: {a}")
    mult = 1
    for i in a:
        mult *= i
    return mult
def div(a,b):
    if b == 0:
        return("Nie można dzielic przez 0 :)")
    logging.debug(f"Dzięlę {a} przez {b}")
    return a / b
def exp(a,b):
    logging.debug(f"Podnoszę {a} do potegi {b}")
    return a ** b

if __name__ == "__main__":
    print("Witaj w kalkulatorze! \nZa chwilę poprosze Cię o podanie paramerów obliczeń. Powodzenia ;)")
    con = "T"
    while con == "T" or con == "t":
        while True:
            try:
                action = int(input("Podaj proszę działanie wybierając odpowiednią liczbę:\n[1] - dodawanie\n[2] - odejmowanie\n[3] - mnożenie\n[4] - dzielenie\n[5] - potęgowanie\nTwój wybrór to: "))
                break
            except ValueError:
                logging.warning(f"To nie jest liczba. Spróbuj ponownie\n")
        if action > 5:
            con = input("Wybrano niewłaściwą liczbę. Chcesz spróbować ponownie? ([T] - tak, [N] - nie): \n")
            if con == "T" or con == "t":
                continue
            else:
                break
        if action == 1 or action == 3:  
            while True:
                try:
                    liczby = input("Teraz podaj liczby, które chcesz poddać działaniu (oddziel liczby przecinkiem): ")
                    liczby_int = [int(x) for x in liczby.split(",")]
                    break
                except ValueError:
                    logging.warning(f"Spróbuj podać poprawne liczby\n")
            if action == 1:
                logging.info(f"Wynik to: {add(liczby_int)}")
            elif action == 3:
                logging.info(f"Wynik to: {mul(liczby_int)}")
        elif action == 2 or action == 4 or action == 5:
            while True:
                try:
                    liczba1 = int(input("Podaj pierwszą liczbę: "))
                    break
                except ValueError:
                    logging.warning(f"To nie jest liczba. Spróbuj ponownie\n")
            while True:
                try:
                    liczba2 = int(input("Podaj drugą liczbę: "))
                    break
                except ValueError:
                    logging.warning(f"To nie jest liczba. Spróbuj ponownie\n")
            if action == 2:
                logging.info(f"Wynik to: {sub(liczba1,liczba2)}")
            elif action == 4:
                logging.info(f"Wynik to: {div(liczba1,liczba2)}")
            elif action == 5:
                logging.info(f"Wynik to: {exp(liczba1,liczba2)}")
        con = input("\nCzy chcesz kontunuować? ([T] - tak, [N] - nie): ")