def calculate_bengal_fire_hours(c1, b1):
    hours = 0

    while c1 > 0 or b1 >= 2:
        while c1 > 0:
            c1 -= 1
            hours += 2
            b1 += 1
        while b1 >= 2 and c1 == 0:
            b1 -= 2
            c1 += 1

    return hours

# Пример использования
c1 = int(input("Введите количество новых бенгальских огней (c1): "))
b1 = int(input("Введите количество потухших бенгальских огней (b1): "))
result = calculate_bengal_fire_hours(c1, b1)
print("Часы горения:", result)
