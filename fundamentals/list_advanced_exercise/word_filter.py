# words = input().split()
# result = []
#
# for word in words:
#     if len(word) % 2 == 0:
#         result.append(word)
#
# for word in result:
#     print(word)

words = [word for word in input().split() if len(word) % 2 == 0]
for word in words:
    print(word)