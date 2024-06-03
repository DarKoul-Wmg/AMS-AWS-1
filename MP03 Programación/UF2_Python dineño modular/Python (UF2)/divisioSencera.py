def divisio(x, y):
    try:
        dividendo = int(x)
        divisor = int(y)
        return dividendo/divisor
    except ValueError:
        raise ValueError("'x' i 'y' s'han de poder convertir a sencers.")
    except ZeroDivisionError:
        raise ZeroDivisionError("'y' no pot ser zero.")


print(divisio(3, 5))
print(divisio(3, 0))
