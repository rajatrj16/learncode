import random

def display_board(board):
    print(' | ________________________________________________|')
    print(' |                                                 |')
    print(" | "+board[1]+"  |  "+board[2]+" | "+board[3]+"  |  "+board[4]+" | "+board[5]+"  |  "+board[6]+" | "+board[7]+"  |  "+board[8]+" | "+ board[9]+"  | "+board[10]+" | ")
    print(' | ------------------------------------------------|')
    print(" | "+board[11]+" | "+board[12]+" | "+board[13]+" | "+board[14]+" | "+board[15]+" | "+board[16]+" | "+board[17]+" | "+board[18]+" | "+ board[19]+" | "+board[20]+" | ")
    print(' | ------------------------------------------------|')
    print(" | "+board[21]+" | "+board[22]+" | "+board[23]+" | "+board[24]+" | "+board[25]+" | "+board[26]+" | "+board[27]+" | "+board[28]+" | "+ board[29]+" | "+board[30]+" |  ")    
    print(' | ------------------------------------------------|')
    print(" | "+board[31]+" | "+board[32]+" | "+board[33]+" | "+board[34]+" | "+board[35]+" | "+board[36]+" | "+board[37]+" | "+board[38]+" | "+ board[39]+" | "+board[40]+" | ")
    print(' | ------------------------------------------------|')
    print(" | "+board[41]+" | "+board[42]+" | "+board[43]+" | "+board[44]+" | "+board[45]+" | "+board[46]+" | "+board[47]+" | "+board[48]+" | "+ board[49]+" | "+board[50]+" | ")
    print(' | ------------------------------------------------|')
    print(" | "+board[51]+" | "+board[52]+" | "+board[53]+" | "+board[54]+" | "+board[55]+" | "+board[56]+" | "+board[57]+" | "+board[58]+" | "+ board[59]+" | "+board[60]+" | ")
    print(' | ------------------------------------------------|')
    print(" | "+board[61]+" | "+board[62]+" | "+board[63]+" | "+board[64]+" | "+board[65]+" | "+board[66]+" | "+board[67]+" | "+board[68]+" | "+ board[69]+" | "+board[70]+" | ")
    print(' | ------------------------------------------------|')
    print(" | "+board[71]+" | "+board[72]+" | "+board[73]+" | "+board[74]+" | "+board[75]+" | "+board[76]+" | "+board[77]+" | "+board[78]+" | "+ board[79]+" | "+board[80]+" | ")
    print(' | ------------------------------------------------|')
    print(" | "+board[81]+" | "+board[82]+" | "+board[83]+" | "+board[84]+" | "+board[85]+" | "+board[86]+" | "+board[87]+" | "+board[88]+" | "+ board[89]+" | "+board[90]+" | ")
    print(' | ________________________________________________|')
    print(' |                                                 |')

# testboard = ['X','1','2','3','4','5','6','7','8','9','10','1','2','3','4','5','6','7','8','9','10','1','2','3','4','5','6','7','8','9','10','1','2','3','4','5','6','7','8','9','10','1','2','3','4','5','6','7','8','9','10','1','2','3','4','5','6','7','8','9','10','1','2','3','4','5','6','7','8','9','10','1','2','3','4','5','6','7','8','9','10','1','2','3','4','5','6','7','8','9','10']

def generate_number():
    tambola = random.sample(range(1,91),90)
    return tambola

number = generate_number()
count = 0
theBoard = [' '] * 91
display_board(theBoard)

while count <  len(number):
    next = input("\nNext: ")
    if next == '':
        print(number[count], end="")
        count+=1
        print(f"Count is: {count}")
    elif next == 'show':
        total = ''        
        total = number[:count]
        total.sort()
        str(total)
        for i in range(0, len(total)):
            total[i] = str(total[i])
        total.insert(0,'#')
        display_board(total+theBoard)
        print(f"Numbers so far: {len(number[:count])}")
    elif next == 'finish':
        print("\nYour Lucky Numbers are: ")
        print(number)
        break

print("\nYour Game Ends Now!\n")
for i in range(0, len(number)):
    number[i] = str(number[i])
number.insert(0,'#')
display_board(number)
print(len(number))
