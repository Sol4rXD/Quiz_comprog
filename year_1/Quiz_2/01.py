player_1_name = input('Player1 name: ')
player_2_name = input('Player2 name: ')
print()

player_1_score = 0
player_2_score = 0

round = 0

def one_vs_one():
    print('__QQ      __QQ')
    print('()">  VS  ()">')
    print()

def one_vs_two():
        print('__QQ', end = '       ')
        print('O')
        print('()">' , end = '  ')
        print('VS' , end = '  ')
        print("/|\\")
        print('          ', end ='')
        print('/ \\')
        print()

def two_vs_one():
     print(' O       __QQ')
     print('/|\  VS  ()">')
     print('/ \\')
     print()

def two_vs_three():
        print(' O        /\_/\\')
        print('/|\\  VS  ( o.o )')
        print('/ \\       > ^ <')
        print()

def three_vs_two():
     print(' /\_/\        O ')
     print('( o.o )  VS  /|\\')
     print(' > ^ <       / \\')
     print()

def three_vs_one():
        print(' /\_/\       __QQ')
        print('( o.o )  VS  ()">')
        print(' > ^ < ')
        print()

def one_vs_three():
     print('__QQ       /\_/\ ')
     print('()">  VS  ( o.o )')
     print('           > ^ < ')
     print()

def two_vs_two():
        print(' O        O')
        print('/|\\  VS  /|\\')
        print('/ \\      / \\')
        print()

def three_vs_three():
        print(' /\_/\        /\_/\ ')
        print('( o.o )  VS  ( o.o )')
        print(' > ^ <        > ^ < ')
        print()
     
while True:
    if player_1_score == 3 or player_2_score == 3:
        if player_1_score == 3:
            player_win = player_1_name
        else:
            player_win = player_2_name
        print(f'{player_1_name} {player_1_score} / {player_2_name} {player_2_score}')
        print(f'{player_win} win!')
        print()
        break
    if player_1_score == player_2_score and round == 5:
        print(f'{player_1_name} {player_1_score} / {player_2_name} {player_2_score}')
        print('Draw!')
        print()
        break

    round += 1
    print(f'Round {round}!')
    print(f'{player_1_name} {player_1_score} / {player_2_name} {player_2_score}')

    player_1_choice = int(input(f"{player_1_name}'s choice (1/rat, 2/hunter and 3/lion): "))
    player_2_choice = int(input(f"{player_2_name}'s choice (1/rat, 2/hunter and 3/lion): "))

    if player_1_choice == player_2_choice:
        if player_1_choice == 1:
            one_vs_one()
        elif player_1_choice == 2:
            two_vs_two()
        elif player_1_choice == 3:
            three_vs_three()
        
    elif player_1_choice == 1 and player_2_choice == 2:
        player_1_score += 1
        one_vs_two()
        continue
    elif player_1_choice == 2 and player_2_choice == 3:
        player_1_score += 1
        two_vs_three()
        continue
    elif player_1_choice == 3 and player_2_choice == 1:
        player_1_score += 1
        three_vs_one()
        continue
    elif player_2_choice == 1 and player_1_choice == 2:
        player_2_score += 1
        two_vs_one()
        continue
    elif player_2_choice == 2 and player_1_choice == 3:
        player_2_score += 1
        three_vs_two()
        continue
    elif player_2_choice == 3 and player_1_choice == 1:
        player_2_score += 1
        one_vs_three()
        continue
