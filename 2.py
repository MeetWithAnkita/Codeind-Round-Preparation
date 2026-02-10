# # Suppose, There is an analog Clock having second hand only. User has 3 attempts to stop second hand.
# # User will be awarded with points a/c to following:-

# # If second hand stops at [1,5,9,11]: 10 points

# # If second hand stops at [4,7,8,10]: 20 points

# # If second hand stops at [3,2,6,12]: 30 points

# # Also, consider there are three players, declare the winner of the game.
# # note: 
# # Imagine second hand stops only at digit of clock.
# # sample run:-
# # Press 'Enter to continue and 'ctrl+c' to stop seconds hand of clock: [Enter]
# # 1
# # 2
# # 3
# # stopped and points are added --> 20
# # 5
# # 6
# # 7
# # 8
# # 9
# # 10
# # stopped and points are added --> 10
# # 12
# # 1
# # 2
# # 3
# # 4
# # 5
# # stopped and points are added 20

# # Total score: 50


from time import sleep

# def run():
#     print("Press 'Enter' to Coninue:\n Press 'CTRL+C' to stop the second hand:")

#     attempts= 1
#     points = 0
#     point_table = {}

#     name = input("Enter teh name of a player:")

#     while True:
#         try:
#             for digit in range (1, 13):
#                 print(digit)
#                 sleep(0.2) #Gap time between two digit print
#         except KeyboardInterrupt:
#             print(f"Stopped at {digit}")   
#             print("Points are added..continue...")
#             sleep(2)
#             if digit in [1,5,9,11]:
#                 points += 10 
#             elif digit in [4, 7, 8, 10]:
#                 points += 20
#             else:
#                 points += 30

#             attempts += 1
#             if attempts ==4 :
#                 print(f"{name} has scored {points} points.")
#                 point_table[name] = points
#                 ans = input("If there any other player: Y/N").lower()
#                 if ans == 'y':
#                     name = input("Enter teh name of a player:")
#                     attempts = 1
#                     points = 0

#                 else: 
#                     print("Final Result:",point_table)
#                     return
                            

# run()

from time import sleep

def run():
    print("Press 'Enter' to Continue:")
    print("Press 'CTRL+C' to stop the second hand:")

    attempts = 1
    points = 0
    point_table = {}

    name = input("Enter the name of a player: ")

    current_digit = 1   # store current position

    while True:
        try:
            for digit in range(current_digit, 13):
                print(digit)
                current_digit = digit  # update position
                sleep(0.2)

            # if reaches 12, start again from 1
            current_digit = 1

        except KeyboardInterrupt:
            print(f"Stopped at {current_digit}")
            print("Points are added..continue...")
            sleep(2)

            # Points logic
            if current_digit in [1,5,9,11]:
                points += 10
            elif current_digit in [4,7,8,10]:
                points += 20
            else:
                points += 30

            attempts += 1

            # Move to next digit (clock moves forward)
            current_digit += 1
            if current_digit > 12:
                current_digit = 1

            if attempts > 3:
                print(f"{name} has scored {points} points.")
                point_table[name] = points

                ans = input("Any other player? (Y/N): ").lower()
                if ans == 'y':
                    name = input("Enter the name of a player: ")
                    attempts = 1
                    points = 0
                    current_digit = 1
                else:
                    print("Final Result:", point_table)
                    return

run()


