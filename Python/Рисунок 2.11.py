dict = {1: [1, 2, 3], 2: "hello", 3: [4, 5, 6], 5: [7, 8],
        4: [9, 10]}  # створення словнику з даними
i = 0
while i < len(dict):  # проходження по ключам мловника
    i += 1
    if i in dict:  # якщо ключіснує то перевірити тип його значення
        if isinstance(dict[i], list):  # якщо значення типу список
            for elem in dict[i]:
                print(elem, end="")  # вивести елементи списку
        else:  # якщо ек список, перейти на наступну ітерація
            continue
    else:  # якщо не існує ключа, то вийти з циклу
        break
