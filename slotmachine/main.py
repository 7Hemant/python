import random 

MAC_LINES =3
MAX_BET =100
MIN_BET =1

ROWS =3 
COLS = 3

symbol_count ={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

def get_slot_machine_spn(rows,cols,symbols):
    all_symbols =[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns=[]        
    for _ in range(cols):
        column=[]
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)    

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i!=len(column)-1:
                print(column[row],end="|")
            else:
                print(column[row],end="")   
        print()
        
def deposit():
    while True:
        amount =input("what would you like to deposit? $")
        if amount.isdigit():
           amount= int(amount)
           if amount >0:
               break 
           else:
               print("amount mmust be greater than 0")
        else:
            print("please enter a number")
    return amount

def get_number_of_lines():
    while True:
        lines =input("Enter the number of lines of bet on (1-"+ str(MAC_LINES) +")" )
        if lines.isdigit():
           lines= int(lines)
           if 1<=lines<=MAC_LINES:
               break 
           else:
               print("enter valid number of lines")
        else:
            print("please enter a number")
    return lines


def get_bet():
    while True:
        amount =input("what you amount want to bet" )
        if amount.isdigit():
           amount= int(amount)
           if MIN_BET<= amount <= MAX_BET:
               break 
           else:
               print(f"amount mmust be betwen ${MIN_BET}-{MAX_BET}")
        else:
            print("please enter a number")
    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet =bet *lines
        if total_bet> balance:
            print(f"you do not have enough to bet that mount , your  current balance is ${balance}")
        else:
            break

    print(f"you are betting ${bet} on {lines} lines. total bet is equal to: ${total_bet}")
    solts = get_slot_machine_spn(ROWS,COLS,symbol_count)
    print_slot_machine(solts)


main()


#38.35
#https://youtu.be/th4OBktqK1I?si=b0Vx86vymyTE1ks2