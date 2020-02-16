#!/usr/bin/python3

lineg = " __ __ __"
line1 = "{}|{}|{}|{}|"
lineabc = "  A B C"
field_names = {}
count = 1
for i in [1,2,3]:
    for j in ["A","B","C"]:
        field_names[count] = j + str(i)
        count += 1
numbers = ['1','2','3','4','5','6','7','8','9']
while True:
    print(lineabc)
    print(line1.format(1," "," "," "))
    print(line1.format(2,"X","X","X"))
    print(line1.format(3,"X","X"," "))
    number = input("Введите номер ячейки:\n{}\n".format(field_names))
    if number not in numbers:
        print("Введите номер ячейки из диапозона {}".format(numbers))
    else:
        number = int(number)



