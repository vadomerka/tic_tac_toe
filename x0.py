#!/usr/bin/python3

from enum import Enum
class FieldState(Enum):
    empty = 0
    playerx = 1
    player0 = 2

class Field():
    def __init__(self, row, col, state=FieldState.empty):
        self.state = state
        self.row = row
        self.col = col

    def __repr__(self):
        return "{}, {}, {}\n".format(self.state, self.row, self.col)


    def __str__(self):
        if self.state == FieldState.playerx:
            return "X"
        if self.state == FieldState.player0:
            return "0"
        return " "


class Game():
    def __init__(self):
        self.fields = {}       
        self.size = 3
        self.lineg = " __ __ __"
        self.line1 = "{}|{}|{}|{}|"
        self.lineabc = "  A B C"
        self.field_names = {}
        self.numbers = ['1','2','3','4','5','6','7','8','9']
        count = 1
        for i in [1,2,3]:
            for j in ["A","B","C"]:
                self.field_names[count] = j + str(i)
                count += 1

        for r in range(self.size):
            for c in range(self.size):
                n = c + r * self.size
                self.fields[n] = Field(r, c) 


    def __repr__(self):
        return "{}".format(self.fields)


    def number_by_field(self,field):
        return field.row * self.size + field.col

    def draw_head(self):
        print(self.lineabc)


    def draw_board(self):
        self.draw_head()
        for r in range(3):
            shift = r * self.size
            print(self.line1.format(r+1,self.fields[0 + shift],self.fields[1 + shift],self.fields[2 + shift]))
    

    def process_event(self, state):
        while True:
            number = input("Введите номер ячейки:\n{}\n".format(self.field_names))
            if number not in self.numbers:
                print("Введите номер ячейки из диапозона {}".format(self.numbers))
                continue
            n = int(number) - 1
            row =  n / self.size
            col = n % self.size
            return Field(int(row), int(col), state)

        return None


    def run(self):
        state = FieldState.playerx
        while True:
            self.draw_board()
            field = self.process_event(state)
            number = self.number_by_field(field)
            if self.fields[number].state != FieldState.empty:
                print("Поле уже занято")
                continue
            self.fields[number] = field
            state = FieldState.player0 if state == FieldState.playerx else FieldState.playerx
            r = self.check()
            if r:
                state = r
                self.draw_board()
                self.final(state)
                break    

    def check(self):
        fields = self.fields
        state = fields[0].state
        if state != FieldState.empty and state == fields[4].state and fields[4].state == fields[8].state:
            return  state
        state = fields[6].state
        if state != FieldState.empty and state == fields[4].state and fields[4].state == fields[2].state:
            return state
        for r in [0,1,2]:
            n = 0 + r*self.size
            state = fields[n].state
            if state != FieldState.empty and state  == fields[n + 1].state and state  == fields[n + 2].state:
                return state
        for c in [0,1,2]:
            state = fields[c].state
            size = self.size
            print("c {} fc{} fc+s{} fc+2s{} ".format(c, fields[c], fields[c+size], fields[c+2*size]))
            if state != FieldState.empty and state == fields[c + size].state and state == fields[c + 2*size].state:
                return state
    
        for k,v in fields.items():
            if v.state == FieldState.empty:
                return None
        return FieldState.empty

    def final(self, state):
        if state == FieldState.empty:
            print("Ничья!")
        elif state == FieldState.playerx:
            print("Победили Х!")
        else:
            print("Победили 0!")

def test():
    game = Game()
    game.run()
    exit()

test()

def  final(field):
    if field != " ":
        print("Победили {}!".format(field))
    else:
        print("Ничья!") 

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
        if fields[n] != " " and fields[n] == fields[n + size] and fields[n] == fields[n + 2*size]:
            return fields[n]

    for k,v in fields.items():
        if v == " ":
            return False
    return " "


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


