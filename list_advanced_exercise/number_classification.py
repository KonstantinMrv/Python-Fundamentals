numbers = [int(num) for num in input().split(", ")]

positive = [num for num in numbers if num >= 0]
negative = [num for num in numbers if num < 0]
even = [num for num in numbers if num % 2 == 0]
odd = [num for num in numbers if num % 2 != 0]

print("Positive:", end=" ")
print(*positive, sep=", ")
print("Negative:", end=" ")
print(*negative, sep=", ")
print("Even:", end=" ")
print(*even, sep=", ")
print("Odd:", end=" ")
print(*odd, sep=", ")
