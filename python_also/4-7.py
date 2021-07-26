import random
import time

correctCount = 0
count = 0
NUMBER_OF_QUESTIONS = 10
startTime = time.time()

while count < NUMBER_OF_QUESTIONS:
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)

    if number1 < number2:
        number1, number2 = number2, number1

    answer = eval(input("Чему равняется " + str(number1) + " * " + str(number2) + "? "))

    if number1 * number2 == answer:
        print("Правильно!")
        correctCount += 1
    else:
        print("Ваш ответ неправильный.\n", number1, " * ", number2, "равняется",
              number1 * number2)

    count += 1

endTime = time.time()
testTime = int(endTime - startTime)
print("Правильное количество ответов ", correctCount, "из", NUMBER_OF_QUESTIONS,
    "\nTest time is", testTime, "seconds\n")
