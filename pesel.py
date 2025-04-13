"""
Zadanie 1 - Weryfikacja numeru PESEL
"""

def verify_pesel(pesel: str) -> int:
    """
    Weryfikuje numer PESEL.

    Args:
        pesel (str): Numer PESEL w postaci ciągu 11 znaków.

    Returns:
        int: 1 jeśli numer jest poprawny, 0 jeśli nie.
    """
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    suma = sum(int(pesel[i]) * weights[i] for i in range(10))
    kontrolna = (10 - (suma % 10)) % 10
    return 1 if kontrolna == int(pesel[-1]) else 0


# Przykładowe wywołania testowe:
if __name__ == "__main__":
    print(verify_pesel("97082123152"))
    print(verify_pesel("02221500655")) 
    print(verify_pesel("44051401359"))  
    print(verify_pesel("02070803628")) 
