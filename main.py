import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def calc(a,b,c):
    """
    Returns the result of an operation based on the arguments entered by the user
    Arguments:
    operation mark (int)
    number 1 (int)
    number 2 (int)
    """
    if a == 1:
        logging.debug(f"Dodaję {b} do {c}")
        print(f"Wynik to: {b+c}")
    elif a == 2:
        logging.debug(f"Odejmuję {c} od {b}")
        print(f"Wynik to: {b-c}")
    elif a == 3:
        logging.debug(f"Mnożę {b} i {c}")
        print(f"Wynik to: {b*c}")
    elif a == 4:
        logging.debug(f"Dzięlę {b} przez {c}")
        print(f"Wynik to: {b/c}")     

if __name__ == "__main__":
    print("Witaj w kalkulatorze! \nZa chwilę poprosze Cię o podanie paramerów obliczeń. Powodzenia!")
    action = int(input("Podaj proszę działanie posługując się odpowiednią liczbą:\n[1] - dodawanie\n[2] - odejmowanie\n[3] - mnożenie\n[4] - dzielenie\nTwój wybrót to: "))
    if action > 4:
        logging.warning("Nie ma takiego działania, wybrano złą liczbę")
        exit(1)
    numbers = input("Teraz podaj dwie liczby, które chcesz poddać działaniu (oddziel liczby przecinkiem): ")
    liczby = numbers.split(',')
    liczba1 = int(liczby[0])
    liczba2 = int(liczby[1])
    logging.debug(f"Wybrane zostały następujęce liczby: {liczba1} i {liczba2}")

calc(action,liczba1,liczba2)