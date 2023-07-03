'''
                        ***********************
-start : welcome message ; games options
-enter game number:
    -game1 : names seperated by length --> names < length
    -game2 : split even and odd numbers in an entered range of numbers
-options : options to exit
-finish game : play again
-yes : play again - no : exit

                        ***********************
'''


class Game:
    def __init__(self):
        while True:
            print (''' Welcome to our Game.
     Enter your Choice :
        1: Game1
        2: Game2
        3: Exit''')
            user_choice = int(input('Enter Game Number : ' ))
            if user_choice ==3:
                break
            elif user_choice == 1:
                self.game1()
            elif user_choice == 2:
                self.game2()
            user_input=input('press any key to play again or X to Exit : ')
            if user_input == 'x':
                break

    def game1 (self):
        names = input ('Enter Names : ')
        names_list = names.split(',')
        print (names_list)
        lenght = int(input('Enter lenght : '))
        for x in names_list:
            if len(x)>lenght:
                print(x)

    def game2 (self):
        start = int(input ('Enter the start : '))
        end = int(input ('Enter the end: '))
        even=[] 
        odd=[]
        for x in range(start,end+1):
            if x%2==0:
                even.append(x)
            else: 
                odd.append(x)
        print(even)
        print(odd)

G = Game() 








