#!/usr/bin/python3
def  final(field):
    print("Победили {}!".format(field))




def show_field(fields):
    print(lineabc)
    print(line1.format(1,fields[1],fields[2],fields[3]))
    print(line1.format(2,fields[4],fields[5],fields[6]))
    print(line1.format(3,fields[7],fields[8],fields[9]))




def check(fields):
    if fields[1] != " " and fields[1] == fields[5] and fields[5] == fields[9]:
        return  fields[1]
    if fields[7] != " " and fields[7] == fields[5] and fields[5] == fields[3]:
        return fields[7]
    size = 3
    for r in [0,1,2]:
        n = 0 + r*3 + 1 
        if fields[n] != " " and fields[n] == fields[n + 1] and fields[n] == fields[n + 2]:
            return fields[n]
    for c in [0,1,2]:
        n = c + 1 
        if fields[n] != " " and fields[n] == fields[n + size] and fields[n] == fields[2*size]:
            return fields[n]
    return False

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
x_or_0 = True
while True:
    show_field(fields)
    number = input("Введите номер ячейки:\n{}\n".format(field_names))
    if number not in numbers:
        print("Введите номер ячейки из диапозона {}".format(numbers))
        continue
    else:
        number = int(number)
        if fields[number] != " ":
            print("Поле уже занято")
            continue
        if x_or_0:
            fields[number] = "X"
        else:
            fields[number] = "0"
        x_or_0 = not x_or_0


        r = check(fields)
        if r:
            show_field(fields)
            final(r)
            break

