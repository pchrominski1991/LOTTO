import random


def user_numbs():
    while True:
        try:
            result = []
            while len(result) < 6:                                     #  Get 6 number from user.
                 choice = int(input("Give your choice:"))
                 if choice not in result and choice in range(1, 50):   # numbers (1-49)
                    result.append(choice)                              # save numbers as elements of list
                 else:
                     print("NOT correct number")
            break
        except ValueError:                                             # if user type not a number, try again
             print("It's not a number! Enter the numbers again")
    print(f" Your numbers: {sorted(result)}")                          # print sorted list of numbers
    return result


def lotto():                                                           # chose 6 random numbers (1, 49)
    numbers = list(range(1, 50))
    random.shuffle(numbers)
    rnd_num = numbers[0: 6]
    chosen = user_numbs()
    shots = 0
    for number in chosen:                                              # check if some random numbers and numbers given by user are the same and count it
        if number in rnd_num:
            shots += 1
    print(f" Lotto numbers: {sorted(rnd_num)}")
    print(f"You hit {shots} {'number' if shots == 1 else 'numbers'}!")

lotto()














