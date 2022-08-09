import keyboard

def press_key_b4(key: str):
    from keyboard import is_pressed
    """
    Só dá break quando uma tecla específica é pressionada, e então, continua o código
    :param key:
    :return:
    """

    while True:
        #
        if is_pressed(key):
            if is_pressed(key):
                return True
        else:
            ...

