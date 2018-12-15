def f():
    try:
        a = input("type a number:")
        a = float(a)
        print(a)
        return a
    """
    Return convert a number to float
    :param a: float.
    """
    except ValueError:
        print("Invalid value")

f()
