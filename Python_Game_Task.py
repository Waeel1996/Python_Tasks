'''

-start : welcome message ; games options
-enter game number:
    -game1 : names seperated by length --> names < length
    -game2 : split even and odd numbers in an entered range of numbers
-options : options to exit
-finish game : play again
-yes : play again - no : exit

                        ***********************
'''


def game1 ():
    names = input ('Enter Names : ')
    names_list = names.split(',')
    print (names_list)
    lenght = int(input('Enter lenght : '))
    for x in names_list:
        if len(x)>lenght:
            print(x)


def game2 ():
    start = int(input ('Enter the start : '))
    end = int(input ('Enter the end: '))

game1()
game2()
