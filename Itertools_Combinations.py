from itertools import combinations

user_input = input("ENter your word and number : ").split(" ")


word = user_input[0].upper()
number = int(user_input[1])

for i in range(1, int(number)+1):
    for comb in combinations(sorted(word), i):
        print(''.join(comb))