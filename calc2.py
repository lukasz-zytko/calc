import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s', encoding="UTF-8")

def calc(a,b,c,*arg):
    if a == 1:
        logging.debug(f"Dodaję {b} do {c}")
        return b+c
    elif a == 2:
        logging.debug(f"Odejmuję {c} od {b}")
        return b-c
    elif a == 3:
        logging.debug(f"Mnożę {b} i {c}")
        return b*c
    elif a == 4:
        logging.debug(f"Dzięlę {b} prze {c}")
        return b/c

print("***Kalkulator***")
con = "t"
while con == "t" or con == "T":
    action = int(input("Wybierz działanie:\n [1] - dodawanie\n [2] - odejmowanie\n [3] - mnożenie\n [4] - dzielenie\nTwój wybór: "))
    liczba1 = float(input("Podaj pierwszą liczbę: "))
    liczba2 = float(input("Podaj drugą liczbę: "))
    logging.info(f"Wynik: {calc(action,liczba1,liczba2)}")
    con = input("Kontynuować? [T] - tak, [N] - nie: ")
