def suma(a, b):
    try:
        a = float(a)
        b = float(b)
        return a + b
    except ValueError:
        return "error"
