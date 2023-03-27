words = input().split()

count_by_letter = {}

for word in words:
    for letter in word:
        if letter in count_by_letter:
            count_by_letter[letter] += 1
        else:
            count_by_letter[letter] = 1
print(count_by_letter)
# for letter, count in count_by_letter.items(): #.items() разделя ключва и съответната му стойност в общ списък
#     print(f"{letter} -> {count}")

for letter in count_by_letter :
    print(f"{letter} -> {count_by_letter[letter]}") #count_by_letter[letter] извиква стойността от ключа letter