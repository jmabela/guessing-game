"""A number-guessing game."""

# Put your code here

import random

def gretting():
    name = input("What's your name beautiful human? ")
    name = name.title()
    print()
    print(f"Hello, {name}! I'm glad you're here!")
    print ("So let's play a little game! ")
    print()

    return name


def option_a():
    
    print()
    number = random.randint(0,100)
    numbers_tried = []
    print ("Guess a number between 0 and 100. You can also press 'S' to show numbers you've tried")

    i = 1
    while True:
            guessed_number = input("Your guess? ")
            
            
            if guessed_number.isnumeric() == True:
                guessed_number = int(guessed_number)

                if guessed_number == number:
                    print()
                    print(f'You guessed the number! It took you {i} tries!')
                    print()
                    break
                elif guessed_number > 100:
                    
                    print("Please, numbers equal or lower than 100")
                    
                elif guessed_number < number:
                    
                    print('Number is higher')
                    numbers_tried.append(guessed_number)
                    i = i + 1
                    
                elif guessed_number > number:
                    
                    print ('Number is lower')
                    numbers_tried.append(guessed_number)
                    i = i + 1
                    
            elif guessed_number == 'S' or guessed_number == 's': 
                
                numbers_tried.sort()
                print(numbers_tried)

            else:
                print ("Only use numbers or 'S' to see list")



def option_b():
    
    print()
    while True:
            
        print(f"Okay, {name}, think of two numbers and then think of a number between them ")
        num_1 = (input('Number #1>>> '))
        num_2 = (input('Number #2>>> '))

        if num_1.isnumeric() == False or num_2.isnumeric() == False:
            print("Please only use numbers! Thank you!")
            print ("Let's try again ")

        else:
            
            num_1 = int(num_1)
            num_2 = int(num_2)
            
            i = 0
            
            if num_1 > num_2:
                num_3 = num_2
                num_2 = num_1
                num_1 = num_3
                
            answer = input(f'Is your number {num_1}? Y/N ')
            answer = answer.title()
            i = i + 1
            
            if answer == 'Y':
                
                print("That was too easy")
                
            elif answer == "N": 
                answer = input (f'Is your number {num_2}? Y/N ')
                answer = answer.title()
                i = i + 1
    
                if answer == "Y":
                    print ("Too easy!")
                elif answer == "N":
                    while True:
            
                        num_3 = (num_1+num_2) // 2
                        
                        answer = input(f'Is your number = or < or > than {num_3}? ')
                        answer = answer.title()
            
                        if answer == "=" :
                            print()
                            if i < 11:
                                print(f"Uff, that was easy! It only took me {i} tries! ")
                            else:
                                print (f"Wow it took me {i} tries but I finally got it!")
                            break
            
                        elif answer == "<":
                            num_2 = num_3 
                            i = i + 1
            
                        elif answer == ">":
                            num_1 = num_3
                            i = i + 1
            
                        else:
                            print ("That's not an option, please selet '=', '<' or '>'. Thanks!")
    
                else:
                    print("That's not an option")
            break

    else:
        print("That's not an option")
    print()

    

def main(): 
    while True:
        print("Please pick one of these options")
        print()
        print(f"A.- You, {name}, will guess the number that I'm thinking ")
        print(f"B.- I will guess the number that you, {name}, are thinking")
        print (f"C.- You, {name}, are tired of this game and want to exit")
        option = (input(">")).title()
    
        if option == "C":
            
            print(f"Goodbye, {name}! It was fun playing with you!")
            break
            
        elif option == "A":
            
            option_a()
            
        elif option == "B":
    
            option_b()        
    
        else:
            print()
            print(f"Oh oh! That's not an option, {name}!")
    



name = gretting()
main()
