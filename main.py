def main_simple(a, b, c):
    return a * b + c

calcul = main_simple(2, 4, 5)
print(calcul)

total = 0
def somme(a, b):
    global total
    total = a + b
    print(total)

def multiplication(c):
    result = c * total
    return result

somme(5, 10)
print("encore")
print(multiplication(3))
