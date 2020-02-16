#!/usr/bin/python3

lineg = " __ __ __"
line1 = "{}|{}|{}|{}|"
lineabc = "  A B C"
field_names = {}
fields = {}
for i in range(1,10):
    fields[i] = " "
count = 1
for i in [1,2,3]:
    for j in ["A","B","C"]:
        field_names[count] = j + str(i)
        count += 1
numbers = ['1','2','3','4','5','6','7','8','9']
while True:
    print(lineabc)
    print(line1.format(1,fields[1],fields[2],fields[3]))
    print(line1.format(2,fields[4],fields[5],fields[6]))
    print(line1.format(3,fields[7],fields[8],fields[9]))
    number = input("Введите номер ячейки:\n{}\n".format(field_names))
    if number not in numbers:
        print("Введите номер ячейки из диапозона {}".format(numbers))
        continue
    else:
        number = int(number)
        fields[number] = "X"



