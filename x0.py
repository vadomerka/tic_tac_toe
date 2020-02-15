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
print(lineabc)
print(line1.format(1,"X","X","X"))
print(line1.format(2,"X","X","X"))
print(line1.format(3,"X","X","X"))

input("Введите номер ячейки:")

