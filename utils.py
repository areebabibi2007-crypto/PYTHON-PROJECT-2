def is_valid_amount(amount):
    """
    Check whether the entered amount is valid.
    Returns True if valid, otherwise False.
    """

    try:
        value = float(amount)

        if value < 0:
            return False

        return True

    except ValueError:
        return False


def line():
    print("=" * 40)


def title(text):
    line()
    print(text.center(40))
    line()