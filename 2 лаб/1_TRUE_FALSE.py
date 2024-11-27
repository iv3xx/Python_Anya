a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))

is_isosceles = (a == b) or (a == c) or (b == c)

print(is_isosceles)
