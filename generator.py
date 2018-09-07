from itertools import repeat, combinations, chain

n = 10
alpha = ["a","b","c"]

numbers = list(range(1, n))
letters = list(chain(*list(repeat(alpha, 3))))

print (numbers)
print (list(letters))

generator =list(combinations(chain(numbers,letters), 8))
index = 0
for combo in generator:
    if "a" or 9 not in combo:
        print(combo)
        index += 1
print(index)