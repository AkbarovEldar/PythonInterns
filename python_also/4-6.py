import random

number = random.randint(0, 100)

print("Угадайте магическое число между 0 и 100")

guess = -1

while guess != number:
    guess = int(input("Введите ваше число: "))
    if guess == number:
        print("Да, число равняется ", number)
    elif guess > number:
        print("Ваша число слишком велико")
    else:
        print("Ваше число слишком мало")

