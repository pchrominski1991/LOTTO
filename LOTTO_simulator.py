import random


def user_numbs():
    while True:
        try:
            result = []
            while len(result) < 6:
                 choice = int(input("Give your choice:"))
                 if choice not in result and choice in range(1, 50):
                    result.append(choice)
                 else:
                     print("NOT correct number")
            break
        except ValueError:
             print("It's not a number! Enter the numbers again")
    print(f" Your numbers: {sorted(result)}")
    return result


def lotto():
    numbers = list(range(1, 50))
    random.shuffle(numbers)
    rnd_num = numbers[0: 6]
    chosen = user_numbs()
    shots = 0
    for number in chosen:
        if number in rnd_num:
            shots += 1
    print(f" Lotto numbers: {sorted(rnd_num)}")
    print(f"You hit {shots} {'number' if shots == 1 else 'numbers'}!")

lotto()














