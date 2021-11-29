import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s', encoding="UTF-8")

def calc(choice,num1,num2):
    if choice == 1:
        logging.debug(f"Dodaję {num1} do {num2}")
        if type(num2) == list:
            num2.insert(0,num1)
            return sum(num2)
        else:
            return num1 + num2
    elif choice == 2:
        logging.debug(f"Odejmuję {num2} od {num1}")
        return num1 - num2
    elif choice == 3:       
        if type(num2) == list:
            num2.insert(0,num1)
            multi = 1
            for i in num2:
                multi *= i
            logging.debug(f"Mnożę elementy: {num2}")
            return multi
        else:
            logging.debug(f"Mnożę {num1} i {num2}")
            return num1 * num2
    elif choice == 4:
        logging.debug(f"Dzięlę {num1} przez {num2}")
        return num1 / num2

if __name__ == "__main__":
    print("***Kalkulator***")
    con = "t"
    while con == "t" or con == "T":
        while True:
            try:
                action = int(input("Wybierz działanie:\n [1] - dodawanie\n [2] - odejmowanie\n [3] - mnożenie\n [4] - dzielenie\nTwój wybór: "))
                break
            except ValueError:
                logging.warning("Podaj wlaściwą liczbę")
        if action > 4:
            logging.warning("Niewłaściwy wybór")
            con = input("Chcesz spróbowac jeszcze raz? [T] - tak, [N] - nie: ")
            continue
        if action == 1 or action == 3:
            while True:
                try:
                    input1 = float(input("Podaj pierwszą liczbę: "))
                    break
                except ValueError:
                    logging.warning("Niewłaściwa liczna. Spróbuj jeszcze raz")
            while True:
                try:
                    input2 = float(input("Podaj drugą liczbę: "))
                    break
                except ValueError:
                    logging.warning("Niewłaściwa liczba. Spróbuj jeszcze raz")
            count = input("Czy chcesz dodać kolejną liczbę? [T] lub [N]")
            if count == "T" or count == "t":
                input2 = list([input2])
                i = 3
                while count == "T" or count == "t":
                    while True:
                        try:
                            add_input = float(input(f"Podaj liczbę nr {i}: "))
                            break
                        except ValueError:
                            logging.warning("Niewłaściwa liczba. Spróbuj jeszcze raz")
                    input2.append(add_input)
                    i += 1
                    count = input("Czy chcesz dodać kolejną liczbę? [T] lub [N]")
            else:
                pass
        elif action == 2:
            while True:
                try:
                    input1 = float(input("Podaj pierwszą liczbę: "))
                    break
                except ValueError:
                    logging.warning("Niewłaściwa liczna. Spróbuj jeszcze raz")
            while True:
                try:
                    input2 = float(input("Podaj drugą liczbę: "))
                    break
                except ValueError:
                    logging.warning("Niewłaściwa liczba. Spróbuj jeszcze raz")
        elif action == 4:
            while True:
                try:
                    input1 = float(input("Podaj pierwszą liczbę: "))
                    break
                except ValueError:
                    logging.warning("Niewłaściwa liczna. Spróbuj jeszcze raz")
            while True:
                try:
                    input2 = float(input("Podaj drugą liczbę: "))
                    input1 / input2
                    break
                except (ValueError, ZeroDivisionError):
                    logging.warning("Niewłaściwa liczba lub 0. Spróbuj jeszcze raz")

        logging.info(f"Wynik: {calc(action,input1,input2)}")
        con = input("Kontynuować? [T] - tak, [N] - nie: ")