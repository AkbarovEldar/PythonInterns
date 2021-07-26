sum = 0
number = 0
count = 0
while count <50:
    number+=1
    if number%2 != 0:
        continue
    count+=1
    sum+=number

print('Сумма равняется: ', sum)