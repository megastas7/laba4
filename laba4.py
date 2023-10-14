def plural_form(number):
    if number % 10 == 1 and number % 100 != 11:
        return 'ь'
    elif number % 10 in [2, 3, 4] and (number % 100 < 10 or number % 100 >= 20):
        return 'я'
    else:
        return 'ей'


def number_to_words(number):
    units = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']

    thousands_units = ['', 'одна', 'две', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']

    teens = ['', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать',
             'восемнадцать', 'девятнадцать']
    tens = ['', 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят',
            'девяносто']
    hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']

    if number == 0:
        return 'ноль'

    words = ''
    if number // 1000 > 0:
        thousands = number // 1000
        if thousands % 10 == 1 and thousands // 10 != 1:
            words += hundreds[thousands // 100] + ' ' + tens[thousands // 10] + ' ' + thousands_units[thousands % 10] + ' тысяча '
        elif thousands // 10 == 1 and thousands % 10 != 0:
            words += hundreds[thousands // 100] + ' ' + teens[thousands % 10] + ' тысяч '
        elif thousands % 10 < 5 and thousands // 10 != 1:
            words += hundreds[thousands // 100] + ' ' + tens[thousands // 10] + ' ' + thousands_units[thousands % 10] + ' тысячи '
        else:
            words += hundreds[thousands // 100] + ' ' + tens[thousands // 10] + ' ' + thousands_units[thousands % 10] + ' тысяч '
        number %= 1000

    if number // 100 > 0:
        words += hundreds[number // 100] + ' '
        number %= 100

    if number // 10 > 1:
        words += tens[number // 10] + ' '
        number %= 10
    elif number // 10 == 1:
        words += teens[number % 10]
        number = 0

    if number > 0:
        if number == 1 and words:
            words += 'один '
        elif number == 2 and words:
            words += 'два '
        elif number < 10:
            words += units[number] + ' '

    return words.strip()


def main():
    number = int(input("Введите число от 1 до 100000: "))
    if number < 1 or number > 100000:
        print("Введено некорректное число")
        return

    words = number_to_words(number)
    print(words + ' рубл' + plural_form(number))


if __name__ == "__main__":
    main()